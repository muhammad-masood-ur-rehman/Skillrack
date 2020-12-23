String Word Counter
Given a string S as input which consists of multiple words separated by a space, the program must print the count C of the words which are repeated exactly N times. The comparison of the words is case sensitive.
Input Format:
The first line contains S
The second line contains N
Output Format:
The first line contains C
Boundary Conditions:
1 <= Length of S <= 10000
Example Input/Output 1:
Input:
one two three four three two five
1
Output:
3
Explanation:
The words which are repeated only once are one, four and five. Hence the count is 3.
Example Input/Output 2:
Input:
one two three four three two five one five Three
2
Output:
4
a=input().split()
n=int(input())
l=[x for x in a if a.count(x)==n]
print(len(set(l)))
