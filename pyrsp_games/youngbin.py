#-*-coding:utf-8-*-

import random

winConditions = {"가위":"보","바위":"가위","보":"바위"}
selection = {1:"가위",2:"바위",3:"보"}
print("가위,바위,보 게임")
while True:
    player = input("가위(1), 바위(2), 보(3) 중 하나를 숫자로 선택하세요. 종료하려면, 0을 입력하세요.")
    if(player==0):
        exit()
    bot = random.choice(["가위","바위","보"])
    try:
        if player not in [1,2,3]:
            raise ValueError
    except ValueError as e:
        print(e)
        print("올바른 값이 아닙니다.")
        continue
    if winConditions[selection[player]] is bot:
        print("이겼습니다.")
    elif selection[player] is bot:
        print("비겼습니다.")
    else:
        print("졌습니다.")
    print("나:{}, 상대방:{}".format(selection[player], bot))
