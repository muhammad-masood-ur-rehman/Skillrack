Vowel Expansion
Vowel Expansion: The program must accept a string S as the input. The program must expand the string S by inserting vowels after each vowel in it based on the following conditions.
- If the vowel is a or A, then the program must insert one more a or A next to it.
- If the vowel is e or E, then the program must insert two more e or E next to it.
- If the vowel is i or I, then the program must insert three more i or I next to it.
- If the vowel is o or O, then the program must insert four more o or O next to it.
- If the vowel is u or U, then the program must insert five more u or U next to it.
Finally, the program must print the modified string S as the output.
Note: The case of the vowels to be inserted must be the same as the case of the vowels present in the string S.
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line contains S.
Output Format:
The first line contains the modified string S.
Example Input/Output 1:
Input:
Argument
Output:
AArguuuuuumeeent
Explanation:
There are 3 vowels in the given string Argument (A, u and e).
The first vowel is A. So one more A is inserted next to it.
Now the string becomes AArgument.
The second vowel is u. So five more u are inserted next to it.
Now the string becomes AArguuuuuument.
The third vowel is e. So two more e are inserted next to it.
Now the string becomes AArguuuuuumeeent.
So AArguuuuuumeeent is printed as the output.
Example Input/Output 2:
Input:
LETUSCrack#123
Output:
LEEETUUUUUUSCraack#123
Example Input/Output 3:
Input:
ABCDEiou
Output:
AABCDEEEiiiiooooouuuuuu
GivenString=input().strip()
List1=[]
for ele in GivenString:
    if  ele in 'aeiouAEIOU' and(ele=='a'or ele=='A'):
        List1.append(ele)
    elif ele in 'aeiouAEIOU' and(ele=='e'or ele=='E'):
        List1.append(ele*2)
    elif ele in 'aeiouAEIOU'and(ele=='I'or ele=='ele'):
        List1.append(ele*3)
    elif ele in 'aeiouAEIOU' and(ele=='o'or ele=='O'):
        List1.append(ele*4)
    elif ele in 'aeiouAEIOU' and(ele=='u'or ele=='U'):
        List1.append(ele*5)
    List1.append(ele)
print(''.join(List1))
