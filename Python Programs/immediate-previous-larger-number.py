Immediate Previous Larger Number
Immediate Previous Larger Number: N numbers are passed as input to the program. The program must print the immediate previous larger number. If there is no such larger number print 0 for that specific number.
Note: As N can be as high as 100000, optimize your algorithm to avoid timeout.
Input Format:
The first line contains N.
The second line contains N numbers separated by a space.
Output Format:
The first line contains N numbers which denote the immediate previous larger number.
Boundary Conditions:
2 <= N <= 100000
Example Input/Output 1:
Input:
11
455 346 76 304 488 374 385 433 350 9 1000
Output:
0 455 346 346 0 488 488 488 433 350 0
a=int(input()) 
b=list(map(int,input().split())) 
c=0
for i in range(a): 
    found=0 
    for j in reversed(range(i)): 
        if(b[i]<b[j]):
            print(b[j],end=" ") 
            found=1 
            break 
    if(found==0):
        print(c,end=" ")
