Distinct Length Pairs
The program must accept M integers and N integers as the input. The program must form pairs of integers by selecting one integer from M integers and another integer from N integers. Then the program must print the number of pairs containing two integers with different number of digits as the output.
Boundary Condition(s):
1 <= M, N <= 10^4
1 <= Each integer value <= 10^16
Input Format:
The first line contains M and N separated by a space.
The second line contains M integers separated by a space.
The third line contains N integers separated by a space.
Output Format:
The first line contains the count of pairs as per the conditions.
Example Input/Output 1:
Input:
3 4
12 1 454
988 2 112 47
Output:
8
Explanation:
The pairs with two different length integers are
12 988
12 2
12 112
1 988
1 112
1 47
454 2
454 47
Example Input/Output 2:
Input:
5 10
464 69 1 9 62
69 26 592 28 22 252 172 341 9 5
Output:
34
num1,num2=map(int,input().split()) 
lis1=list(map(int,input().split())) 
lis2=list(map(int,input().split()))  
lis3,lis4=[],[]
for ele in lis1: 
    lis3.append(len(str(ele))) 
for ele in lis2:
    lis4.append(len(str(ele))) 
lis3.sort()  
lis4.sort()  
ctr=0
for ele in lis3:
    ctr+=(len(lis4)-lis4.count(ele)) 
print(ctr)
