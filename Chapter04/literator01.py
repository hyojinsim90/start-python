## reversed() 함수와 이터레이터

numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print("reversed_number : ", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

'''
결과 : 
reversed_number :  <list_reverseiterator object at 0x00000171244FFFD0>
6
5
4
3
2
'''

