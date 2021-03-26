## format() 함수의 다양한 형태

# format() 함수로 숫자를 문자열로 변환하기
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

# 출력하기
print(format_a) # 5000만 원
print(format_b) # 파이썬 열공하여 첫 연봉 5000만 원 만들기
print(format_c) # 3000 4000 5000
print(format_d) # 1 문자열 True