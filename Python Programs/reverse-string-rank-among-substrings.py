Reverse String Rank among SubStrings
A string S is passed as the input. The program must generate the set (all unique) of all the substrings of S in the reverse order and then sort that set lexicographically. Now the program must print the rank of the reverse of the string S in the new set formed.
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
7
Explanation:
Reverse of eren is nere
Lexicograhically sorted set of unique substrings of nere is
e
er
ere
n
ne
ner
nere
r
re
In this nere appears in the 7th position.
n=input().strip()[::-1]
r=[n[i:j] for i in range(len(n)) for j in range(i+1,len(n)+1)]
k=sorted(set(r))
print(k.index(n)+1)
