#Block_1(Напишіть програму, яка пропонує користувачу ввести ціле число і
#  визначає чи це число парне чи непарне, чи введені дані коректні.)
def even_odd_number(number):
    try:
        if number%2==0:
            print("Even")
        else:
            print('Odd')
    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
even_odd_number("jkjg")
even_odd_number([10,11])
even_odd_number(10)
even_odd_number(-10)

#Block_2(Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить 
# повідомлення про те чи вік є парним чи непарним числом. Необхідно передбачити можливість введення 
# від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію.
#  Головний код має викликати функцію, яка обробляє введену інформацію)


def odl_number(number):
    try:
        if number<0:
            raise ValueError("That not positive number")
        elif number%2==0:
            print("Even")
        else:
            print('Odd')
    except ValueError as e:
        print(e)  
    except TypeError:
        print("TypeError")  
odl_number(-10)


Block_3(Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, 
передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки
 інших виняткових ситуацій. Використати блоки else та finaly)

def fractoin(a,b):
    try:
        print(f"Fraction{a/b}")
    except ZeroDivisionError:
        print("ZerroError")
    except TypeError:
        print('TypeError')
    except ValueError:
        print('ValueError')
    else:
        print("Yes?")
    finally:
        print("Good job")

fractoin(10,0)
fractoin(10,"jdfkjd")
fractoin(10,11)


#Block_4(Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, який відповідає
#  цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) .  введення чисел від 8 і більше, 
# а також випадки введення не числових даних.)

day = ['Monday', "Tuesday", "Wednesday", "Thursday" , "Friday", "Saturday"," Sunday"]
def day_week(number):
    try:
        if number>7 or number<1:
            raise ValueError("That number is not corect ")
        
        print(day[number-1])
    except TypeError:
        print("TypeError")
    except ValueError as e:
        print(e)
day_week(0)


#Block_4a(Застосовуючи dict)
day={1:'Monday', 2:"Tuesday", 3:"Wednesday", 4:"Thursday" , 5:"Friday", 6:"Saturday",7:" Sunday"}
def day_week(number):
    try:
        if number>7 or number<1:
            raise ValueError("This number is not corect ")
        print(day[number])
    except NameError:
        print("NameError")
    except TypeError:
        print("TypeError")
    except ValueError as e:
        print(e)
    except SyntaxError:  
        print("SyntaxError")
    except:
        print("No!No!No!")
day_week(10)
