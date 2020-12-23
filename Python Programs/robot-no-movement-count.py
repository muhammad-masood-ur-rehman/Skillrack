Robot No Movement Count
As a final year project certain students in a college have designed a Robot which can move front, back, left or right in a given rectangular grid of dimension L*B units (L denotes the length from left to right and B denotes the breadth from top to bottom). Always the robot moves in units which are of integer values. The robot cannot move outside the grid (That is the robot cannot go beyond L and B units). A sequence of N movement instructions are given to the robot to move in the desired direction (F-front or up, B-back or down, L-left, R-right) and the robot moves if the destination falls within the limit of the grid dimensions. Else the robot does not move. Assume the robot always starts at the bottom left of the grid. The program must print the number of movement instructions C for which the robot did not move (as the destination was outside the grid)
Input Format: The first line contains L and B separated by a space. The second line contains N which denotes the number of instructions. The third line contains N instructions separated by one or more spaces.
Output Format: The first line contains C which denoted the count of instructions for which the robot did not move.
Boundary Conditions:
1 <= L, B <= 999
1 <= N <= 999 C <= N
Example Input/Output 1:
Input:
6 5
9
3R 2L 11R 4F 4R 2F 3B 5L 4B
Output:
3
Explanation: The robot did not move for the instructions 11R, 2F and 4B as they will make the robot go outside the grid.
import re
l,l1=[],[]
le,b=input().split()
x,y,c=0,0,0
s=int(input())
a=input().split()
r=re.compile("([0-9]+)([a-zA-Z]+)")
for i in range(s):
    m=r.match(a[i])
    l.append(m.group(1))
    l1.append(m.group(2))
for i in range(len(l)):
    if l1[i]=="R":
        x+=int(l[i])
        if x<0 or x>int(le):
            c+=1
            x-=int(l[i])
    elif l1[i]=="L":
        x-=int(l[i])
        if x<0 or x>int(le):
            c+=1
            x+=int(l[i])
    elif l1[i]=="F":
        y+=int(l[i])
        if y<0 or y>int(b):
            c+=1
            y-=int(l[i])
    elif l1[i]=="B":
        y-=int(l[i])
        if y<0 or y>int(b):
            c+=1
            y+=int(l[i])

print(c)
#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
    int l,b,i,c,j;
    cin>>l>>b;
	cin>>c;
	int r[c],count=0;
	char a[c];
	for(i=0;i<c;i++)
		cin>>r[i]>>a[i];
	int t=0,s=0,h=0;
	for(i=0;i<c;i++)
		{
		if(a[i]=='R')
			{
    			t=s+r[i];
   			    if(t<=l && t>=0)
    			{
       			 s=t;
   				 }
    			else
   				 {
       			 count++;
   				 }
			}
		else if(a[i]=='L')
			{
    			t=s-r[i];
    			if(t>=0 && t<=l)
   				 {
       				 s=t;
    			 }
    			else
    			{
      			  count++;
    			}
			}
		else if(a[i]=='F')
			{
   				 t=h+r[i];
  				  if(s<l && t>=0 && t<=b)
    				{
     				   h=t;
   					 }
    			  else
   				 {
       				 count++;
    			  }
			}
		else if(a[i]=='B')
			{
   				 t=h-r[i];
    			if(s<l && t>=0 && t<=b)
					{
						h=t;
					}
   				 else
   				 {
       			 count++;
	   				 }
			}
		}
cout<<count;
return 0;
}
   
