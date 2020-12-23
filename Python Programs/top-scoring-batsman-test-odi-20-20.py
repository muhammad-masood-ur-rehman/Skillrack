Top Scoring Batsman - TEST ODI 20-20
The program must accept the runs scored by N batsmen in the various cricket formats - TEST, ODI and 20-20 and print the top scoring batsman.
- In case two batsmen have scored same total runs, consider TEST cricket runs. The batsman who has scored higher runs in TEST cricket is the top scoring batsman.
- In case two batsmen have scored same total runs and have TEST cricket runs equal, consider ODI runs.
- In case two students have scored same total runs and have TEST and ODI runs equal, consider 20-20 runs.
Input Format:
The first line contains N.
N lines follow with each line containing Batsman Name and runs in TEST, ODI and 20-20 runs (the values are separated by a space).
Output Format:
The first line contains the name of the top Scoring Batsman.
Boundary Conditions:
1 <= N <= 20
Example Input/Output 1:
Input:
3
Raman 400 300 200
Dujon 800 50 50
Chandan 500 200 200
Output:
Dujon
n=int(input())
l=[]
for i in range(n):
    a=list(map(str,input().split()))
    a[1],a[2],a[3]=int(a[1]),int(a[2]),int(a[3])
    l.append(a)
m=[0]
for i in l: 
    if sum(i[1:])>sum(m[1:]):
        m=i 
    elif sum(i[1:])==sum(m[1:]):
        if i[1]>m[1]: 
            m=i 
        elif i[1]==m[1]: 
            if i[2]>m[2]:
                m=i 
            elif i[2]==m[2]: 
                if i[3]>m[3]: 
                    m=i 
print(m[0])
