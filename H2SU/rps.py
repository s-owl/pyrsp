#-*-coding:utf-8-*-
name = "H2SU" # 플레이어 이름
i = 0

def showRSP(mine, others):
    if (i==0):
        i+=1
        return "paper"
    elif (i==1):
        i+=1
        return "scissors"
    elif(i==2):
        i=0
        return "rock"