import os
import shutil
import glob


def DataMerger():
    curdir = os.getcwd()
    datachecker = os.path.join(curdir, '04_목포대_발송용')

    if not os.path.exists(datachecker):
        print('데이터가 존재하지 않습니다. 04_목포대_발송용 을 디렉토리에 위치시키세요')
        return

    result = os.path.join(curdir, 'result')
    if not os.path.exists(result):
        os.mkdir(result)

    train = os.path.join(curdir, 'result', 'train')
    label = os.path.join(curdir, 'result', 'label')
    targetdir = os.path.join(curdir, '04_목포대_발송용', '01_이미지데이터')
    labeldir = os.path.join(curdir, '04_목포대_발송용', '02_메타데이터', 'result')

    if not os.path.exists(train):
        os.mkdir(train)

    if not os.path.exists(label):
        os.mkdir(label)

    print('파일 생성 및 확인 완료')
    files = []

    all_files = os.listdir(targetdir)
    for folder in all_files:
        folder_path = os.path.join(targetdir, folder)
        output = glob.glob(os.path.join(folder_path, '*.JPG'))
        files.extend(output)

    for f in files:
        dst = os.path.join(train, os.path.basename(f))
        shutil.copy(f, dst)

    print('JPG 데이터 merge 완료')

    Lfiles = []

    Lall_files = os.listdir(labeldir)
    for folder in Lall_files:
        folder_path = os.path.join(labeldir, folder)
        output = glob.glob(os.path.join(folder_path, '*annotation.json'))
        Lfiles.extend(output)

    for f in Lfiles:
        dst = os.path.join(label, os.path.basename(f))
        shutil.copy(f, dst)

    print('JSON 데이터 merge 완료')


DataMerger()
