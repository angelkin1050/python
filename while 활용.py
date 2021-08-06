"""
startnum = 1
while startnum <=15:
    print(startnum)
    startnum = startnum + 1

    변수 num에 1을 대입한 후 1씩 증가시키면서 10까지의 누적 합을 구하기

num = 1
result = 0
while num<=10:
    print(num)
    result = result + num
    num = num + 1
print(result)
"""
i = 1
result = 0
num = int(input("100 이하의 정수를 입력하시오"))
if (num>100):
    print("잘못 입력하셨습니다")
    exit()
while i<= num:
    print(i)
    result = result + i
    i = i + 1
print(result)

