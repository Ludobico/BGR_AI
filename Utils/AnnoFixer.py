import os
import shutil


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
