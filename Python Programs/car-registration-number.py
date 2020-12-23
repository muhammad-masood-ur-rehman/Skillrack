Car Registration Number
The program must accept the registration number N of a car as the input. The program must print the sum of digits in N as the output.
Example Input/Output 1:
Input:
TN-76 AC-1234
Output:
23
Explanation:
The digits in the registration number TN-76 AC-1234 are 7, 6, 1, 2, 3 and 4.
So their sum 23 is printed as the output.
Example Input/Output 2:
Input:
TN-13 AD-9051
Output:
19
Python :


@Agent Stark
num=int(input())
c=0
for ele in num:
    for ele in '1234567890':
         c+=int(ele)
print(c)
C :

@ Agent FALCON
