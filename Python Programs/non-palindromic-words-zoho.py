Non Palindromic Words [ZOHO]
Non Palindromic Words: A string with one or more words is passed as the input. The program must print only the words which are not palindromes. Print -1 if all the words in the string are palindromes.
Boundary Condition(s):
1 <= N, Length of S <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains the words which are not palindromes separated by a space.
Example Input/Output 1:
Input:
Today madam came to the class
Output:
Today came to the class
Example Input/Output 2:
Input:
malayalam ere
Output:
-1
s=input().split()
k=0
for i in s:
    if i!=i[::-1]:
        k=1
        print(i,end=' ')
if k==0:print(-1)
