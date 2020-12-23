Six Blocks Two Towers
Six Blocks Two Towers: Accept an input of 6 numbers which represent the height of blocks. Also accept 2 numbers which represent the height of the towers. Use the blocks to get the desired height of the towers by using 3 blocks for each tower. The result for each tower should be printed in descending order of the height of the blocks.
Boundary Condition(s):
1 <= Height of the blocks <= 1000
3 <= Height of the towers <= 3000
Input Format:
The first line contains the height of the six blocks separated by a space.
The second line contains the height of the two towers separated by a space.
Output Format:
The first line contains the height of the blocks forming tower1 (separated by a space) and then an ampersand which is again followed by the height of the blocks forming tower2 (separated by a space).
Example Input/Output 1:
Input:
10 15 90 65 30 25
135 100
Output:
90 30 15 & 65 25 10
Example Input/Output 2:
Input:
45 30 12 18 10 40
40 115
Output:
18 12 10 & 45 40 30
li=list(map(int,input().split())) 
a1,a2=map(int,input().split()) 
l=0;r=0;f=0
d=[]
for foo in range(4):
    for bar in range(foo+1,5):
        for ele in range(bar+1,6):
            if(li[foo]+li[bar]+li[ele]==a1):
                d.append(li[foo]) 
                d.append(li[bar]) 
                d.append(li[ele])   
                li.pop(foo)
                li.pop(bar-1) 
                li.pop(ele-2)
                f=1
                break 
        if(f==1):
            break 
    if(f==1):
        break
d=sorted(d,reverse=True)
li=sorted(li,reverse=True)
print(*d,sep=" ",end=" ") 
print("&",end=" ") 
print(*li,sep=" ")
