Array Maximum Sum Divisible By N
n array of numbers separated by space will be passed as input. A number N is also passed as input. The program has to print the maximum sum of the numbers in the array which is divisible by N. If there is no such maximum sum of the numbers, the program should print -1 as output.
Input Format: The first line contains the array of numbers separated by space. The second line contains the value of N
Boundary Conditions: The length of the array of numbers will be from 3 to 200.
1 <= N <= 1000
Output Format: The maximum sum of the numbers in the array that is divisible by N.
Example Input/Output 1:
Input:
10 20 40 70
3
Output:
120
Explanation: The maximum sum of numbers that is divisible by 3 is 120 (10+40+70) and hence it is printed as the output.
Example Input/Output 2:
Input:
22 34 54 80 93 41
5
Output:
290
Explanation: The maximum sum of numbers that is divisible by 5 is 290 (22+54+80+93+41) and hence it is printed as the output.
import itertools
a,n,l1=[int(i) for i in input().split()],int(input()),[]
for i in range(1,len(a)):
    l=list(itertools.combinations(a,i))
for i in range(len(l)):
    s=sum(l[i])
    if s%n==0:
        l1.append(s)
if len(l1)!=0:
    print(max(l1))
else:
    print("-1")
