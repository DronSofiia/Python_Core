# #Task_1(Is the string uppercase?)
def is_uppercase(inp):
    return inp.isupper()

print(is_uppercase("HFJLKFG"))

# #Task_2()
def sorter(textbooks):
    return sorted(textbooks,key=str.lower)

print(sorted(['Algebra', 'History', 'Geometry', 'English']))

#Task_3()
def shorten_to_date(long_date):
    return long_date.split(',')[0]

print(shorten_to_date("Tuesday May 29, 8pm"))