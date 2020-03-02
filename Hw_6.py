# #Task_1(Return an array, where the first element is the count of positives numbers and the second element is sum of
# #  negative numbers. If the input array is empty or null, return an empty array.)

def count_positives_sum_negatives(arr):
    sum_negative=0
    count_posytyve=0
    if arr == []:
        return []
    else:
        for i in range(len(arr)):
            if arr[i]>0:
                count_posytyve+=1
            elif arr[i]<0:
                
                sum_negative+=arr[i]
        return([sum_negative,count_posytyve])

print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))

#Task_2(In this kata you will create a function that takes in a list and returns a list with the reverse order.)
def reverse_list(l):
   
    return(l[::-1])

print(reverse_list([1,2,3,4]))

#Task_3(If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.)

def solution(number):
    sum=0
    for i in range(number):
        if i%3==0 or i%5==0:
            sum+=i
            
    return sum

print(solution(10))
        

