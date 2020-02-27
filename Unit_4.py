#Block_1(Написати скрипт, який з двох введених чисел вихначить, яке більше, а яке менше)
print("write a:")
a=int(input())
print("write b:")
b=int(input())
if a<b:
    print(b,">", a)
else:
    print(a,">",b)


#Block_2(Перевірка на парність/непарність)
print("write a:")
a=int(input())
if a%2 == 0:
    print("even")
else:
    print("odd")

#Block_3(Обчислити факторіал числа)
print("write a:")
a=int(input())
factorial=1
for i in range(1,a+1):
    factorial=factorial*i
print(factorial)

#Block_4a(Роздрукувати всі парні числа за 100 використовуючи цикл while)
a=0
while a<100:
    if a%2 == 0:
        print(a)
    a=a+1

 #Block_4b(Роздрукувати всі парні числа за 100 використовуючи цикл for)
for i in  range(0,100,2):
    print(i)

#Block_5a(Роздрукувати всі непарні числа використовуючи continue)
for i in  range(0,100):
    if i%2 == 0:
        continue
    print(i)

#Block_5b(Роздрукувати всі непарні числа невикористовуючи continue)
for i in  range(0,100):
    if i%2 == 1:
        print(i)

#Block_6(Перевірити чи список містить парні числа)
spysok = [8,1,4,6]
isOdd=True
for i in spysok:
    if i%2 != 0:
        isOdd=False
        break
if isOdd:
    print("odd")
else:
    print("no odd")


#Block_7( Створити список, який містить елементи цілочисельного типу, 
      # потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. )
spysok='1058'
spysok=list(spysok)
new=[]
for i in spysok:
    new.append(float(i))
print(new)

#Block_8
n=int(input('Write n'))
a=0
fibonachi=[1,1]
for i in range(2,n):
    fibonachi.append(fibonachi[i-1]+fibonachi[i-2])
    if fibonachi[i]>=n:
        del fibonachi[i]
        break
print(fibonachi)

#Block_9
spysok=['maybe','it','does','not']
for i in spysok:
    print(i)
    print(type(spysok[0]))


