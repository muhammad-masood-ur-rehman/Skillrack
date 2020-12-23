All Digits - Pairs Count
The program must accept N integers as the input. The program must print the number of pairs X where the concatenation of the two integers in the pair consists of all the digits from 0 to 9 in any order at least once.
Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^8
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains X.
Example Input/Output 1:
Input:
6
38479 74180 967132 1584604 726510 6512160
Output:
3
Explanation:
The 3 possible pairs are given below.
(38479, 726510) -> 38479726510
(38479, 6512160) -> 384796512160
(967132, 1584604) -> 9671321584604
The concatenation of the two integers in each pair contains all the digits from 0 to 9 at least once.
Example Input/Output 2:
Input:
4
2670589 243106 3145987 5789
Output:
4
Python:
num=int(input()) 
list_arr=list(map(str,input().split()))
count=0 
for i in range(len(list_arr)):
    for j in range(i+1,len(list_arr)):
        temp=list_arr[i]+list_arr[j]
        if len(set(temp))==10:
            count+=1
print(count)
