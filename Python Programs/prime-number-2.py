Prime Number
An integer value N is passed as the input. The program must print YES if N is prime number. Else the program must print NO.
Input Format:
The first line denotes the value of N.
Output Format:
YES or NO based on if N is a prime number or not. (The OUTPUT is CASE SENSITIVE).
Boundary Conditions:
2 <= N <= 9999999
Example Input/Output 1:
Input:
19
Output:
YES
Example Input/Output 2:
Input:
189210
Output:
NO
n=int(input())
if n>1:
    for i in range(1,n):
        if n%i==0:
            print("NO")
            break
    else:
        print("YES")
