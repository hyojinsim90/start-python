## 딕셔너리의 요소에 접근하기

# 딕셔너리를 선언합니다
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중야황산나트륨", "치자황색소"],
    "origin" : "필리핀" 
}

# 출력합니다
print("name:", dictionary["name"]) # name: 7D 건조 망고
print("type:", dictionary["type"]) # type: 당절임
print("ingredient:", dictionary["ingredient"]) # ingredient: ['망고', '설탕', '메타중야황산나트륨', '치자황색소']
print("origin:", dictionary["origin"]) # origin: 필리핀
print()

# 값을 변경합니다
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"]) # name: 8D 건조 망고
print()

# 리스트 안의 특정 값 출력 가능
print(dictionary["ingredient"][1]) # 설탕


## 딕셔너리의 문자열 키와 관련된 실수

dict_key = {
    name : "7D 건조 망고",
    type : "당절임"
}
'''
에러 발생 : 
Traceback (most recent call last):
  File "c:\Chapter04\dict01.py", line 30, in <module>
    name : "7D 건조 망고",
NameError: name 'name' is not defined
에러 이유 :
name을 정의하지 않아서. name을 "name"으로 정의해야한다. 
type은 type() 함수라는 기본 식별자가 있어서 오류를 발생시키지는 않지만,
print()하면 <class 'type'>: '당절임' 으로 나온다

'''


