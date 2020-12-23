Robot Picking Boxes
Robot Picking Boxes: Robots are used to automate the process of picking up mobile phone boxes and relocating them within a warehouse. The boxes are stacked and arranged adjacently. All the stacks may not have equal number of boxes. The robot can collect and pickup boxes either vertically (boxes in a single stack) or horizontally (across multiple stacks). But when picking up boxes horizontally, the robot can pick up only the boxes in continous stacks in a single attempt. 
Given the number of stacks N and the count of boxes in each stack, the program must print the minimum number of attempts M required to pick (collect) and relocate all the boxes. 
Input Format: 
The first line contains N. 
The second line contains the number of boxes B(1), B(2), … B(N) in the N stacks separated by a space. 
Output Format: 
The first line contains M (which is the minimum number of attempts) 
Boundary Conditions: 
2 <= N <= 100 
1 <= B(i) <= 50 
Example Input/Output 1: 
Input: 
6 
5 4 4 3 4 4 
Output: 
6 
Explanation: The boxes are stacked as given below where each asterisk is a box. 
*
*** **
******
******
******
As the robot can pick only continuous boxes in a single attempt, at least 6 attempts are required. 
Example Input/Output 2: 
Input: 
10 
5 5 5 5 4 5 5 5 5 5 
Output: 
6 
Example Input/Output 3: 
Input: 
10 
29 5 5 5 4 5 5 5 5 18 
Output: 
8
def findCount(a,si,ei):
    rc=0
    if ei-si==0:
        rc+=1
        return rc
    m=999999
    for i in range(si,ei+1):
        if a[i]<m:
            m=a[i]
    rc+=m
    for i in range(si,ei+1):
        a[i]-=m
    sti,eti=-1,-1
    for i in range(si,ei+1):
        if a[i]>0 and sti==-1:
            sti=i
        if a[i]==0 and sti!=-1 and eti==-1:
            eti=i-1
            rc+=findCount(a,sti,eti)
            sti,eti=-1,-1
    if sti!=-1 and eti==-1:
        eti=ei
        rc+=findCount(a,sti,eti)
    return min(rc,ei-si+1)
n=int(input())
a=list(map(int,input().strip().split()))

print (min(n,findCount(a,0,n-1)))
