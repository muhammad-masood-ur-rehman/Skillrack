K Integers - Same Ends Program In Python
The program must accept two integers N and K as the input. The program must print the first K integers greater than N which are having the same first and last digits as the output.
Boundary Condition(s):
10 <= N <= 10^7
1 <= K <= 1000
Input Format:
The first line contains N and K separated by a space.
Output Format:
The first line contains K integers separated by a space.
Example Input/Output 1:
Input:
1990 10
Output:
1991 2002 2012 2022 2032 2042 2052 2062 2072 2082
Explanation:
Here N = 1990 and K = 10.
The first 10 integers greater than 1990 and having the same first and last digits are given below.
1991 2002 2012 2022 2032 2042 2052 2062 2072 2082
Example Input/Output 2:
Input:
9999 15
Output:
10001 10011 10021 10031 10041 10051 10061 10071 10081 10091 10101 10111 10121 10131 10141
a,b=map(int,input().split())
c,i=0,a+1
while(c<b):
    if str(i)[0]==str(i)[-1]:
        print(i,end=" ")
        c+=1 
    i+=1
