Words - Maximum Consonants
Words - Maximum Consonants: The program must accept a string S containing multiple words as the input. The program must print the words in S till the word that has the maximum number of consonants. If two or more words have the same maximum number of consonants, the program must print till the last occurring word among those words.
Boundary Condition(s):
3 <= Length of S  <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains the word(s) in S as per the given conditions.
Example Input/Output 1:
Input:
Hi bob@123, your transaction is successful. Thank You.
Output:
Hi bob@123, your transaction is successful.
Explanation:
The number of consonants in the word Hi is 1.
The number of consonants in the word bob@123, is 2.
The number of consonants in the word your is 2.
The number of consonants in the word transaction is 7.
The number of consonants in the word is is 1.
The number of consonants in the word successful. is 7.
The number of consonants in the word Thank is 4.
The number of consonants in the word You. is 1.
Here the maximum number of consonants is 7.
The words "transaction" and "successful." have the same maximum number of consonants, so the words till the last occurring word "successful." are printed as the output.
Hence the output is
Hi bob@123, your transaction is successful.
Example Input/Output 2:
Input:
FGHJKfghjkl ab#1990 aeiou aaaaabcdfgheeeeee lol
Output:
FGHJKfghjkl
s=input().strip().split();m=-1
for i in range(len(s)-1,-1,-1):
    c=0
    for j in s[i]:
        if j not in 'aeiouAEIOU' and j.isalpha():c+=1 
    if c>m:m=c;d=i 
print(*s[:d+1])
