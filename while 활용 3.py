"""
점수를 계속 입력받다가 0이 입력되면 제외하고 이전에 입력된 자료의 수와 합계,
평균을 출력하는 프로그램
(평균은 반올림하여 소수 둘째 자리)
EX)15 88 97 0
"""
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
