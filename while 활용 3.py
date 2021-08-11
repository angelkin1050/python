
점수를 계속 입력받다가 0이 입력되면 제외하고 이전에 입력된 자료의 수와 합계,
평균을 출력하는 프로그램
(평균은 반올림하여 소수 둘째 자리)
EX)15 88 97 0

cnt = 0
sum_ = 0
num = input("점수를 입력하세요").split()
num = list(map(int, num))

while num[cnt] != 0:
    sum_=sum_ + num[cnt]
    cnt = cnt + 1
    avg = sum_/ cnt
print("입력된 자료의 개수 = %d"%cnt)
print("입력된 자료의 합계 = %d"%sum_)
print("입력된 자료의 평균 = %.2f"%avg)


정수를 입력받다가 100이상의 수가 입력이 되면 마지막 입력된 수를 포함하여
합계와 평균을 출력하는 프로그램
(평균은 반올림하여 소수 첫째 자리까지 출력)

cnt = 0
sum_ = 0
num = input("정수를 입력하세요").split()
num = list(map(int, num))

while True:
    sum_ = sum_ + num[cnt]
    if(num[cnt] >= 100):
        break
    cnt = cnt + 1
avg = sum_/ cnt
print("입력된 자료의 합계 = %d"%sum_)
print("입력된 자료의 평균 = %.1f"%avg)


정수를 계속 입력 받다가 0이 입력되면 입력된 수 중 홀수의 합과 평균을 출력하는
프로그램
(정수 미만은 버림)
cnt = 0
sum_ = 0
odd_cnt = 0
num = list(map(int, input("정수를 입력하세요").split()))

while True:
    if(num[cnt] == 0):
        break
    if(num[cnt]%2 == 1):
      sum_ = sum_ + num[cnt]
      odd_cnt = odd_cnt + 1
    cnt = cnt + 1
avg = sum_/ cnt
print("입력된 자료의 합계 = %d"%sum_)
print("입력된 자료의 평균 = %d"%avg)
 








 








