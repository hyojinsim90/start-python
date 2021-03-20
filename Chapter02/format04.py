# 조합하기
output_h = "{:+5}".format(52) # 기호를 뒤로 밀기: 양수
output_i = "{:+5d}".format(-52) # 기호를 뒤로 밀기: 음수
output_j = "{:=+5d}".format(52) # 기호를 앞으로 밀기: 양수
output_k = "{:=+5d}".format(-52) # 기호를 앞으로 밀기: 음수
output_l = "{:+05d}".format(52) # 0으로 채우기: 양수
output_m = "{:+05d}".format(-52) # 0으로 채우기: 음수

print("조합하기")
print(output_h) #   +52
print(output_i) #   -52
print(output_j) # +  52
print(output_k) # -  52
print(output_l) # +0052
print(output_m) # -0052

