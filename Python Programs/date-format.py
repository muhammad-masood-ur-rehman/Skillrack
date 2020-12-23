Date Format
The program must accept a date as the input. The program must print the date in the mentioned format as shown in the Example Input/Output section.
Input Format:
The first line contains the input date in the format YYYYMMDD where YYYY represents Year, MM represents Month and DD represents Date.
Output Format:
The first line contains the date as shown in the Example Input/Output section.
Example Input/Output :
Input:
20160302
Output:
2016, 2nd of March
Python:
s=input().strip()
year=s[:4]
month=s[4:6]
date=s[6:]
l=["January","February","March","April","May","June","July","August","September","October","November","December"]
a=int(date)%10
if(a==1):
    sufx="st"
elif(a==2):
    sufx="nd"
elif(a==3):
    sufx="rd"
else:
    sufx="th"
print(str(int(year)) +", "+str(int(date))+sufx+" of "+l[int(month)-1])
s=input().strip();y=s[:4];m=s[4:6];d=s[6:];a=int(d)%10
l=["January","February","March","April","May","June","July","August","September","October","November","December"]
sx='st' if a==1 else 'nd' if  a==2  else 'rd' if a==3 else 'th'
print(str(int(y))+", "+str(int(d))+sx+" of "+l[int(m)-1])
C:
#include<stdio.h>
#include <stdlib.h>
char* fun(int n){
    return n==1? "January" : n==2? "February" : n==3? "March" : n==4? "April" : n==5? "May" : n==6? "June" : n==7? "July" : n==8?"August" : n==9?"September" : n==10? "October": n==11? "November" : "December";
}
int main()
{
    int n;
    scanf("%d",&n);
    char str[10];
    str[0]='\0';
    int var=n%100;
    if(var==1 || var==21 || var==31){
        strcpy(str,"st");
    }
    else if(var==3 || var==23){
        strcpy(str,"rd");
    }
    else if(var==2 || var==22){
        strcpy(str,"nd");
    }
    else {
        strcpy(str,"th");
    }
    printf("%d, %d%s of %s",n/10000,n%100,str,fun((n%10000)/100));

}
