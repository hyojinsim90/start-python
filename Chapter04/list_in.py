# 리스트 안에 for문 사용하기

array = [i * i for i in range(0, 20, 2)]
# range(0, 20, 2)요소를 i라고 할때 i * i 로 리스트를 재조합해 주세요 라는 뜻
print(array) # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
