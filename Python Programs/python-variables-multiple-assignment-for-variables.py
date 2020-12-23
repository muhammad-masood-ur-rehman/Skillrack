Python Variables - Multiple Assignment For Variables
Python allows us to assign values for more than one variable in a single line. The variables can be separated using commas. The one-liners for multiple assignments has lots of benefits. It can be used for assigning multiple values for multiple variables or multiple values for a single variable name. 
Let us take a problem statement in which we have to assign the values 100 and 200 to the variables a and b. The usual code will be like the following.
a = 100
b = 200
print(a,b)
100 200
Values equal to Variables:
When the variables and values of multiple assignments are equal, each value will be stored in all the variables.
a, b = 100, 200
print(a,b)
100 200
Both the programs gives the same results. This is the benefit of using one line value assignments.
Values greater than Variables
Let us try to increase the number of values in the previous program. The multiple values can be assigned to a single variable. While assigning more than one value to a variable we must use an asterisk before the variable name.
a , *b = 100, 200, 300
print(a)
print(b)
100
[200, 300]
One Value to Multiple Variables:
We can assign a value to more than one variable. Each variable will be separated using an equal to symbol.
a = b = c = 100
print(a,b,c)
100 100 100
Assign different types to variables:
We can assign different types to the variables . Each variable will be separated using an comma(,) symbol.
a, b= "Letuscrack",100
print(a)
print(b)
Letuscrack
100
