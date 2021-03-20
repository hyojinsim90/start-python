## 부동 소수점 출력의 다양한 형태

#float 자료형 기본

output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273) # 15칸 만들기
output_c = "{:+15f}".format(52.273) # 15칸에 부호 추가하기
output_d = "{:+015f}".format(52.273) # 15칸에 부호 추가하고 0으로 채우기

print(output_a) # 52.273000
print(output_b) #       52.273000
print(output_c) #      +52.273000
print(output_d) # +0000052.273000
