## 키가 존재하지 않을 때 None을 출력하는지 확인하기

# 딕셔너리를 선언합니다
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중야황산나트륨", "치자황색소"],
    "origin" : "필리핀" 
}

# 존재하지 않는 키에 접근해봄
value = dictionary.get("존재하지 않는 키")
print("값 :", value) # 값 : None

# None 확인 방법
if value == None: #None과 같은지 확인만 하면 됨
    print("존재하지 않는 키에 접근했었습니다")
