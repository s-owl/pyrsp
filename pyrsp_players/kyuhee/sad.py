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
	
