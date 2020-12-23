Forward and Reverse Order of Alphabets - Matrix Pattern
Accept an integer N and an alphabet A as input. The program must print the pattern as shown in the Example Input/Output section below. (Note: N is always an even integer and A is always a lowercase alphabet)
Boundary Condition(s):
2 <= N <= 26
Input Format:
The first line contains the value of N.
The second line contains the alphabet A.
Output Format:
The first N lines contain the desired pattern.
Example Input/Output 1:
Input:
2
a
Output:
a z
b y
Explanation:
In the odd columns, the alphabets should be printed in forward order whereas in even columns their corresponding reverse alphabets should be printed as output. Here, a and b are in the odd columns. So, z and y are their corresponding reverse alphabets in the even columns.
Example Input/Output 2:
Input:
4
z
Output:
z a a z
b y c x
d w e v
f u g t
Explanation:
In the odd columns, the alphabets should be printed in forward order whereas in even columns their corresponding reverse alphabets should be printed as output. Here, z, a, b, c, d, e, f, g are in the odd columns. So, a, z, y, x, w, v, u and t are their corresponding reverse alphabets in the even columns.
a=int(input()) 
b=input() 
c=[]
d=[]  
ev=ord(b)  
od=(122-ord(b))+97
for i in range(a):
    for j in range(a): 
        if(j%2==0): 
            if(ev>122):
                ev=97
            c.append(chr(ev))
            ev+=1
        else:
            if(od<97):
                od=122
            d.append(chr(od)) 
            od-=1
x=0 
y=0 
for i in range(a):
    for j in range(a):
        if(j%2==0):
            print(c[x],end=" ")  
            x+=1 
        else:
            print(d[y],end=" ")  
            y+=1 
    print()
