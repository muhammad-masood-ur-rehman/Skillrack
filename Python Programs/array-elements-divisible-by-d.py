Array Elements-Divisible by D
An array of N positive integers are passed as input. D which is a positive integer is also passed as the input. The program must print the elements in the array which are divisible by D. 
Input Format: 
The first line contains the value of N. 
The second line contains the N values, each separated by a space. 
The third line contains the value of D. 
Output Format: 
The first line contains the elements among the array which are divisible by D, with each value separated by a space. 
Boundary Conditions: 2 <= N <= 10000 1 <= D <= 9999 
Example Input/Output 1: 
Input: 
6 
10 20 30 40 50 60 
4 
Output: 20 40 60
num=int(input())
arr=list(map(int,input().split()))
d=int(input())
for ele in arr:
    if ele%d==0:
        print(ele,end=" ")
