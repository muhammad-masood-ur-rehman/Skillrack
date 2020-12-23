Convert KM/HR to M/S
Speed S of a car is passed as input. It is in kilometers per hour. Write a program to convert the speed from kilometer per hour to meter per second.
Boundary Condition:
0 < S < 4500
Input:
Speed of a car is passed as input.
Output:
Speed is converted into meter per second and it is printed in a new line. Limit the accuracy of the floating point to two places without rounding up.
Example Input/Output 1:
Input:
230
Output:
63.88
Explanation:
Speed of the car in meter per second = 230*1000/3600 = 63.88
a=int(input())
b=str(a*5/18)
k=b.index('.')
print(b[:k+3]) if len(b)-1-k>=2 else print (b+'0')
