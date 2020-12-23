Batsman Score
Batsman Score: Given an integer R as input, the program must print Double Century if the given integer R is greater than or equal to 200. Else if the program must print Century if the given integer R is greater than or equal to 100. Else if the program must print Half Century if the given integer R is greater than or equal to 50. Else the program must print Normal Score.
Boundary Condition(s):
1 <= R <= 999
Input Format:
The first line contains the value of R.
Output Format:
The first line contains Double Century or Century or Half Century or Normal Score.
Example Input/Output 1:
Input:
65
Output:
Half Century
Example Input/Output 2:
Input:
158
Output:
Century
r=int(input())
print('Double Century') if r>=200 else print('Century') if r>=100 else print('Half Century') if r>=50 else print('Normal Score')
