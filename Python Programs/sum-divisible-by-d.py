Sum divisible by D
Two numbers A and B are passed as input. The program must print yes if the sum of these two numbers A and B is divisible by a third number D. The program must print no if the sum of these two numbers A and B is NOT divisible by D.
Input Format:
The first line denotes the value of A.
The second line denotes the value of B.
The third line denotes the value of D.
Output Format:
The first line either contains yes or no (The output is case SENSITIVE)
Boundary Conditions:
1 <= A <= 9999999
1 <= B <= 9999999
2 <= D <= 50
Example Input/Output 1:
Input:
50
40
9
Output:
yes
Explanation:
The sum of 50 and 40 is 90 which is divisible by 9. Hence the program prints yes.
Example Input/Output 2:
Input:
80
3
20
Output:
no
Explanation:
The sum of 80 and 3 is 83 which is divisible by 20. Hence the program prints no
a=int(input())
b=int(input())
c=int(input())
if(a+b)%c==0:
    print("yes")
else:
    print("no")
