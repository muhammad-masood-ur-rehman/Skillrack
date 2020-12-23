Odd-Even Values Difference
Given a value of N positive integers, the program must print the difference between the sum of odd integers and the sum of even integers.
Input Format:
The first line will contain the value of N
The second line will contain the N positive integers separated by a space.
Output Format:
The first line will contain the integer value denoting the difference.
Constraints:
2 <= N <= 25
Example Input/Output 1:
Input:
5
10 11 20 33 1
Output:
15
Explanation:
The sum of odd integers is = 11+33+1 = 45.
The sum of even integers is = 10+20 = 30.
Hence the difference 45-30 = 15 is printed as the output.

Example Input/Output 2:
Input:
6
2 24 7 35 5 30
Output:
-9
Explanation:
The sum of odd integers is = 7+35+5 = 47
The sum of even integers is = 2+24+30 = 56
Hence the difference 47-56 = -9 is printed as the output.
n=int(input())
li=list(map(int,input().split()))
a,b=0,0
for i in li:
    if(i%2==0):
        a+=i 
    else:
        b+=i 
print(b-a)
