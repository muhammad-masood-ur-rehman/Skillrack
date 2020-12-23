Robot Ditch Catch-22
A robot is programmed to move forward F meters and backwards again, say B meters, in a straight line. The Robot covers 1 meter in T units of time. On Robot's path there is a ditch at a distance FD from initial position in forward direction as well as a ditch at a distance BD from initial position in backward direction. This forward and backward movement is performed repeatedly by the Robot.
Your task is to calculate amount of time taken, before the Robot falls in either ditch, if at all it falls in a ditch.

Input Format:
First line contains total number of test cases, denoted by N
Next N lines, contain a tuple containing 5 values delimited by space
F B T FD BD, where
- F denotes forward displacement in meters
- B denotes backward displacement in meters
- T denotes time taken to cover 1 meter
- FD denotes distance from Robot's starting position and the ditch in forward direction
- BD denotes distance from Robot's starting position and the ditch in backward direction

Output Format:
For each test case print time taken by the Robot to fall in the ditch and also state which ditch he falls into. Print F for forward and B for backward. Both the output must be delimited by whitespace
OR
Print No Ditch if the Robot does not fall in either ditch

Boundary Conditions / Constraints:
First move will always be in forward direction
1 <= N <= 100
F > 0
B > 0
T > 0
FD > 0
BD > 0
All input values will be positive integers.

Example Input/Output 1:
Input:
3
9 4 3 13 10
9 7 1 11 13
4 4 3 8 12
Output:
63 F
25 F
No Ditch
#include<stdio.h>
#include<conio.h>
void main(){
    int n,i;
    int f,b,fd,bd,t,c=0,tc=0;
    scanf("%d",&n);
    if(n>=1 && n<=100){
        for(i=0;i<n;i++){
            scanf("%d %d %d %d %d",&f,&b,&t,&fd,&bd);
            if(fd>0 && bd>0 &&  t>0 && f>0 && b >0){
                if(f>=fd){
                    c=fd*t;
                printf("%d F\n",c);
                }
                else if(f==b){
                    printf("NO Ditch\n");
                }
                else if(f>b){
                    while(!0){
                        tc=tc+f;
                        c=c+f;
                        if(c>fd) break;
                        c=c-b;
                        tc=tc+b;
                    }
                    tc=tc-(c-fd);
                    printf("%d F\n",tc*t);
                }
                else{
                    while(!0){
                        tc=tc+f;
                        c=c-f;
                        if(c>bd) break;
                        c=c+b;
                        tc=tc+b;
                    }
                    tc=tc-(c-bd);
                    printf("%d B\n",tc*t);
                }
            }
        }
    }
}
