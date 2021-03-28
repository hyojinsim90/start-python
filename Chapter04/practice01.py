list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 비파과적 연산
print(list_a + list_b)

# 파괴적 연산
list_a.extend(list_b)
print(list_a)

# 결과는 둘다 [1, 2, 3, 4, 5, 6] 로 같지만, list_a는 extend해줄때 완전히 바뀌게 된다.