Python Program to Print All Vowels
Accept a string S as the input and print all the vowels in S as the output. If there is no vowel in S then the program must print -1 as the output.
Boundary Condition(s):
1 <= Length of S <= 100
Example Input/Output 1:
Input:
letuscrack
Output:
eua
Example Input/Output 2:
Input:
Sky
Output:
-1
inpStr = input().strip()
vowels = "aeiouAEIOU"
printed = False
for ch in inpStr:
    if ch in vowels:
        print(ch, end="")
        printed = True
if not printed:
    print("-1")
