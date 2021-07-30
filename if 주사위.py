num1 = int(input("첫번 째 주사위를 던져서 나온 수를 입력하세요"))
num2 = int(input("두번 째 주사위를 던져서 나온 수를 입력하세요"))
if (num1>=4 and num2>=4):
    print("이겼습니다")
elif (num1>=4 or num2>=4):
    print("비겼습니다")
elif (num1<4 and num2<4):
    print("졌습니다")
