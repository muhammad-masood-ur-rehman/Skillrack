Increment & Decrement Triangle Pattern
Increment & Decrement Triangle Pattern: The program must accept an Integer N as the input. The program must print hyphens and integers In N+1 lines based on the following conditions.
In the 1st line, the program must print N hyphens and an integer (0).
In the 2nd line, the program must print N-1 hyphens and three Integers (N, 0, N).
In the 3rd line, the program must print N-2 hyphens and five Integers (N-1, N, 0, N, N-1).
In the 4th line, the program must print N-3 hyphens and seven Integers (N-2, N-1, N, 0, N, N-1, N-2).
Similarly, the program must print the remaining lines as the output.

Input Format:
The first line contains N.

Output Format: 
The first N+1 lines contain hyphens and integers based on the given conditions. 

Example Input/Output 1:
Input:
5
Output: 
-----0
----505
---45054
--3450543
-234505432
12345054321


Example Input/Output 2: 
Input: 
9
Output:
---------0
--------909
-------89098
------7890987
-----678909876
----56789098765
---4567890987654
--345678909876543
-23456789098765432
1234567890987654321
n=int(input())
print("-"*n,0,sep="")
for i in range(n,0,-1):
    print("-"*(i-1),end="")
    for j in range(i,n+1):
        print(j,end="")
    print(0,end="")
    for j in range(n,i-1,-1):
        print(j,end="")
    print() 
