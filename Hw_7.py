#Task_1(Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0.)
def summation(num):
    sum = 0
    for i in range(num+1):
        sum += i
        
    return sum

print(summation(8))

#Task_2()
animals = [ 'dog', 'cat', 'elephant' ]
def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list
print(list_animals(animals))

#Task_3(Given a string, you have to return a string in which each character (case-sensitive) is repeated once.)

def double_char(s):
    new_string=''
    for i in range(len(s)):
        new_string+=s[i]+s[i]
    return new_string

print(double_char("helo"))
