
numbers = [1, 2, 3, 4, 5, 6]

for i in reversed(numbers): # 필요한 시점에 reversed() 함수를 사용한다
    print("첫 번째 반복문: {}".format(i))

for i in reversed(numbers):
    print("두 번째 반복문: {}".format(i))

'''
첫 번째 반복문: 6
첫 번째 반복문: 5
첫 번째 반복문: 4
첫 번째 반복문: 3
첫 번째 반복문: 2
첫 번째 반복문: 1
두 번째 반복문: 6
두 번째 반복문: 5
두 번째 반복문: 4
두 번째 반복문: 3
두 번째 반복문: 2
두 번째 반복문: 1
'''