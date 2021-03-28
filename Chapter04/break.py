## break

i = 0

while True:
    print("{}번째 반복문입니다".format(i))
    i = i + 1
    input_text = input("> 종료하시겠습니다(y/n): ")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다.")
        break

'''
0번째 반복문입니다
> 종료하시겠습니다(y/n): d
1번째 반복문입니다
> 종료하시겠습니다(y/n): n
2번째 반복문입니다
> 종료하시겠습니다(y/n): y
반복을 종료합니다.
'''