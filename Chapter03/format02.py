### format() 함수의 다양한 기능

## 정수를 특정 칸에 출력하기

# 정수
output_a = "{:d}".format(52) # :d를 사용하면 매개변수로 정수만 올 수 있다

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)


# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a) # 52
print("# 특정 칸에 출력하기")
print(output_b) #    52
print(output_c) #         52
print("# 빈칸을 0으로 채우기")
print(output_d) # 00052
print(output_e) # -0052
# 부호가 있을 때는 맨 앞자리를 부호로 채우고 나머지 빈 곳을 0으로 채운다
