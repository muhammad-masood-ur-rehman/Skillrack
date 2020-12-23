Find the oldest age in the family
A family consists of N members. Their ages are passed as input separated by a space. Write a program to find the age of the oldest member in the family.
Boundary Conditon:
All the ages must be between 0 and 110.
Input:
N numbers are passed as input separated by one or more spaces.
Output:
Print the age of the oldest member in the family.
Example Input/Output :
Input:
10 78 56 87 32
Output:
87
print(max(sorted(list(map(int,input().split())))[::-1]))
