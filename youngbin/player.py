#-*-coding:utf-8-*-
import random
name = "한영빈"
def showRSP(mine, others):
    if(len(others)>=1):
        return others[-1][0]
    else:
        return "rock"
