#Task_1(We need a function that can transform a number into a string)
def number_to_string(num):
    return str(num)


#Task_2(You need to write a function that 
# reverses the words in a given string. A word can also fit an empty string)
def reverses_string(line):
    new_line=line.split(" ")
    for i in range(int(len(new_line)/2)):
        new_line[i],new_line[len(new_line)-i-1]=new_line[len(new_line)-i-1],new_line[i]
    return new_line

print(reverses_string("hello word my sun"))


#Task_3(Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly 
# different. She added a special case to her function, but she made a mistake.)
def message(name):
    if name=='Johnny':
        print("Hello, my love")
    else:
        print("Hello, my friends")
message(input("Write your name "))


