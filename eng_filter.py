# deepspeech 모델 학습을 위해 생성한 csv 파일의 텍스트에서 정규식을 이용하여 영어 포함여부에 의한 csv 분리
# 각 csv 파일의 형태는 wav_file경로, wav_file크기, 해당 wav파일에 맞는 텍스트

import csv
import re
import pandas as pd

reg = re.compile(r"[a-zA-Z]")

with open("./all_data.csv", "r", encoding="utf-8", newline='') as f:
    wr = csv.reader(f)
    a_list = list(wr)

    for a in a_list:
        if reg.search(a[-1]):
            with open(r"./eng_result.csv", "a", encoding="utf-8", newline="") as wf:
                w = csv.writer(wf)
                w.writerow(a)
        else:
            with open(r"./kor_result.csv", "a", encoding="utf-8", newline="") as wf:
                w = csv.writer(wf)
                w.writerow(a)
print("success")

