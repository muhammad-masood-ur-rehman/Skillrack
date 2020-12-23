Password Check
iven a word, check if it is a valid password or not.  A password is said to be valid if it satisfies the following conditions:
i) Should begin with a letter
ii) Should contain at least one digit and one special character
iii) Length of the password should be atleast 8
Print ‘Valid’ if the given word satisfies the above three conditions  and print ‘Invalid’ otherwise.
Input format:
A word
Output format:
Print ‘Valid’ if the given word satisfies the above three conditions  and print ‘Invalid’ otherwise.

Input for the problem:
A word
Processing:
Using conditional statements, we check whether the password is valid or invalid.
Output :
Valid/Invalid
s=input()
cnt=0
if s[0].isalpha():
    cnt=cnt+1
if len(s)>=8:
    cnt=cnt+1
for ltr in s:
    if ltr.isdigit():
        cnt=cnt+1
        break
for ltr in s:
    if not ltr.isdigit() and not ltr.isalpha():
        cnt=cnt+1
        break
if cnt==4:
    print("Valid")
else:
    print("Invalid")
