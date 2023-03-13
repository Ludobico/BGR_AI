# BGR_AI
데이터셋을 분석 및 학습하는 레파지토리

데이터셋 압축을 해제하고 레파지토리와 동일한 경로로 파일을 위시시킨다음 `utils`에있는 파일을 순차적으로 실행시키면됩니다.

## DataMerger.py
데이터셋에 있는 `이미지데이터` 와 `메타데이터`의 형식은 아래와 같습니다.

이미지 데이터
```
+---JCS221001
|       JCS221001_001.JPG
|       JCS221001_002.JPG
|       JCS221001_003.JPG
|       JCS221001_004.JPG
|       JCS221001_005.JPG
|       JCS221001_006.JPG
|       JCS221001_007.JPG
|       JCS221001_008.JPG
|       JCS221001_009.JPG
|       JCS221001_010.JPG
|       JCS221001_011.JPG
|       JCS221001_012.JPG
|       JCS221001_013.JPG
|       JCS221001_014.JPG
|       JCS221001_015.JPG
|       JCS221001_016.JPG
|       JCS221001_017.JPG
|
+---JCS221002
|       JCS221002_001.JPG
|       JCS221002_002.JPG
|       JCS221002_003.JPG
|       JCS221002_004.JPG
```

메타 데이터
```
+---JCS221001
|       JCS221001_001_annotation.json
|       JCS221001_001_original.json
|       JCS221001_002_annotation.json
|       JCS221001_002_original.json
|       JCS221001_003_annotation.json
|       JCS221001_003_original.json
|       JCS221001_004_annotation.json
|       JCS221001_004_original.json
|       JCS221001_005_annotation.json
|       JCS221001_005_original.json
|       JCS221001_006_annotation.json
|       JCS221001_006_original.json
|       JCS221001_007_annotation.json
|       JCS221001_007_original.json
|       JCS221001_008_annotation.json
|       JCS221001_008_original.json
|       JCS221001_009_annotation.json
|       JCS221001_009_original.json
|       JCS221001_010_annotation.json
|       JCS221001_010_original.json
|       JCS221001_011_annotation.json
|       JCS221001_011_original.json
|       JCS221001_012_annotation.json
|       JCS221001_012_original.json
|       JCS221001_013_annotation.json
|       JCS221001_013_original.json
|       JCS221001_014_annotation.json
|       JCS221001_014_original.json
|       JCS221001_015_annotation.json
|       JCS221001_015_original.json
|       JCS221001_016_annotation.json
|       JCS221001_016_original.json
|       JCS221001_017_annotation.json
|       JCS221001_017_original.json
|       JCS221001_disease.json
|
+---JCS221002
|       JCS221002_001_annotation.json
|       JCS221002_001_original.json
|       JCS221002_002_annotation.json
|       JCS221002_002_original.json
|       JCS221002_003_annotation.json
|       JCS221002_003_original.json
|       JCS221002_004_annotation.json
|       JCS221002_004_original.json
```

이 파일들중 학습에 실질적으로 필요한 `.JPG` 와 `annotation.json` 파일만 따로 폴더에 저장되는 파일입니다.
위의 함수를 실행시키면 레파지토리 경로내에 `result` 폴더가 생성되며 `train` 폴더에는 이미지, `lebel` 폴더에는 json 파일이 들어갑니다.

## AnnoFixer.py
현재 받은 `Annotation.json` 파일의 형식이 기존 `COCO`와 다르기 때문에 `COCO`형식으로 변환해 줘야합니다.
`DataMerger.py`를 실행시킨 후 `result` 폴더내에 `train`,`label` 이있다면 위의 코드를 실행시키면 `AnnotationFixed` 라는 폴더가 생성되며
`label`에 포함된 `json` 파일들을 `COCO` 형식으로 변환한뒤 `AnnotationFixed` 폴더내에 위치하게 됩니다.

## main.py
이미지나 어노테이션에 존재하는 데이터를 분석하는 코드입니다.

`annotation`에 있는 질병의 종류와 갯수를 출력하려면 아래의 명령을 터미널에 입력하시면됩니다.
```
python main.py -a 'disease'
or
python main.py --analysis_type 'disease'
```

출력된 질병을 csv 파일로 저장하려면 아래의 명령을 터미널에 입력하세요.

```
python main.py -a 'disease' -s true
or
python main.py --analysis_type 'disease' --save_csv true
```
