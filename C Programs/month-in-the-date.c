Month in the Date
The program must accept a valid date D in the format of DD-MM-YYYY as the input. The program must print the name of the month in the given date as the output.
Input Format:
The first line contains a valid date.
Output Format:
The first line contains the month for the given date.
Example Input/Output 1:
Input:
27-11-1997
Output:
November
Explanation:
The given date is 27-11-1997. The month 11 indicates November.
Hence the output is November
Example Input/Output 2:
Input:
08-04-2020
Output:
April
Python:
st=input().split("-") 
months=["January" ,"February" "March","April" "May" "June" ,"July","August" ,"September" ,
"October" ,"November" ,"December"] 
 ele=int(str[1])-1 
 print(months[ele])
st=input().split("-") 
months={"01":"January","02":"February","03":"March","04":"April","05":"May", "06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"] 
 print(months[st[1]])
import datetime
s=input().split("-")
x=datetime.datetime(int(s[2]),int(s[1]),int(s[0]))
print(x.strftime("%B"))
import datetime
s=input().split("-")
x=datetime.datetime(int(s[2]),int(s[1]),int(s[0]))
print(x.strftime("%B"))
C:
int main()
{
int day,month,year;
scanf("%d-%d-%d",&day,&month,&year);
char monthlist[13][10]={"January","February","March","April",
                "May","June","July","August","September",
                "October","November","December"};
printf("%s",monthlist[month-1]);
}
#include<stdio.h>
#include <stdlib.h>

int main()
{
int x,y,z;
scanf("%d-%d-%d",&x,&y,&z);
switch(y){
    case 1:
     printf("January");
     break;
     case 2:
     printf("February");
     break;
     case 3:
     printf("March");
     break;
     case 4:
     printf("April");
     break;
     case 5:
     printf("May");
     break;
     case 6:
     printf("June");
     break;
     case 7:
     printf("July");
     break;
     case 8:
     printf("August");
     break;
     case 9:
     printf("September");
     break;
     case 10:
     printf("October");
     break;
     case 11:
     printf("November");
     break;
     case 12:
     printf("December");
     
}

}
int main()
{
int day,month,year;
scanf("%d-%d-%d",&day,&month,&year);
if(month==1)
printf("January");
else if(month==2)
printf("February");
else if(month==3)
printf("March");
else if(month==4)
printf("April");
else if(month==5)
printf("May");
else if(month==6)
printf("June");
else if(month==7)
printf("July");
else if(month==8)
printf("August");
else if(month==9)
printf("September");
else if(month==10)
printf("October");
else if(month==11)
printf("November");
else
printf("December");
}
