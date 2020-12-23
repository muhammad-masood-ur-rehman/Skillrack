Count of UpperCase Letters
A string S is passed as the input. The program must print the number of upper case letters in the string S. Input Format: The first line denotes the value of S.Output Format: The first line contains the count of upper case letters in S.
Boundary Conditions: Length of S is from 3 to 100.
Example Input/Output 1:
Input: ViCtorY
Output: 3
Example Input/Output 2:
Input: zookeeper
Output: 0
s=input()

print(sum(1 for i in s if i.isupper()))
