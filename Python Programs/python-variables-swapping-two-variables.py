Python Variables - Swapping Two Variables
Swapping is the process of exchanging the values of two variables with each other. This can be useful in many operations in computer science. Here, I have written two major methods used by the programmer to swap the values as well as the optimal solution.
Using a temporary variable:
This method uses a temporary variable to store some data. The following code is written with a temporary variable name.
a , b = 100 , 200
print(a,b)
temp = a+b  #a=100 b=200 temp=300
b = a       #a=100 b=200 temp=300
a = temp-b  #a=200 b=100 temp=300
print("After swapping:",a,b)
100 200
After swapping: 200 100
Without using a temporary variable:
The following code swaps the variable without using a temporary variable.
a , b = 100 , 200
print(a,b)
a = a+b  #a=300 b=200
b = a-b  #a=300 b=100
a = a-b  #a=200  b=100
print("After swapping:",a,b)
100 200
After swapping: 100 200
Both the programs gives the same results.
Optimal Solution in Python:
This is a different approach to swap variables using python. In the previous section, we have learned about multiple assignments. We can use the concept of swapping.
a , b = 100 , 200
print(a,b)
a , b = b , a
print("After swapping",a,b)
200 100
