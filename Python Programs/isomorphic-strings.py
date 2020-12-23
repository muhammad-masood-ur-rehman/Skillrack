Isomorphic Strings
Given two strings S1 and S2, the program must print if they are isomorphic or not.
Two strings are isomorphic if the characters in S1 can be replaced to get S2 based on the conditions given below.
- All occurrences of a character must be replaced with another character while preserving the order of characters.
- No two characters can map to the same character but a character can map to itself.
Input Format:
The first line contains S1
The second line contains S2
Output Format:
The first line contains YES or NO indicating if S1 and S2 are isomorphic or not.
Boundary Conditions:
1 <= Length of S1 and S2 <= 1000
Example Input/Output 1:
Input:
fill
bell
Output:
YES
Example Input/Output 2:
Input:
paper
title
Output:
YES

Example Input/Output 3:
Input:
pen
egg
Output:
NO
a = input().strip()
b = input().strip()
x = {}; y = {}
def is_isomorphic(a, b):
    if len(a) != len(b):
        return False
    else:
        for i, v in enumerate(a):
            if v in x and x[v] != b[i]:
                return False
            else:
                x[v] = b[i]
            if b[i] in y and y[b[i]] != v:
                return False
            else:
                y[b[i]] = v
        return True

if (is_isomorphic(a, b)):
    print("YES")
else:
    print("NO")
