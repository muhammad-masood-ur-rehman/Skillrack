Print till First Non-Alphabet
Print till First Non-Alphabet: The program must print the given input String S till the first non alphabet character in the input String S.
           
Boundary Condition(s):
1 <= Length of S <= 1000
Input Format:
The first line contains the String S.
Output Format:
The first line contains the String  till the first non alphabet character.
Example Input/Output 1:
Input:
IamSorry!forwhatidid
Output:
IamSorry
Explanation :
IamSorry is printed until special character '!' occurs.
Example Input/Output 2:
Input:
mail.google.com
Output:
mail
Explanation :
mail is printed until special character '.' occurs.
s=input().strip()
for i in s:
    if i.isalpha():
        print(i,end="")
    else:
        break
