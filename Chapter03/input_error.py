## 입력받고 더하기

# 입력을 받습니다
string = input("입력> ")

# 출력합니다
print("입력 + 100: ", string + 100) #typeError - 문자와 숫자가 더해지는경우
"""
Traceback (most recent call last):
  File "C:/Users/tlagy/Desktop/개발 공부/python/alone_study_python/Chapter03/input_error.py", line 5, in <module>
    print("입력 + 100: ", string + 100)
TypeError: can only concatenate str (not "int") to str
"""

