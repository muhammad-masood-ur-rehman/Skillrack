Value Equals Previous Two
An array of N integers is passed as the input. The program must find the combination of integers forming a sequence whose length is more than 4 which satisfies the below conditions.
- The ith  index must satisfy arr[i] = arr[i-1] + arr[i-2]
- The length of the sequence must be the maximum possible
- If there are more than one sequences satisfying above two conditions, then print the sequence which contains the smaller value integers.
If there is no such combination of integers, then the program must print -1.
Boundary Condition(s):
1 <= N <= 25
Input Format:
The first line contains N.
The second line contains the N integer values separated by a space.
Output Format:
The first line contains the integer values in the sequence or -1.
Example Input/Output 1:
Input:
9
4 2 7 5 3 8 10 11 19
Output:
2 3 5 8
Explanation:
2 3 5 8 and 3 8 11 19 are the two sequences having same length. But as 2 3 5 8 contains the smaller values, it is printed as the output.
Example Input/Output 2:
Input:
4
1 5 6 10
Output:
-1
Explanation:
Here the sequence 1 5 6 length is not 4. Hence -1 is printed.
num=int(input()) 
lis1=list(map(int,input().split()))  
lis1.sort()  
lis2,lis3=[],[]
for ele in range(num-1):
    for bar in range(ele+1,num): 
        lis2.append(lis1[ele])
        lis2.append(lis1[bar]) 
        t1=0 
        t2=1
        for foo in range(bar+1,num):
            if(lis1[foo]==(lis2[t1]+lis2[t2])):
                lis2.append(lis1[foo])  
                t1+=1 
                t2+=1 
        lis3.append(lis2) 
        lis2=[] 
lis4,lis5=[],[] 
for ele in lis3:
    lis4.append(len(ele)) 
maxima=max(lis4) 
if(maxima<4):
    print(-1) 
    exit() 
for ele in lis3:
    if len(ele)==maxima:
        lis5.append(sum(ele)) 
for ele in lis3:
    if sum(ele)==min(lis5):
        print(*ele)
        break
