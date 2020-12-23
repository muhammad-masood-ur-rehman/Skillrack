Expiry Date - After M Months
C:
#include<stdio.h>
#include <stdlib.h>
int main(){
int m,y,e;
scanf("%d-%d\n%d",&m,&y,&e);
y=y+(e/12);
m=m+(e%12);
if(m>12){
m=m%12;
y++;
}
printf("%02d-%d",m,y);
}
Java:
import java.util.*;
import java.text.DecimalFormat;
public class Hello {
    public static void main(String[] args) {
		DecimalFormat df = new DecimalFormat("00");
		Scanner sc = new Scanner(System.in);
		String[] date = sc.nextLine().split("[-]");
		int months = sc.nextInt();
		int initialmonth=(Integer.parseInt(date[0])+months%12);
		int year = (Integer.parseInt(date[1]));
		year+=(Integer.parseInt(date[0])+months)%12==0?
		(int)((Integer.parseInt(date[0])+months)/12)-1
		:(int)((Integer.parseInt(date[0])+months)/12);
		int finalmonths = initialmonth%12==0?12:initialmonth%12;
		String expmonth=df.format(finalmonths);
		System.out.println(expmonth+"-"+year);
	}
}
Python:
a=list(input().split("-"))
b=int(input())
t=int(a[0])
t1=int(a[1])
while b>0:
    if t<12:
        t+=1
    elif t==12:
        t1+=1 
        t=1
    b-=1
print("%02d"%t,end="-")
print(t1)
C++:
#include <iostream> 
using namespace std;
int main(int argc, char** argv)
{
int mm,yy,m;
cin>>mm;
cin>>yy;
cin>>m;
int k=mm+m;
int d=0;
while(k>12){
    d++;
    k=k-12;
}
int h=yy-d;
if(k<10){
    cout<<0<<k<<h;
}
else{
    cout<<k<<h;
}
}
