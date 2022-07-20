# deepspeech 모델 학습을 위해 생성한 csv 파일의 텍스트에서 정규식을 이용하여 특수한 문자 또는 한자, 콤마 등을 포함된 문장 제거
# 각 csv 파일의 형태는 wav_file경로, wav_file크기, 해당 wav파일에 맞는 텍스트

import csv
import re

def search_write():
    if reg.search(line[2]):
        w = csv.writer(f2)
        w.writerow(line)
    else:
        w = csv.writer(f3)
        w.writerow(line)


reg = re.compile(r"[^a-zA-Z0-9가-힣\s%&$!?.]")

with open("./all_data.csv", "r", encoding="utf-8", newline='') as f:
    with open(r"./strange_thing.csv", "a", encoding="utf-8", newline="") as f2:
        with open(r"./correct_thing.csv", "a", encoding="utf-8", newline="") as f3:
            wr = csv.reader(f)
            next(wr)
            for line in wr:
                if len(line) == 3:
                    if line[2] != '':
                        search_write()
                    else:
                        print(f'{line} -> 웃는소리 & 인식이 잘 안된 파일')
                else:
                    if line[2] == '':                    # 문장 맨 앞에 있는 , 지우기
                        line.pop(2)
                    elif line[3] == '':                            # 문장 맨 뒤에 있는 , 지우기
                        line.pop(3)
                    else:                                     # 문장 중간에 ,가 있는경우
                        line[2] = ' '.join(line[2:len(line)])
                        for i in range(len(line) - 1, -1, -1):
                            if i > 2:
                                line.pop(i)
                    search_write()

print("success")



