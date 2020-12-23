Distinct Letters
Write an algorithm and the subsequent Python code to check if the given word is good or bad.: e.g. START, GOOD, BETTER are bad: WRONG is good! Make the comparison to be case insensitive.
Input format:
A word
Output format:
Print ‘Good’ if all letters of the word are distinct and print ‘bad’ otherwise

Input for the problem:
A word
Processing:
We loop through the letters of the word and using conditional statements and a flag variable we check whether the letters in the word are distinct or not.
Output:
‘Good’ if all letters of the word are distinct and print ‘bad’ otherwise.
s=input().lower()
cnt=0
for ltr in s:
    for itr in s:
        if itr==ltr:
            cnt=cnt+1
    if cnt>1:
        break
    cnt=0
if cnt==0:
    print("Good")
else:
    print("Bad")
    
