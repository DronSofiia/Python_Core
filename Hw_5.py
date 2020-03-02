# #Task_1(Given two ordered pairs calculate the distance between them. 
# # Round to two decimal places. This should be easy to do in 0(1) timing.)
from math import sqrt
def distance(x1, y1, x2, y2):
    return(round(sqrt((x2-x1)**2+(y2-y1)**2),2))
print(distance(1,1,0,0))


# #Task_2(Create a robot that will always win the game. Your robot will always go first. 
# # The function should take an integer and returns 1, 2, or 3.)

def make_move(sticks):
    return sticks % 4

print(make_move(21))

# #Task_3(Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing.
# #  String should be capitalized and properly spaced. Using re and string is not allowed.)

def filter_words(st):
    # st1=st[0].upper()
    # st2=st[1:].lower()
    st=st[0].upper()+st[1:].lower()
    return(st)

print(filter_words("HELLO woRd"))

#Task_4(Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished For Loop!)
def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i+=1
        
    return res

print(create_array(10))
