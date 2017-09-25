"""

이 프로그램은 복불복 또는 추첨의 의도로 만들어졌으며,
이 모든 저작권은 제작자한테 있습니다.
2차 수정 또는 2차 배포는 제작자의 허락 없이 할 수 없으며,
이를 어길 시에는 법적 처벌을 받을 수도 있습니다.

"""


import sys
import random
import time
import os

class LuckGame_Korean:

    def help(self):
        return "항목추가 : 추가 | 항목보기 : 보기 | 추첨시작 : 추첨 | 전체삭제 : 삭제 | 화면 정리하기 : 정리 | 도움말 : 도움말 | 나가기 : 나가기"

    LuckList = list()

user = LuckGame_Korean()

while True:
    print(user.help())

    cmd = input("명령어를 입력하시오. >> ")
    if cmd == "추가":
        text = input("추가할 문자열을 입력하시오. >> ")
        user.LuckList.append(text)
    elif cmd == "보기":
        print(user.LuckList)
    elif cmd == "추첨":
        pick = random.choice(user.LuckList)
        print("0%")
        time.sleep(random.random())
        print(str(random.randint(1, 11)) + "%")
        time.sleep(random.random())
        print(str(random.randint(12, 22)) + "%")
        time.sleep(random.random())
        print(str(random.randint(23, 33)) + "%")
        time.sleep(random.random())
        print(str(random.randint(34, 44)) + "%")
        time.sleep(random.random())
        print(str(random.randint(45, 55)) + "%")
        time.sleep(random.random())
        print(str(random.randint(56, 66)) + "%")
        time.sleep(random.random())
        print(str(random.randint(67, 77)) + "%")
        time.sleep(random.random())
        print(str(random.randint(78, 88)) + "%")
        time.sleep(random.random())
        print(str(random.randint(89, 99)) + "%")
        time.sleep(random.random())
        print(str(100) + "%" )
        time.sleep(random.random())
        print("당첨된 사람은... / 벌칙은...")
        print(pick + "입니다!!")
    elif cmd == "정리":
        os.system("cls")
    elif cmd == "삭제":
        LuckList = []
    elif cmd == "도움말":
        print(user.help())
    elif cmd == "나가기":
        sys.exit()
    else:
        print("추가, 보기, 추첨, 삭제, 정리, 도움말, 나가기 중의 명령어를 입력해 주십시오.")


#Copyright(c) All Rights Reserved. 2017 Kim DongWoo
