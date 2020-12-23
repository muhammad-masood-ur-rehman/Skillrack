Float Sum - Concatenation
The program must accept N integers (where N is always even) as the input. The program must form N/2 float values by concatenating every two integers with a . (Dot) between them. Then the program must print the sum of those N/2 float values with the precision up to 3 decimal places as the output.
Boundary Condition(s):
2 <= N <= 100
0 <= Each integer value <= 1000
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains the sum of N/2 float values with the precision up to 3 decimal places.
Example Input/Output 1:
Input:
4
31 481 686 83
Output:
718.311
Explanation:
Here N = 4 and the 4 integers are 31, 481, 686 and 83.
The float values 31.481 and 686.83 are formed by concatenating every two integers with a . (Dot) between them.
The sum of the two float values with the precision up to 3 decimal places is 718.311 (31.481 + 686.83).
So 718.311 is printed as the output.
Example Input/Output 2:
Input:
6
5 1 0 12 8 0
Output:
13.220
n=int(input())
l=list(map(int,input().split()))
s=0;d=0 
for i in range(0,n,2):
    s+=float('0'+'.'+str(l[i+1]))
    d+=l[i]
print("%.3f"%float(s+d))
