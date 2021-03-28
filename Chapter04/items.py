example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C", # 이렇게 끝내도 에러 안나나봄
}

# 딕셔너리의 items() 함수 결과 출력
print(example_dictionary.items()) # dict_items([('키A', '값A'), ('키B', '값B'), ('키C', '값C')])

# for 반복문과 items() 함수 조합해서 사용
for key, element in example_dictionary.items(): # key, element 말고 num, value이런식으로 써도 똑같이 나옴
    print("dictionary[{}] = {}".format(key, element))

'''
dictionary[키A] = 값A
dictionary[키B] = 값B
dictionary[키C] = 값C
'''
