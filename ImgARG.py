import argparse
import os
import json

ap = argparse.ArgumentParser()

ap.add_argument("-a",
                "--analysis_type",
                type=str,
                help='label 폴더내의 질병 클래스의 종류와 개수를 출력합니다.',
                required=True)

args = vars(ap.parse_args())


class ImageAnalysis:
    def ImageDeseaseCount(self):
        self.DeseaseList = []
        self.countDict = {}
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

        for ADL in self.DeseaseList:
            if ADL not in self.countDict:
                self.countDict[ADL] = 1
            else:
                self.countDict[ADL] += 1

        for k, v in self.countDict.items():
            # print(k, v)
            # 질병 클래스
            if 'PO' in k:
                v = str(v)+str('\t 정상')
            if 'VI' in k:
                v = str(v)+str('\t 비브리오증')

            # 질병 부위 클래스
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

            print(k, v)


if __name__ == '__main__':
    LA = ImageAnalysis()
    if args['analysis_type'] == 'disease':
        LA.ImageDeseaseCount()
