Swap Integers - Equal Sum Matrices
Swap Integers - Equal Sum Matrices: The program must accept two integer matrices M1 and M2 of equal size RxC as the input. If it is possible to equalize the sum of the integers in M1 and M2 by swapping an integer at the same position between two matrices, then the program must print the integers after the swapping as the output. If two or more such swaps are possible, then the program must consider the first occurring swap. If it is not possible to equalize the sum of the integers In M1 and M2 or they are already equal, then the program must print -1 as the output.

Example Input/Output 1:
Input:
2 2
3 2
3 4
1 4
1 2
Output:
13

Example Input/Output 2:
Input:
3 4
18 45 49 11
48 56 31 12
63 21 18 36
35 14 95 10
70 16 36 11
73 30 70 12
Output:
-1
r,c=map(int,input().split())
m1=[list(map(int,input().split())) for i in range(r)]
m2=[list(map(int,input().split())) for i in range(r)]
for i in range(r):
    for j in range(c):
        m1[i][j],m2[i][j]=m2[i][j],m1[i][j]
        s,s1=0,0
        for k in m1:
            s+=sum(k)
        for k in m2:
            s1+=sum(k)
        if s==s1 and m1[i][j]!=m2[i][j]:
            print(m1[i][j],m2[i][j])
            exit()
        m1[i][j],m2[i][j]=m2[i][j],m1[i][j]
else:
    print(-1)
YouTube Explanations and Solutions:
https://www.youtube.com/watch?v=xuPRqgGwEmM 
https://www.youtube.com/watch?v=KZZ3w4h_cYs 
