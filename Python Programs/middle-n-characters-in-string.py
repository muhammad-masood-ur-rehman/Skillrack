Middle N Characters in String
Middle N Characters in String: Given a String S and an integer N as input, the program must print the N characters present in the middle of the string. If the length of S is even and N is odd print the character from the second half of the string as the output.
Boundary Condition(s):
3 <= Length of S <= 100
3 <= N <= 100
Input Format:
The first line contains the String S.
The second line contains the value of N.
Output Format:
The first line contains the N characters present in the middle of the string.
Example Input/Output 1:
Input:
hello
3
Output:
ell
Explanation:
There are 5 characters in the given string -> h e l l o
The middle 3 characters are e l l
Hence the output is ell
Example Input/Output 2:
Input:
whatsapp
5
Output:
atsap 
Explanation:
There are 8 characters in the given string -> w h a t s a p p
The middle 5 characters are a t s a p
Hence the output is atsap
s=input().strip()
n=int(input())
d=len(s)-n
if n:
    l=s[(d+1)//2:len(s)-(d//2)]
    print(l)
