# {} 개수만큼 적용된고 나머지 매개변수는 버려짐
print("{} {}".format(1, 2, 3, 4, 5)) # 1, 2

# indexError
print("{} {} {}".format(1, 2))
'''
Traceback (most recent call last):
  File "C:/Users/tlagy/Desktop/개발 공부/python/alone_study_python/Chapter03/practice04.py", line 2, in <module>
    print("{} {} {}".format(1, 2))
IndexError: Replacement index 2 out of range for positional args tuple
'''
# {}가 매개변수보다 많으면 에러 발생
