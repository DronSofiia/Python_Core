#Block_1(Створити список цілих чисел, які вводяться 
        з терміналу та визначити серед них максимальне та мінімальне число.)
a=int(input("How many elements"))
list=[]
for i in range(a):
    list.append(int(input("Write element")))
max = list[0]
min = list[0]
for i in range(a):
    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]
print("max", max )
print("min", min)
print(list)  

#Block_2(В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.)
list=[]
list_parni=[]
list_neparni_tri=[]
list_inshi=[]
a=0
for i in range(10):
    a=a+1
    list.append(a)
for i in list:
    if i % 2 == 0:
        list_parni.append(i)
    elif i%3==0:
        list_neparni_tri.append(i)
    else:
        list_inshi.append(i)
print("Парні",list_parni)
print("Непарні на три ",list_neparni_tri)
print("Ті,що лишились",list_inshi)


#Block_3(Обчислення факторіалу)
a=int(input("write number"))
list=[]
l=1
for i in range(1,a+1):
    list.append(i)
for i in list:
    l=i*l
print("factorial =", l)

#Block_4(Написати скрипт, який перевіряє логін , якщо він вірний , то привітайте користувача )
enter=input("enter login ")
login='login'
while enter==login:
    print("hello")
    break
#Block_5(Написати програму, яка зчитує число , поки не зустріне відємне, нуль проходить)

i=1
while i>=0:
    i=int(input("Enter number"))
print("The end")


#Block_6(На ввід подається число елементів, самі елементи і якщо зустрічається мінусові = break)

count_element=int(input("Write count"))
for i in range(count_element):
    element=int(input("Enter elements"))
    if element<0:
        break
print("The end")

#Block_7(Знайти прості числа від 10 до 30 , а всі решту подати у вигляді ....)
lst = []
k = 0
for i in range(10, 30):

    for j in range(2, i):
        
        if i % j == 0:
            k = k + 1
    
    if k == 0:
        lst.append(i)
    else:
        k = 0

print(lst)


            
         
        




