#-*-coding:utf-8-*-
import rsp
import rsp1
import time

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
    time.sleep(0.5)
    a = rsp.showRSP(aHistory, bHistory)
    b = rsp1.showRSP(bHistory, aHistory)

    result = playRSP(a, b)
    if result==0:
        aHistory.append([a, 0])
        bHistory.append([b, 0])
        draw += 1
        print("비겼습니다! -> {}:{} -> {}:{}".format(a,b,awin,bwin))
    if result==1:
        aHistory.append([a, 1])
        bHistory.append([b, 2])
        awin += 1
        print("{}(이)가 이겼습니다! -> {}:{} -> {}:{}".format(rsp.name,a,b,awin,bwin))
    if result==2:
        aHistory.append([a, 2])
        bHistory.append([b, 1])
        print("{}(이)가 이겼습니다! -> {}:{} -> {}:{}".format(rsp1.name,a,b,awin,bwin))
        bwin += 1

print("{} : {} 승, {} : {} 승, {}번 비김".format(rsp.name, awin, rsp1.name, bwin, draw))
if awin==bwin:
    print("비겼습니다!")
elif awin>bwin:
    print("{} 가 이겼습니다!".format(rsp.name))
else:
    print("{} 가 이겼습니다!".format(rsp1.name))
