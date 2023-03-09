import os
import shutil
import json


class AnnoFixer:
    def __init__(self):
        self.curdir = os.getcwd()
        self.resultdir = os.path.join(self.curdir, 'result')
        self.labeldir = os.path.join(self.resultdir, 'label')
        self.traindir = os.path.join(self.resultdir, 'train')

        if not os.path.exists(self.resultdir):
            print('result 폴더가 존재하지 않습니다. DataMerger를 실행하세요.')
            return
        else:
            print('result 폴더 check')

        if not os.path.exists(self.labeldir):
            print('label 폴더가 존재하지 않습니다. DataMerger를 실행하세요.')
            return
        else:
            print('label 폴더 check')

        if not os.path.exists(self.traindir):
            print('train 폴더가 존재하지 않습니다. DataMerger를 실행하세요.')
            return
        else:
            print('train 폴더 check')

        self.fixCOCO()

    def fixCOCO(self, intend=2):
        self.mergedir = os.path.join(self.resultdir, 'AnnotationFixed')

        if not os.path.exists(self.mergedir):
            os.mkdir(self.mergedir)
        else:
            print('수정된 Annotation 파일 확인')
            print(self.mergedir)

        for file_name in os.listdir(self.labeldir):
            if not file_name.endswith('.json'):
                continue

            file_path = os.path.join(self.labeldir, file_name)
            with open(file_path, 'r') as f:
                data = json.load(f)

            data['images'] = [data['images']]

            fixed_file_name = os.path.splitext(file_name)[0] + '_fixed.json'
            new_file_path = os.path.join(self.mergedir, fixed_file_name)

            with open(new_file_path, 'w') as f:
                json.dump(data, f, indent=intend)

        print("Annotation JSON 파일 수정 완료")


if __name__ == "__main__":
    AnnoFixer()
