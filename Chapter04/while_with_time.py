## 5초 동안 반복하기

# 시간과 관련된 기능을 가져옵니다
import time

number = 0

print(time.time()) # 1616948963.803591
print(time.time() + 5) # 1616948968.804589

# 5초동안 반복합니다
target_tick = time.time() + 5 # time.time()보다 5초 많게 설정됨
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복했습니다.".format(number)) # 5초 동안 9025471번 반복했습니다.