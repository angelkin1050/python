print("안녕하세요. bmi계산기 입니다")
height = int(input("키를 입력해주세요."))
weight = float(input("몸무게를 입력해주세요."))
bmi = weight / ((height*0.01) * (height*0.01))
if bmi<18.5:
    print("저체중")
elif bmi<23:
    print("정상")
elif bmi<25:
    print("과체중")
elif bmi<30:
    print("비만")
else:
    print("고도비만")


