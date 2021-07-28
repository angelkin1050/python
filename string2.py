"""
name = input("이름을 입력하세요")
print("안녕하세요 %s의 복습입니다"%(name))
print("%s%s님 반갑습니다"%(name[1],name[2]))
massage = "날씨가 너무 덥네요"
print("%s"%(massage[4:11]))
"""
#문자열에서 찾고자 하는 문자 갯수 반환
fruit = "apple"
print(fruit.count('p'))
#index : 찾고자 하는 문자의 위치 반환
hello = "coding is happy"
print(hello.index('g'))
#upper : 소문자를 대문자로 바꾸기
upperhello = hello.upper()
print(upperhello)
#lower : 대문자를 소문자로 바꾸기
print(upperhello.lower())
#replace : 특정 문자를 다른 문자로 대체하기
print(hello.replace('coding','sleeping'))
