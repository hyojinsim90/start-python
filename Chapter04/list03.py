## 리스트 요소 제거 

list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# 제거방법[1] - del
del list_a[1]
print("del list_a[1]:", list_a)  # [0, 2, 3, 4, 5]

# 제거방법[2] - pop()
list_a.pop(2)
print("pop(2):", list_a) # [0, 2, 4, 5]

# 제거방법[3] - remove
list_a.remove(5)
print("list_a.remove(3):", list_a) # [0, 2, 4]

# 제거방법[4] - clear
list_a.clear()
print("list_a.clear:", list_a) # []