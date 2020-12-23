Difference between sum of odd and even digits
A number N is passed as input. The program must find the difference between sum of odd and even digits in the number and print the difference.
Input Format:
In the first line, number N is passed as input.
Output Format:
The difference between the sum of odd and even digits is printed as the first line.
Boundary Conditions:
0 < N < 9999999
Example Input/Output 1:
Input:
561790
Output:
16
Explanation:
Sum of odd digits = 5+1+7+9 = 22
Sum of even digits = 6+0 = 6
So the difference is 22-6 = 16 is printed as the output.
Example Input/Output 2:
Input:
88125
Output:
-12
Explanation:
Sum of odd digits = 1+5 = 6
Sum of even digits = 8+8+2 = 18
So the difference is 6-18 = -12 which is printed as the output.
n=input().strip();s=0;d=0
for i in n:
  if int(i)%2==0:s+=int(i)
  else:d+=int(i) 
print(d-s)
