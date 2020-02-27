#Task_1
def warning(pump, speed , gallon):
    if speed*gallon >= pump :
        return True
    else:
        return False

print(warning(50,25,2))

#Task_2
def space_in_car(seats, now, wait):
    if wait+now > seats:
        print("No seats")
    else:
        print(f"Yes {seats-now}")
print(space_in_car(50,25,25))

#Task_3
def play_in_banjo(name):
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
print(play_in_banjo('Roma'))

#Task_4
def bool_type(boolean):
    if boolean:
        return 'yes'
    else:
        return 'no'
print(bool_type("3.14"))

#Task_5
array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]; 
def sheeps_count(sheeps):
    count=0
    for i in sheeps:
        if i == True:
            count=count+1
    print(count)  

print(sheeps_count(array1))  

#Task_6
def correct_tail(body, tail):

    if body[-1] == tail:
        return True
    else:
        return False
   