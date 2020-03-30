# #Block_1(Спробуйте переписати наступний код через map. Він приймає список реальних
# #  імен і замінює їх хеш-прізвищами, використовуючи  більш надійний метод-хешування.)

# names = ['Sam', 'Don', 'Daniel'] 
# names= map(hash,names)
# print(list(names))

# #Block_2(Вивести список кольору “red”, який найчастіше зустрічається в даному списку  [“red”, “green”, “black”, “red”, 
# # “brown”, “red”, “blue”, “red”, “red”, “yellow” ] використовуючи функцію filter.)

# colors=["red", "green",  "red", "brown", "red", "blue", "red", "red", "yellow" ]
# sort_red=list(filter(lambda x: x== "red", colors))
# print(sort_red)

#Block_3(. Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список 
#  в список, всі числа якого мають тип даних integer:
# 1)  використовуючи метод  append
# 2)  використовуючи метод  map)
li=[]
number=['1','2','3','4','5','7']
for item in number:
    li.append(int(item))
print(li)

