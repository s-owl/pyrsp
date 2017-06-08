#-*-coding:utf-8-*-

import random

while True:
    try:
        rsp = input("가위,바위,보 중 하나를 입력하세요(1.가위 2.바위 3.보): ")
    except:
        print("1~3 중 하나를 입력하시오.")
        continue
    com = random.randint(1,3)
    if rsp == com:
        print("무승부")
    elif rsp == 1:
        if com == 2:
            print("패배")
        elif com == 3:
            print("승리")
    elif rsp == 2:
        if com == 1:
            print("승리")
        elif com == 3:
            print("패배")
    elif rsp == 3:
        if com == 1:
            print("패배")
        elif com == 2:
            print("승리")
    else:
        try:
            raise ValueError
        except ValueError:
            print("잘못 입력하였습니다")
