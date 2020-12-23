Characters at Positions of Multiples of X
Characters at Positions of Multiples of X: Given a string S and an integer X as input, the program must print the characters at the positions of multiples of X until the last character is printed. If the multiple of X goes beyond the last character, then the string characters should be navigated in a cyclic manner till the last character is printed.
Boundary Condition(s):
1 <= length of string <= 100
1 <= X <= 100
Input Format:
The first line contains the string S and the value of X separated by space(s).
Output Format:
The first line contains the characters at the positions of multiples of X until the last character of the string S.
Example Input/Output 1:
Input:
denomination 8
Output:
aon
Explanation:
The character at the first multiple of 8 is 'a'.
Since the second multiple of 8 is beyond the last character of the string, consider the string in a cyclic manner. Then the character at the second multiple of 8 is 'o'.
Similarly, the character at the third multiple of 8 is 'n' and also it is the last character of the string.
Example Input/Output 2:
Input:
importance 2
Output:
motne
Explanation:
The character at the first multiple of 2 is 'm'.
The character at the second multiple of 2 is 'o'.
The character at the third multiple of 2 is 't'.
The character at the fourth multiple of 2 is 'n'.
The character at the fifth multiple of 2 is 'e' and also it is the last character of the string S.
Python:
a,b=map(str,input().split())
b=int(b)
i,j=1,0
while j!=len(a):
   if i%b==0:
       print(a[j],end='')
       if j==len(a)-1:break
   if j==len(a)-1:
    j=0
   else:j+=1
   i+=1
