#Task_1
Py_zen="""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
print("Word count 'better'", Py_zen.find("better"), "/// Word count 'never'", 
       Py_zen.find("never"),"/// Word count 'is' " , Py_zen.find("is"))
print("Uppercase", Py_zen.upper())
print("Replece 'i' on '&' ", Py_zen.replace("i","&"))


#Task_2
number='1645'
number=list(number)
number=list(map(int,number))
a=1
for i in number:
    a*=i
print("Multiplication",a)
print("Sort by list",number.sort())
print("Reversed ", number.reverse())

number='1645'
number=list(number)
number=list(map(int,number))
a=1
for i in number:
    a*=i
print("Multiplication",a)
number.sort()
print("Sort by list",number)
number.sort(reverse=True)
print("Reversed ", number)









