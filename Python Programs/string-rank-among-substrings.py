String Rank among SubStrings
A string S is passed as the input. The program must generate the set (all unique) of all the substrings of S and then sort that set lexicographically. Now the program must print the rank of the string S in the new set formed.
Note:
- String S contains only lowercase English letters.
- Time complexity matters, optimize your algorithm
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line contains S.
Output Format:
The first line contains the integer value denoting the rank.
Example Input/Output 1:
Input:
eren
Output:
5
Explanation:
Lexicograhically sorted set of unique substrings of S is
e
en
er
ere
eren
n
r
re
ren
In this eren appears in the 5th position.
n=input().strip()
r=[n[i:j] for i in range(len(n)) for j in range(i+1,len(n)+1)]
k=sorted(set(r))
print(k.index(n)+1)
