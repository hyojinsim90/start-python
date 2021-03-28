## enumerate() 함수와 리스트

example_list = ["요소A", "요소B", "요소C"]

# 단순 출력
print(example_list) # ['요소A', '요소B', '요소C']
print()

# enumerate() 함수를 적용
print(enumerate(example_list)) # <enumerate object at 0x0000026F588F9780>
print()

# list() 함수로 강제 변환
print(list(enumerate(example_list))) # [(0, '요소A'), (1, '요소B'), (2, '요소C')]
print()

# 반복문과 조합하기
for i, value in enumerate(example_list): 
    print("{}번째 요소는 {}입니다.".format(i, value))

'''
0번째 요소는 요소A입니다.
1번째 요소는 요소B입니다.
2번째 요소는 요소C입니다.
'''