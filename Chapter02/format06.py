# 소수점 아래 자릿수 지정하기
output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

print(output_a) #          52.273 
print(output_b) #           52.27
print(output_c) #            52.3
# 소수점 포함 자리가 15자리가 됨
