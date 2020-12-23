String - Vowels Position Sum
Accept a String S as the input. The program must print the sum of the positions of the vowels in S. If the string does not contain any vowels then print -1.

Boundary Condition(s):
2 <= Length of the string S <= 100

Input Format:
The first line contains the string S.

Output Format:
The first line contains the sum of the positions of the vowels in S.
Example Input/Output 1:
Input:
nose
Output:
6
Explanation:
The vowels in the string are o and e. The position of o is 2 and the position of e is 4. The sum of the positions = 2 + 4 = 6.
                                                                          
Example Input/Output 2:
Input:
xyz
Output:
-1
s=input().strip()
k=0
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        k+=i+1 

if k!=0:
    print(k)
else:
    print("-1")
