Find Random Character
Find Random Character: The program must accept a string S representing the name of a boy as the input. His friend shuffles the characters in the name S and inserts a random character at a random position. The modified name M is also passed as the input to the program. The program must find the randomly inserted character in M and print it as the output.
Note: Length of M = (Length of S) + 1.
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line contains S.
The second line contains M.
Output Format:
The first line contains the randomly inserted character in M.
Example Input/Output 1:
Input:
nelson
oneplsn
Output:
p
Explanation:
Here S = nelson and M = oneplsn.
The randomly inserted character in M is p.
So p is printed as the output.
Example Input/Output 2:
Input:
AAaa
AaAaA
Output:
A
string1=sorted(input().strip())
string2=sorted(input().strip())

for ele in range(len(string1)):
    if string1[ele]!=string2[ele]:
        print(string2[ele])
        exit()

print(string2[-1])
