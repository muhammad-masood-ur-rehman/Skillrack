Print except multiples of N
Two numbers A and B are passed as input. A number N is also passed as the input. The program must print the numbers from A to B (inclusive of A and B) which are not divisible by N.
Input Format:
The first line denotes the value of A.
The second line denotes the value of B.
The third line denotes the value of N.
Output Format:
The numbers from A to B (inclusive of A and B) which are not divisible by N, each separated by a space.
Boundary Conditions:
1 <= A <= 9999999
A <  B <= 9999999
1 <= N <= 9999
Example Input/Output 1:
Input:
3
20
5
Output:
3 4 6 7 8 9 11 12 13 14 16 17 18 19
Explanation:
The numbers 5 10 15 20 are left out as they are divisible by 5.
a=int(input())
b=int(input())
n=int(input())
for i in range(a,b+1):
    if (i%n==0):
        continue
    print(i,end=" ")
