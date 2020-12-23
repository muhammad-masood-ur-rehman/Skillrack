Python Program To Print Number Frequency
An array of N integers is passed as the input to the program. The program must modify the array such that each element in the array is replaced by its frequency of occurrence in the array. Finally the program must print the integers in the modified array.
Boundary Condition(s):
1 <= N <= 10000
1 <= Value of each integer <= 1000000
Input Format:
The first line contains N.
The second line contains the value of the N integers separated by space(s).
Output Format:
The first line contains N integers separated by space.
Example Input/Output 1:
Input:
10
45 22 14 14 45 23 23 23 45 45
Output:
4 1 2 2 4 3 3 3 4 4
Example Input/Output 2:
Input:
6
11 45 45 67 67 67
Output:
1 2 2 3 3 3
n=int(input())
l=list(map(int,input().split()))
print(*[l.count(i) for i in l])
