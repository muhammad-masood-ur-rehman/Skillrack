Print Only Alphabets In Python
A string S is passed as the input. S can contain alphabets, numbers and special characters. The program must print only the alphabets in S.
Input Format:
The first line contains S.
Output Format:
The first line contains only the alphabets in S.
Boundary Conditions:
The length of the input string is between 1 to 1000.

Example Input/Output 1:
Input:
abcd_5ef8!xyz
Output:
abcdefxyz
Example Input/Output 2:
Input:
1239_-87
Output:
Explanation:
As there are no alphabets in the input value nothing is printed as output.
s=input().strip()
for i in s:
    if i.isalpha():
        print(i,end="")
