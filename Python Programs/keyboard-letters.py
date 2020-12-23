Keyboard Letters
Given an  English word,  write an algorithm and the subsequent Python code to check if the given word can be typed using just a single row of the keyboard. (e.g. POTTER, EQUITY). Print ‘Yes’ if the letters of the word are from a single row and print ‘No’ otherwise.
Input format:
A word
Output format:
Print ‘Yes’ if all letters of the word are from same row in a keyboard

Input for the problem:
A word
Processing:
We use conditional statements to check which line the letters of the words are from.
Output :
‘Yes’ if all letters of the word are from same row in a keyboard
s=input()
s=s.upper()
q="QWERTYUIOP"
a="ASDFGHJKL"
z="ZXCVBNM"
flag=0
for ltr in s:
    if ltr not in q:
        flag=1
        break
if(flag==1):
    for ltr in s:
        if ltr not in a:
            flag=2
            break
if(flag==2):
    for ltr in s:
        if ltr not in z:
            flag=3
            break
if flag!=3:
    print("Yes")
else:
    print("No")
