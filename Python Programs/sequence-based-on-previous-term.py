Sequence - Based on Previous Term
The program must accept an integer N as the input. The program must generate a sequence of integers based on the following conditions. 
- The first term of the sequence is always N.
- The current term of the sequence is (previous term / 2) if the previous term is even. Else the current term of the sequence is (previous term * 3) + 1. 
-The sequence always ends with 1. 
Finally. the program must print the integers in the generated sequence as the output. 
Example Input/Output 1: 
Input: 
13
Output: 
13 40 20 10 5 16 8 4 2 1 
Example Input/Output 2: 
Input:
10
Output: 
10 5 16 8 4 2 1
Example Input/Output 3:
Input:
17
Output:
17 52 26 13 40 20 10 5 16 8 4 2 1
n=int(input())
prev=n
print(n,end=' ')
while prev!=1:
    if prev%2==0:
        print(prev//2,end=' ')
        prev=prev//2
    else:
        print(prev*3+1,end=' ')
        prev=prev*3+1
