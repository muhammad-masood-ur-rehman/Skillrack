Print February Calendar
A specific year Y and the starting day of the year D is given as input. Print the February month calendar for that specific year as shown in the Example Input/Output section.
Input/Output Format:
Input:
First line contains the year Y and starting day D separated by a space.
Output:
Print the February month calendar for the given year Y.
Example Input/Output 1:
Input:
2018 MON
Output:
S M T W T F S
* * * * 1 2 3 
4 5 6 7 8 9 10 
11 12 13 14 15 16 17 
18 19 20 21 22 23 24 
25 26 27 28 * * * 
Example Input/Output 2:
Input:
1597 WED
Output:
S M T W T F S
* * * * * * 1 
2 3 4 5 6 7 8 
9 10 11 12 13 14 15 
16 17 18 19 20 21 22 
23 24 25 26 27 28 * 
#include <iostream>
#include<string>
using namespace std;
int main(){
 int i,j,k,m,n,s,t=0,u,v,year,month;
 string day;
 cin>>year>>day;
 if(year%400==0||(year%4==0&&year%100!=0))
 {
     month=29;
 }
 else
 month=28;
 if(day=="MON")s=5;
 if(day=="TUE")s=6;
 if(day=="WED")s=7;
 if(day=="THU")s=1;
 if(day=="FRI")s=2;
 if(day=="SAT")s=3;
 if(day=="SUN")s=4;
 int a[8][8]={0};
 t=1;
 for(i=1;i<6;i++)
 {
     if(i==1)
     {
         for(j=s;j<8;j++)
         {
             a[i][j]=t;
             t++;
         }
     }
     else
     {
         for(j=1;j<8;j++)
         {
             if(t<=month)
             {
                 a[i][j]=t;
                 t++;
             }
         }
     }
 }
 cout<<"S M T W T F S\n";
 for(i=1;i<8;i++)
 {
     if(a[5][i]!=0)
     break;
 }
 if(i==8)
 v=5;
 else
 v=6;
 for(i=1;i<v;i++)
 {
     for(j=1;j<8;j++)
     {
         if(a[i][j]!=0)
         cout<<a[i][j]<<" ";
         else
         cout<<"* ";
     }
     cout<<endl;
 }
}
