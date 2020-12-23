Cyclic Path or Not
The program must accept N pairs of integers as the input. Each pair contains two integers representing the starting point S and the eliding point E of a path. The program must print YES if a cyclic path is formed by connecting all the N paths. Else the program must print NO as the output. The two paths P1 and P2 can be connected only if the end point of P1 is equal to the starting point of P2. 
Boundary Condition(s): 
2 <= N <= 20 
-100 <= E, P <= 100
Input Format: 
The first line contains the value of N. 
The next N lines contain two integers on each line separated by a space.
Output Format: 
The first line contains either YES or NO.
Example Input/Output 1: 
Input: 
4 
2 3
5 1
3 5 
1 2
Output: 
YES
The cyclic path formed using the 4 paths is given below. 
2->3->5->1->2 
So YES is printed as the output.
n=int(input());z,y=[],[];x=[]
for i in range(n):
    a,b=map(int,input().split())
    if [b,a] in x and n>2:
        print('no'.upper());quit()
    x.append([a,b]) 
    z.append(a);y.append(b)
z.sort();y.sort()
if z==y:print('yes'.upper())
else:print('no'.upper())
