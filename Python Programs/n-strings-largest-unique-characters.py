N Strings - Largest Unique Characters
N string values are passed as input to the program. The output is the string which has the largest count of unique characters. If multiple strings have the same largest count of unique characters, print the last occurring string.
Input Format:
The first line contains N.
Next N lines contain the N string values.
Output Format:
The first line contains the string value which has the largest count of unique characters.
Boundary Conditions:
2 <= N <= 1000
1 <= Length of a string value S(i) <= 10^5
Example Input/Output 1:
Input:
3
aaaaaaaaaa
abcdwjdkjwjddcbakd
abcdefghi
Output:
abcdefghi
N = int(input())
List = []
for i in range(N):
    List.append(input().strip())
nList = list(List)
for i in range(N):
    nList[i] = "".join(list(set(list(List[i]))))
 
cList = []
for i in range(N):
    cList.append(len(nList[i]))
 
for i in range(N):
    if cList[N-1-i] == max(cList):
        print(List[N-i-1])
        break
