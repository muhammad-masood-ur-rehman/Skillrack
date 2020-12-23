Print Prime Numbers from 2 to N Program In Python
The program must accept an integer N as the input. The program must print all the prime numbers from 2 to N (inclusive of N) as output.
Boundary Condition(s):
2 <= N <= 999999
Input Format:
The first line contains the value of N.
Output Format:
The first line contains all the prime numbers from 2 to N.
Example Input/Output 1:
Input:
11
Output:
2 3 5 7 11 
Example Input/Output 2:
Input:
120
Output:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113
 def prime(n):
    pr=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if pr[p]==True:
            for i in range(p*p,n+1,p):pr[i]=False 
        p+=1
    for p in range(2,n+1):
        if pr[p]:print(p,end=' ')
n=int(input())
prime(n)
