Travelling PNR List
A mini bus having S seats can be overbooked during festival times. Out of N bookings made C bookings can be cancelled. Hence the final travelling list has to be prepared for the first S bookings considering the cancellations. Each booking is assigned a PNR. Given the list of PNRs for all the bookings, the program must print the final list of PNRs for the confirmed bookings after cancellation. (The first S bookings remaining after cancellation are considered confirmed)
Input Format:
The first line contains S and N separated by a space.
Next N lines contain the PNRs of the N bookings made.
N+2 th line contains C
Next C lines contain the PNRs of the C bookings cancelled.
Output Format:
S lines contain the PNRs of the confirmed bookings.
Boundary Conditions:
5 <= S <= 30 2 <= N <= 50 N-C > 0
Length of PNR is from 1 to 20
Example Input/Output 1:
Input:
8 10
Q78QJ
BKT6V
32KEW
ETDZI
EH16B
UVZFS
V3ITC
WGGLO
41VJ8
NVIRB
2
UVZFS
BKT6V
Output:
Q78QJ
32KEW
ETDZI
EH16B
V3ITC
WGGLO
41VJ8
NVIRB
import java.util.*;
public class Hello {
    public static void main(String[] args) {
                        Scanner s=new Scanner(System.in);
                        int m=s.nextInt();
                        int n=s.nextInt();
                        Vector<String> v=new Vector<String>(n);
                        int i;
                        for(i=0;i<n;i++)
                        v.add(s.next());
                        int z=s.nextInt();
                        for(i=0;i<z;i++)
                        v.remove(s.next());
                        for(i=0;i<m&&i<v.size();i++)
                        System.out.println(v.elementAt(i));
            }
}
n,m=[int(i) for i in input().split()]
v=[]
for i in range(m):
    v.append(input().split())
c=int(input())
for i in range(c):
    v.remove(input().split())
for i in range(n):
    if i<n and i<len(v):
        print(*v[i])
#include <iostream>                        
#include<string.h>
using namespace std;
int main(int argc, char** argv)
{
   int s,n,c,i,j;
   cin>>s>>n;
   char p[n][1000];
   int k[n]={0},o=0;             // k array act as a status array
   for(i=0;i<n;i++)
   cin>>p[i];
   cin>>c;
   char d[100];
   for(i=0;i<c;i++){
   cin>>d;
   for(j=0;j<n;j++)
   if(strcmp(d,p[j])==0)
   k[j]=1;
   }
   for(i=0;i<n;i++)
   {
       if(k[i]==0){
       cout<<p[i]<<"\n";
       o++;}
       if(o==s)
       break;
   }

}
