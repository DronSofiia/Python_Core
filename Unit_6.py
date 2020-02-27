#Block_1(Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел)
def arifmetic_mean(first, *args):
    return(first + sum(args)/(1+len(args)))
print(arifmetic_mean(10,8,8))   
        
#Block_2(Написати функцію, яка повертає абсолютне значення числа)
def absolute(x):
    return(abs(x))
print(absolute(-12))

#Block_3
def max(a,b):
    """ Знаходження максимального числа"""
    if(a>b):
        print("maximal a", a)
    elif (a<b):
        print("maximal b", b)
    else:
        print("they are the same")
print(max(11,11))


#Block_4(Написати програму, яка обчислює площу прямокутника, трикутника
#  та кола (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача))
def sq_rectame():
    a=int(input("write a"))
    b=int(input("write b"))
    print(a*b)
def sq_circle():
    r=int(input("write r"))
    PI=3.14
    print(PI*r**2)
def sq_square():
    a=int(input("write a"))
    print(a**2)
variant=input("Write variant: if rectame - 1 , if circle - 2 , if  square - 3 ")
if variant=="1":
    sq_rectame()
elif variant=="2":
    sq_circle()
elif variant=="3":
    sq_square()
else:
    print("noooooo")
    
    
#Block_5( Написати функцію, яка обчислює суму цифр введеного числа)
def sum_number(number):

    number=list(number)
    number=list(map(int,number))

    a=0
    for i in number:
        a+=i
    print(a)
sum_number('125')

#Block_6(Написати програму калькулятор, яка складається з наступних функцій: 
#головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, калькулятор працює доти, поки ми не виберемо дію
#вийти з калькулятора, після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!)
from math import sqrt
def main():
    print("you can + - / * sqrt ")
    action=input("you choise ")
    return action
def add():
    a=int(input("Write a"))
    b=int(input("Write b"))
    print("Sum is",a+b)
def subst():
    a=int(input("Write a"))
    b=int(input("Write b"))
    print("Subst is",a-b)
def mult():
    a=int(input("Write a"))
    b=int(input("Write b"))
    print("Multiplication is ",a*b)
def div():
    a=int(input("Write a"))
    b=int(input("Write b"))
    print("Division is ",a/b)
def korin():
    a=int(input("Write a"))
    print(f"Sqrt {a} is {sqrt(a)}")

result=main()
if result=="+":
    add()
elif result=="-":
    subst()
elif result=="*":
    mult()
elif result=="/":
    div()
elif result=="sqrt":
    korin()
else:
    print("Nooo")
print("thank you")




#Block_7(Рекурсивною функцією вивести числа фібоначі до заданого)
def fibonachi(n,x=1):
    if x>n:return 1
    else:
        print(x+fibonachi(n,x+1))
        return x+fibonachi(n,x+1)
print(fibonachi(20))




# Block_8(Написати програму, яка обчислює дискримінант квадратного рівняння)
from math import sqrt
a=int(input("write coef x^2 \n"))
b=int(input("write coef x \n"))
c=int(input("write c \n"))
D=b**2-4*a*c
if D<0:
    print(" no solution ")
elif D==0:
    print(f"x1_2={-b/(2*a)}")
else:
    print(f"x1={(-b+sqrt(D))/(2*a)}")
    print(f"x1={(-b-sqrt(D))/(2*a)}")
    



