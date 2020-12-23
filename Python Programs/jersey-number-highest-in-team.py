Jersey Number - Highest in Team
Jersey Number - Highest in Team: In a school there are N students standing in a straight line.  Their Jersey numbers from left to right are passed as the input. The students are to be divided into teams of size T starting from left. First T students form Team 1, next T students form Team 2 and so on. If N is not divisible by T and say the remainder is R, the R students are distributed among the teams formed so far in a round robin fashion (starting from the first team) until the R students are assigned to one of the teams.
Once the teams are formed, the program must print the highest jersey number in each team.
Input Format:
The first line contains N.
The second line contains the jersey numbers of N students separated by a space.
The third line contains T.
Output Format:
The highest jersey number in each team separated by a space.
Boundary Conditions:
1 <= N <= 9999999
Example Input/Output 1:
Input:
10
1 5 8 2 4 11 20 6 7 9
5
Output:
8 20
Example Input/Output 2:
Input:
10
1 5 8 2 4 11 3 6 9 7
4
Output:
9 11
#include <stdio.h>
int t(int *a1,int num){
    int t=a1[0];
    for(int ele=1;ele<num;ele++){
        if(t<a1[ele])
        t=a1[ele];
    }
    return t;
}

int main(){
    int num,wlw,bar;
    scanf("%d",&num);
    int a1[999999];
    for(int ele=0;ele<num;ele++)
    scanf("%d",&a1[ele]);
    scanf("%d",&wlw);
    bar=(num/wlw)>0?num/wlw:1;
    int b1[bar];
    for(int ele=0;ele<bar;ele++){
        b1[ele]=t(a1+(wlw*ele),wlw);
        if(num>((bar*wlw)+ele)){
            int foo=(bar*wlw)+ele;
            while(foo<num){
                if(b1[ele]<a1[foo])
                b1[ele]=a1[foo];
                foo+=bar;
            }
        }
    }
    for(int ele=0;ele<bar;ele++)
    printf("%d ",b1[ele]); 
}
a=int(input()) 
b=list(map(int,input().split())) 
c=int(input()) 
i,j=0,0 
d,e=[],[]  
while(i<a and i<(a-(a%c))):
    count=0 
    while(count<c):
        e.append(b[i]) 
        i+=1 
        count+=1 
    d.append(e) 
    e=[] 
k,cc=0,0 
while(i<a):
    cc=0 
    while(cc<(a%c) and i<a):
        d[j].append(b[i]) 
        cc+=1 
        i+=1
    j+=1 
    if(j>=len(d)):
        j=0 
for i in d:
    print(max(i),end=" ")
