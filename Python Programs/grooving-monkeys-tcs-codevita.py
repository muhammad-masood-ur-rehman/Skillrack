Grooving Monkeys - TCS CodeVita
There are N monkeys in a circus. They dance in a circular formation, very similar to a Gujarati Garba or a Drum Circle. The dance requires the monkeys to constantly change positions after every 1 second. The change of position is not random & you, in the audience, observe a pattern. Monkeys are very disciplined & follow a specific pattern while dancing.
Consider N = 6, and the dancing pattern of the 6 monkeys = {3,6,5,4,1,2}.
The value at monkeys[i], indicates the new position of the monkey who is standing at the ith position.
The program must accept N integers representing the dancing pattern of the monkeys. The program must print the time after which all the monkeys are in the initial position for the first time.
Note: Optimize your logic to avoid Time Limit Exceed error.
Boundary Condition(s):
1 <= T <= 10
1 <= N <= 10000
Input Format:
The first line contains T which represents the number of test cases.
Each test case consists of the following.
The first line contains N denoting the number of monkeys.
The next line contains N integers denoting the dancing pattern array.
Output Format:
The first T lines, each contains an integer representing the minimum number of seconds after which all the monkeys are in their initial position.
Example Input/Output 1:
Input:
1
6
4 3 1 5 6 2
Output:
6
Explanation:
In the first test case, N = 6 and the dancing pattern = {4,3,1,5,6,2}.
Suppose monkeys are a,b,c,d,e,f & Initial position (at t = 0) -> a,b,c,d,e,f
At t = 1 -> c,f,b,a,d,e
a will move to 4th position, b will move to 3rd position, c will move to 1st position, d will move to 5th position, e will move to 6th position and f will move to 2nd position.
Recursively applying the same transpositions, we get the following positions for different values of t.
At t = 2 -> b,e,f,c,a,d
At t = 3 -> f,d,e,b,c,a
At t = 4 -> e,a,d,f,b,c
At t = 5 -> d,c,a,e,f,b
At t = 6 -> a,b,c,d,e,f
Since at t = 6, we got the original position, hence the output is 6.
Example Input/Output 2:
Input:
3
10
3 6 5 7 10 4 2 8 1 9
4
4 3 2 1
7
3 6 1 4 7 5 2
Output:
20
2
4
from math import gcd
def l(x,y):
    return(int((x*y)/gcd(x,y)))
n=int(input())
while(n):
    n=n-1
    a=int(input())
    m=list(map(int,input().split()))
    t=1;c=0;p=0 
    while(p<=a-1):
        b=p;c=0 
        while(m[p]!=0):
            h=p 
            p=m[p]-1 
            m[h]=0 
            c+=1 
        p=b+1 
        if(c!=0):
            t=l(t,c) 
    print(int(t))
