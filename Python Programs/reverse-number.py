Reverse Number
Number N is passed as the input. The program must reverse the number and print the reversed number as the output.
Input Format:
The first line denotes the value of N.
Output Format:
The reversed number.
Boundary Conditions:
1 <= N <= 99999999
Example Input/Output 1:
Input:
1234
Output:
4321
Example Input/Output 2:
Input:
6500
Output:
56
n=int(input())
r=0
while(n>0):
    r=r*10+n%10 
    n=n//10
print(r)
