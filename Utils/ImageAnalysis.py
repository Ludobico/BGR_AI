import argparse
import os
import json
import csv


class ImageAnalysis:
    def ImageDeseaseCount(self, csv_flag):
        self.DeseaseList = []
        self.countDict = {}
        self.txtdict = {}
        self.curdir = os.getcwd()
        self.resultdir = os.path.join(self.curdir, 'result')
        self.labeldir = os.path.join(self.resultdir, 'label')
        self.traindir = os.path.join(self.resultdir, 'train')

        for file_name in os.listdir(self.labeldir):
            file_path = os.path.join(self.labeldir, file_name)
            with open(file_path, 'r') as f:
                data = json.load(f)

            for i in range(len(data['categories'])):
                self.DeseaseList.append(data['categories'][i]['name'])

        # print("어노테이션에 있는 질병 리스트")
        # print(self.DeseaseList)

        # 질병의 갯수를 파악되고 중복된 질병은 제외합니다.
        for ADL in self.DeseaseList:
            if ADL not in self.countDict:
                self.countDict[ADL] = 1
            else:
                self.countDict[ADL] += 1

        for k, v in self.countDict.items():
            # print(k, v)
            # 정상 클래스
            if 'PO' in k:
                v = str(v)+str('\t 정상')
                if 'OUN' in k:
                    v = str(v)+str('\t 외형')
                if 'DYN' in k:
                    v = str(v)+str('\t 체표')
                if 'NAN' in k:
                    v = str(v)+str('\t 항문')
                if 'FDN' in k:
                    v = str(v)+str('\t 등지느러미')
                if 'FAN' in k:
                    v = str(v)+str('\t 뒷지느러미')
                if 'FCN' in k:
                    v = str(v)+str('\t 꼬리지느러미')
                if 'EYN' in k:
                    v = str(v)+str('\t 눈')
                if 'MON' in k:
                    v = str(v)+str('\t 입')
                if 'BEN' in k:
                    v = str(v)+str('\t 복부')
                if 'GCN' in k:
                    v = str(v)+str('\t 아가미뚜껑')
                if 'GIN' in k:
                    v = str(v)+str('\t 아가미뚜껑/아가미')
                if 'LIN' in k:
                    v = str(v)+str('\t 간')
                if 'INN' in k:
                    v = str(v)+str('\t 장')
                if 'SPN' in k:
                    v = str(v)+str('\t 비장')
                if 'ASN' in k:
                    v = str(v)+str('\t 복수')
                if 'REN' in k:
                    v = str(v)+str('\t 생식소')
                if 'KIN' in k:
                    v = str(v)+str('\t 신장')
            # 비브리오증 클래스
            if 'VI' in k:
                v = str(v)+str('\t 비브리오증')
                if 'DYR' in k:
                    v = str(v)+str('\t 체표 발적')
                if 'DYN' in k:
                    v = str(v)+str('\t 체표 괴사')
                if 'DYA' in k:
                    v = str(v)+str('\t 체표 근육 출혈')
                if 'MOU' in k:
                    v = str(v)+str('\t 주둥이 궤양')
                if 'GIP' in k:
                    v = str(v)+str('\t 아가미 빈혈')
                if 'FDS' in k:
                    v = str(v)+str('\t 등지느러미 갈라짐')
                if 'FAS' in k:
                    v = str(v)+str('\t 뒷지느러미 갈라짐')
                if 'FCS' in k:
                    v = str(v)+str('\t 꼬리지느러미 갈라짐')
                if 'FDH' in k:
                    v = str(v)+str('\t 등지느러미 출혈')
                if 'FAH' in k:
                    v = str(v)+str('\t 뒷지느러미 출혈')
                if 'FCH' in k:
                    v = str(v)+str('\t 꼬리지느러미 출혈')
                if 'FDN' in k:
                    v = str(v)+str('\t 등지느러미 괴사')
                if 'FAN' in k:
                    v = str(v)+str('\t 뒷지느러미 괴사')
                if 'FCN' in k:
                    v = str(v)+str('\t 꼬리지느러미 괴사')
                if 'LIC' in k:
                    v = str(v)+str('\t 간 울혈')
                if 'LII' in k:
                    v = str(v)+str('\t 간 염증')
                if 'KIE' in k:
                    v = str(v)+str('\t 신장 비대')
                if 'SPE' in k:
                    v = str(v)+str('\t 비장 비대')

            print(k, v)
            self.txtdict.update({k: v})
        json_string = json.dumps(self.txtdict, ensure_ascii=False)

        # CSV 파일로 저장할거냐
        if csv_flag == True:
            with open(os.path.join(self.resultdir, 'data.txt'), 'w', encoding='UTF-8') as f:
                f.write(json_string)

            with open(os.path.join(self.resultdir, 'data.csv'), 'w', newline='', encoding='UTF-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['클래스 명', '개수', '질병', '증상'])
                for k, v in self.txtdict.items():
                    v_list = v.split('\t')

                    # 증상이 등록이 되지않은 경우
                    if len(v_list) == 2:
                        writer.writerow([k, v_list[0], v_list[1]])

                    # 증상이 등록된 경우
                    if len(v_list) == 3:
                        writer.writerow([k, v_list[0], v_list[1], v_list[2]])

            print("csv 파일 저장 완료")
            print("경로 : {0}".format(self.resultdir))
