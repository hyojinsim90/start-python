# 기호화 함께 출력하기
output_f = "{:+d}".format(52) # 양수
output_g = "{:+d}".format(-52) # 음수
output_h = "{: d}".format(52) # 양수: 기호 부분 공백
output_i = "{: d}".format(-52) # 음수: 기호 부분 공백->-로 채워짐

print("# 기호와 함께 출력하기")
print(output_f) # +52
print(output_g) # -52
print(output_h) #  52
print(output_i) # -52
