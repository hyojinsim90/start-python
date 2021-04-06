## 해결방법 1

#괄호로 문자열 연결하기

# 변수 선언
test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성됩니다"
)

print("test : ", test)
print("type(test) : ", type(test))

'''
결과 : 
test :  이렇게 입력해도 하나의 문자열로 연결되어 생성됩니다
type(test) :  <class 'str'>
'''

## 해결방법 2

# 여러 줄 문자열과 if 구문을 조합했을 떄의 문제 해결(1)

number = int(input("정수 입력> "))

if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다. \n"
        "{}는(은) 짝수입니다"
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다. \n"
        "{}는(은) 홀수입니다."
    ).format(number, number))

'''
결과 : 
정수 입력> 3
입력한 문자열은 3입니다. 
3는(은) 홀수입니다.
'''

## 해결발법 3

# 문자열의 join() 함수 사용하기

# join : 문자열.join(문자열로 구성된 리스트)

num = int(input("정수 입력> "))

if num % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다",
        "{}는(은) 짝수입니다"
    ]).format(num, num))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다",
        "{}는(은) 홀수입니다"
    ]).format(num, num))

'''
결과 : 
정수 입력> 1
입력한 문자열은 1입니다
1는(은) 홀수입니다
'''