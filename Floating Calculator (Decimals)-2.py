#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('a for Addition')
print('b for Subtraction')
print('c for Multiplication')
print('d for Division')

operation = input("Please Type Corresponding Letter for Operation")

#prompt 
num_1 = float(input("Enter first number : "))
num_2 = float(input("Enter second number : "))
    
if operation == "a":
    print(num_1, "+", num_2, "=", (num_1+num_2))
    
elif operation == "b":
    print(num_1, "-", num_2, "=", (num_1-num_2))

elif operation == "c":
    print(num_1, "*", num_2, "=", (num_1*num_2))
    
elif operation == "d":
    print(num_1, "/", num_2, "=", (num_1/num_2))


# In[ ]:




