Count Embedded Integers in String
A string is passed as input. The program must print the count of integers present in the string.
Boundary Condition(s):
1 <= Length of string <= 1000
Input Format:
The first line contains the string.
Output Format:
The first line contains the count of integers.
Example Input/Output 1:
Input:
bingo123alpha56beta
Output:
2
Explanation:
The two integers are 123 and 56.
Example Input/Output 2:
Input:
73dknj99ff8we99
Output:
4
Explanation:
The four integers are 73, 99, 8 and 99.
C:
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char a[1000];
    scanf("%s",a);
    int ele,temp, count=0;
    for(ele=0;ele<strlen(a);ele++){
        if(isdigit(a[ele])){
            temp=ele;
            while(isdigit(a[temp]))
            temp+=1;
            ele=temp;
            count+=1;
        }
    }
    printf("%d ",count);
}
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char s[1000];
    scanf("%s",s);
    
    int count=0,counter=0,i=0;
    while(i<strlen(s)){
        if(s[i]>='0' && s[i]<='9'){
            if(!counter)count++;
            counter=1;
        }
        else{
            counter=0;
        }
        i++;
    }
    printf("%d",count);
}
