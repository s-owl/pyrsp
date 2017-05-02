# pyrsp
파이썬 스터디(2017.04~) 가위바위보 과제

1. 아래 모듈 코드의 `showRSP()`함수 몸체를 채워서 가위바위로 플레이어 모듈을 작성하세요. 단, `random` 모듈을 사용할 수 없습니다.

```python
#-*-coding:utf-8-*-
name = "Player 1" # 플레이어 이름
def showRSP(mine, others):
    """
    가위, 바위, 보 중 하나를 반환하는 함수
    mine : 나의 가위보위보 전적(2차원 배열)
    others : 상대방 가위바위보 전적(2차원 배열)
    [["rock",0],["paper",1],[A,B]...]
    A : "rock","scissors","paper" 중 하나
    B : 0 - 비김, 1 - 이김, 2 - 짐
    """
    return "rock" # "rock", "scissors", "paper" 중 하나 반환
```

다음 코드를 이용하여 가위바위보 플레이어 모듈이 잘 작동하는지 테스트 하세요.

```python
#-*-coding:utf-8-*-
import rsp
import rsp1

def playRSP(a, b):
    if a==b:
        return 0
    elif a=="scissors":
        if b=="rock":
            return 2
        elif b=="paper":
            return 1
    elif a=="rock":
        if b=="paper":
            return 2
        elif b=="scissors":
            return 1
    elif a=="paper":
        if b=="scissors":
            return 2
        elif b=="rock":
            return 1

aHistory = []
bHistory = []
awin = 0
bwin = 0
draw = 0
for i in range(0,100):
    a = rsp.showRSP(aHistory, bHistory)
    b = rsp1.showRSP(bHistory, aHistory)

    result = playRSP(a, b)
    if result==0:
        aHistory.append([a, 0])
        bHistory.append([b, 0])
        draw += 1
        print("비겼습니다!")
    if result==1:
        aHistory.append([a, 1])
        bHistory.append([b, 2])
        awin += 1
        print("{}(이)가 이겼습니다!".format(rsp.name))
    if result==2:
        aHistory.append([a, 2])
        bHistory.append([b, 1])
        print("{}(이)가 이겼습니다!".format(rsp1.name))
        bwin += 1

print("{} : {} 승, {} : {} 승, {}번 비김".format(rsp.name, awin, rsp1.name, bwin, draw))
if awin==bwin:
    print("비겼습니다!")
elif awin>bwin:
    print("{} 가 이겼습니다!".format(rsp.name))
else:
    print("{} 가 이겼습니다!".format(rsp1.name))
```

2. 두 가위바위보 플레이어 모듈을 불러와서, 가위바위보 대결을 붙이는 코드를 작성하세요.

- 각 플레이어 모듈의 가위/바위/보 중 하나를 반환하는 함수를 호출하여 반환받은 값을 서로 다른 변수에 각각 저장합니다.
- 두 변수에 저장된 값을 비교하여 어느 플레이어가 이겼는지 출력합니다.
- 이를 100회 반복하도록 합니다.
- 승패가 출력될 때 마다 플레이어별 이긴 횟수를 카운트 합니다. 비긴 대결로 따로 카운트 합니다.
- 100 회 반복 후 이긴 횟수가 더 많은 플레이어가 이겼음을 출력합니다, 두 플레이어 이긴 횟수가 같을 경우 비겼다고 출력합니다.
- 가위바위도 대결 전적을 따로 기록하지 않아도 됩니다.
