Smallest Palindromic Integer - Greater than X
The program must accept N unique digits and an integer X as the input. The program must print the smallest palindromic integer, which is formed from the given N digits and is greater than X.
Note: At least one non-zero digit is always present in the given N digits.
Input Format:
The first line contains N.
The second line contains N digits separated by a space.
The third line contains X.
Output Format:
The first line contains the smallest palindromic integer, which is formed from the given N digits and is greater than X.
Example Input/Output 1:
Input:
3
2 4 0
567
Output:
2002
Explanation:
The smallest palindromic integer is 2002, which is formed from the given 3 digits and is greater than 567.
Hence the output is 2002
Example Input/Output 2:
Input:
4
1 2 3 4
12545
Output:
13131
C:
#include<stdio.h>
#include <stdlib.h>

int check(char s[],int ref[])
{
    for(int i=0;i<strlen(s);i++)
    {
    if(s[i]!=s[strlen(s)-1-i]||ref[s[i]-'0']==0)
    return 0;
    }
    return 1;
}
int main()
{
int num,i,j,k,possi=0,ref[11]={0};
char ele[11],string[10];
scanf("%d ",&num);
for(i=0;i<num;i++){
scanf("%c ",&ele[i]);
ref[ele[i]-'0']++;
}
scanf("%d",&k);
ele[num]='\0';
for(i=k+1;;i++)
{
    sprintf(string,"%d",i);
    possi=0;
    if(string[0]==string[strlen(string)-1]&&check(string,ref)==1)
    possi=1;
    if(possi==1)
    {
    printf("%d",i);
    break;
    }
}
}
#include<stdio.h>
#include <stdlib.h>
char fun(int* hash,char start){
    for(int ele=start;ele<='9';++ele){
        if(hash[ele])return ele;
    }
    return ' ';
}
int main()
{
    int num;
    scanf("%d",&num);
    
    int hash[256]={0};
    
    for(int ele=0;ele<num;++ele){
        int num;scanf("%d",&num);
        hash[num+'0']++;
    }
    char str[10];
    scanf("%s",str);
    
    char answe[11];

    int ele=0,foo=strlen(str)-1;
    int temp1=0,temp2=foo;
    answe[temp2+1]='\0';
    
    int notpossible=1;
    
    char sigmin=fun(hash,'1');
    char min=hash['0'] ? '0' : sigmin ;

    while(ele<=foo){
        char next=str[ele]+1;
        while(next<='9' && hash[next]==0)next++;
        if(hash[str[ele]]){
            answe[temp1++]=str[ele];
            answe[temp2--]=str[ele];
        }
        else if(next<='9' && next>str[ele]){
            answe[temp1++]=next;
            answe[temp2--]=next;
            notpossible=0;
            break;
        }
        else{
            notpossible=1;
            break;
        }
        ele++;
        foo--;
    }
    if(notpossible){
        if(temp2<temp1){
            int t1=atoi(str),t2=atoi(answe);
            if(t2>t1 ){
                printf("%d",t2);
                return;
            }
        }
        --temp1;temp2++;
        while(temp1>-1){
            char temp=str[temp1]+1;
            char ch='*';
            for(int var=temp;var<='9';++var){
                if(hash[var]){
                    ch=var;
                    answe[temp1++]=var;
                    answe[temp2--]=var;
                    notpossible=0;
                    break;
                }
            }
            if(ch!='*')break;
            temp1--;temp2++;
        }
    }
    if(notpossible){
        printf("%c",sigmin);
        for(int k=0;k<strlen(str)-1;++k)printf("%c",min);
        printf("%c",sigmin);
        return;
    }
    while(temp1<=temp2){
        answe[temp1++]=min;
        answe[temp2--]=min;
    }
    printf("%s",answe);
    return 0;
}
Python:
num=int(input())
li=set(map(str,input().split()))
ctr=int(input())
k=0
ctr=ctr+1
while(True):
    temp=str(ctr)
    if temp==temp[::-1]:
        if set(temp).issubset(li):
            print(temp)
            k=1 
    if k==1:
        break
    ctr+=1
