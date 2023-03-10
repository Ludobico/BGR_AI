import argparse
import os
import json
from Utils.AnnoFixer import AnnoFixer
from Utils.DataMerger import DataMerger
from Utils.ImageAnalysis import ImageAnalysis
ap = argparse.ArgumentParser()

ap.add_argument("-a",
                "--analysis_type",
                type=str,
                help='데이터셋을 분석해줍니다. -a "명령어" 인자로 실행할수있습니다.',
                required=True)

ap.add_argument("-s", "--save_csv", type=bool, default=False, required=False)

args = vars(ap.parse_args())

csv_flag = False

if __name__ == '__main__':
    LA = ImageAnalysis()
    if args['analysis_type'] == 'disease':
        LA.ImageDeseaseCount(csv_flag)
        if args['save_csv']:
            csv_flag = True
            LA.ImageDeseaseCount(csv_flag)
    if args['analysis_type'] == 'merge':
        DataMerger()
    if args['analysis_type'] == 'fix':
        AnnoFixer()
