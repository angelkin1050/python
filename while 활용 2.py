"""
점수를 입력받아 80점 이상이면 합격 메세지 , 그렇지 않으면 불합격 메세지를 출력하는 작업을
반복하다가 0~100점 이외의 점수가 입력되면 종료하는 프로그램
"""
while True:
  score = int(input("점수를 입력하세요"))
  if(score < 0 or score > 100):
    break
  if score >= 80:
    print("합격")
  else :
    print("불합격")

    """
한개의 정수를 입력받아 양수인지 음수인지 출력하는
작업을 반복하다가 0이 입력되면 종료하는 프로그램
"""
while True:
    num = int(input("정수를 입력하세요"))
    if (num ==0):
       break
    if num > 0:
       print("양수")
    elif num < 0:
       print("음수")


