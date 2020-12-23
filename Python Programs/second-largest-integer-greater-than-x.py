Second Largest Integer - Greater than X
Second Largest Integer - Greater than X: The program must accept N integers and an integer X as the input. The program must print the second largest integer greater X among the given N integers as the output.
Note: At least two integers are always greater than X in the given N integers.
Boundary Condition(s):
3 <= N <= 100
1 <= Each integer value, X <= 10^3
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains X.
Output Format:
The first line contains an integer representing the second largest integer greater than X among the given N integers.
Example Input/Output 1:
Input:
8
18 11 13 9 6 25 36 2
15
Output:
25
Explanation:
The second largest integer greater than 15 among the given 8 integers is 25.
So 25 is printed as the output.
Example Input/Output 2:
Input:
6
10 10 20 30 40 50
9
Output:
20
num1=int(input())
list1=list(map(int,input().split()))
list1=sorted(set(list1))
num2=int(input())
final_list=[ele for ele in list1 if ele>num2][1]
print(final_list)
YouTube Explanations and Solutions for
Second Largest Integer - Greater than X
https://www.youtube.com/watch?v=sZtIzYNjzZg 
https://www.youtube.com/watch?v=EfsAKQcd7hY 
