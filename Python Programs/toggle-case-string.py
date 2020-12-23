Toggle case (String)
Toggle case: Given a String S as input, the program must toggle the case of each alphabet.
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line contains the String S.
Output Format:
The first line contains the String with the case of the alphabets toggled.
Example Input/Output 1:
Input:
HelloGoogle
Output:
hELLOgOOGLE
Example Input/Output 2:
Input:
WelcometoAirIndia
Output:
wELCOMETOaIRiNDIA
n=input().strip()
print(n.swapcase())
