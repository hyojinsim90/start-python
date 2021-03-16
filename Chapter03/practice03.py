## 스왑 : 변수교체
a = input("문자열 입력> ") # 안녕히
b = input("문자열 입력> ") # 가세요
print(a, b) # 안녕히 가세요

c = a
a = b
b = c

print(a, b) # 가세요 안녕히
