Reverse & Print Common Characters
Reverse & Print Common Characters: Two string values S1 and S2 are passed as the input. Reverse string S2 and print the letters which are common in a given index. The letters in S1 and S2 will be in lower case.
Input Format: The first line contains S1. The second line contains S2.
Output Format: The first line contains the letters which are common after S2 is reversed.
Boundary Conditions:
2 <= Length of S1 <= 500
2 <= Length of S2 <= 500
Example Input/Output 1:
Input:
energy
genuine
Output:
After reversing S2, we get energy eniuneg The letters common comparing indices are en (in the first two positions)
s1,s2=input(),input()
s2=s2[::-1]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j] and i==j:
            print(s1[i],end="")
