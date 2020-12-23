Three Alphabet Series
Three Alphabet Series: A special alphabet series can be formed by three alphabets A, B and C. An integer K is given as the input to the program. The program must print the count all possible alphabet series of length K as the output. The series must be formed by the following rules.
The alphabet A can be followed by either B or C.
The alphabet B can be followed by either A or C.
The alphabet C can be followed by only B.
Boundary Condition(s):
1 <= K <= 40
Input Format:
The first line contains K.
Output Format:
The first line contains the count of all possible series of length K.
Example Input/Output 1:
Input:
3
Output:
8
Explanation:
The series with length 3 are 
ABA
ABC
ACB
BAB
BAC
BCB
CBA
CBC
Example Input/Output 2:
Input:
5
Output:
21
a=int(input())
x=y=1
for i in range(a+1):
    next=x+y
    x=y
    y=next
print(next)
