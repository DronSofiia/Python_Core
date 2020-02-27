#Block_1(Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел 
від 1 до 100 і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач 
і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. 
Гра має тривати до моменту поки користувач
 не введе число, яке загадане програмою, тоді друкує повідомлення привітання. )
import random

number=random.randint(1,101)
k=0
#print(number)
while True:

    vercia_number=int(input('Guess the intended number'))
    if(number==vercia_number):
        print("you’re right")
        break
    elif (number>vercia_number):
        print("more number")
    else:
        print("fewer number")


#Block_2(Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
#(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).)
from math import pi,pow
metod=input("write metod 1 - примокутник 2 - трикутника  3- кола")
def square_1():
    a=int(input("write a"))
    b=int(input("write b"))
    square=a*b
    print("Square",square)
def square_2():
    h=int(input("write h"))
    a=int(input("write a"))
    square=a*h*0.5
    print("Square",square)
def square_3():
    r=int(input("write r"))
    square=pow(r,2)*pi
    print("Square",square)

if(metod=='1'):
    square_1()
elif (metod=='2'):
    square_2()
elif (metod=='3'):
    square_3()
else:
    print("METOD")
    
#cmd: pip install pyowm
import pyowm
city=input("What city you are interested:")
owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')    # You MUST provide a valid API key
# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
# Search for current weather in the city

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
print("In this city "+ w.get_detailed_status())


