"""
print("안녕하세요")
weight = 60.5
height = 160
print(height)
print(weight)

print("저의 키는 %dcm 입니다"%(height))
print("저의 몸무게는 %.1fkg 입니다"%(weight))
print("키 : %dcm 몸무게 : %.1fkg"%(height,weight))

print("이름을 입력하세요")
name = input()
print(name)

name = input("이름을 입력하세요

height = float(input("키를 입력하세요"))
print(height+100)

age = int(input("당신의 나이는 몇 살입니까?"))
print("당신의 나이는 %d 이군요."%(age))
"""

num1 = int(input("첫번째 정수를 입력하세요"))
num2 = int(input("두번째 정수를 입력하세요"))
num3 = int(input("세번째 정수를 입력하세요"))
hap = num1 + num2 + num3
avg = (num1 + num2 + num3) / 3
print("%d + %d + %d = %d"%(num1,num2,num3,hap))
print("%d / %d = %.2f"%(hap,3,avg))
