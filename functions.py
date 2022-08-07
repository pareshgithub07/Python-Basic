#built in function

"""a = 8
b = 7                    #The above example is built in function
c = sum((a,b))
print(c)"""

#user defined functions

"""def function1 (a,b):
    c = (a+b)            #This the example of user defined function 
    print(c)
function1(8,7)"""

def function2(a,b):
    """This function is not working with 3 numbers"""
   
    average = (a+b)//2
    return average

   
v= function2(6, 2)
print("The avarage of this two no is", v)
#print(function2.__doc__)
