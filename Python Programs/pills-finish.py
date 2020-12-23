Pills Finish
Funda has got flu. Her doctor prescribed her 'x' number of 20mg pills, and told her to take a pill every 'y' hours starting from ‘s’ a.m to ‘e’ p.m. Write an algorithm and a Python code to find out,  in how many days Funda will consume 'x' pills. For example, if 'x' is thirty, 'y' is four, ‘s’ is 9 am and ‘e’ is 10 pm then approximately the tablets will be consumed in 8 days. Use ceil function of math module to round the number of days. Time for start and finish of tablet can be read as an integer. Write appropriate functions for accomplishing the task.
Input Format: First line contains the value of 'x', number of pills
Next line contains the value of 'y', number of hours
Next line contains the value of ‘s’
Next line contains the value of ‘e’
Output Format:
Approximate number of days to consume tablets, ceil the value got
Input for the problem:
First line contains the value of 'x', number of pills
Next line contains the value of 'y', number of hours
Next line contains the value of ‘s’
Next line contains the value of ‘e’
Output for the problem:
Approximate number of days to consume tablets, ceil the value got
from math import ceil
x,y = int(input()),int(input())
s,e = int(input()),int(input())
time = e-s + 12
pills_per_day = 0
for i in range(0,time,y):
    pills_per_day+=1
no_of_days = ceil(x/pills_per_day)
print(no_of_days)
