Reverse Every Word
The program must accept a string S containing multiple words as the input. The program must reverse every word in the string S. Then the program must print the modified string S as the output.
Input : Friday and Saturday
Output : yadirF dna yadrutaS
Explanation:
After reversing every word in the string Friday and Saturday, the string becomes yadirF dna yadrutaS.
Hence the output is yadirF dna yadrutaS
Here are the various methods and logic.
Python :

# Code by @ Agent Stark

# Code by @ Agent Parker
# Code by @ Agent Hawkeye
s=input().strip()
words=s.split(' ')
for ele in words:
    newword=ele[::-1]
    n=''.join(newword)
    print(n,end=" ")
C :

# Code by @ Agent Marvel

# Code by @ Agent Natasha
