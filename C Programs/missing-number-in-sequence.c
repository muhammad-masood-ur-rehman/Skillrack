Missing Number In Sequence
A set of numbers which are in sequence are arranged in descending order as a string S. But one of the number in the sequence is missing in between in the string S. This string S is passed as input to the program. The program must identify the missing number M and print it as output.
Input Format:
The first line will contain the set of numbers in the sequence.
Boundary Conditions:
1 <= M <= 99999
Length of string S is from 5 to 200.
Output Format:
The first line will contain the missing number M.

Example Input/Output 1:
Input:
98764321
Output:
5
Explanation:
The numbers a sequence in descending order are 9 8 7 6 5 4 3 2 1. As 5 is missing, it is printed as the output.

Example Input/Output 2:
Input:
601600598597596
Output:
599
Explanation:
The numbers a sequence in descending order are 601 600 599 598 597 596. As 599 is missing, it is printed as the output.
#include <stdio.h>
long int n(char *a){
    long int b=0;
    for(int i=0;i<strlen(a);i++){
        if(isdigit(a[i])&&a[i])
            b=b*10+a[i]-'0';
        }
        return b;
    }
void stcpy(char *a,char *b,int i){
    int n=0,l=strlen(b);
    for(n=0;n<l&&n<i;n++){
        a[n]=b[n];
    }
    a[n]='\0';
}
int main(){
    char a[1000],b[3][10];
    scanf("%s",a);
    int i,k,k1,l=strlen(a),f=0;
    i=5;
    while(i>0){
        stcpy(b[0],a,i);
        stcpy(b[1],a+i,i);
        stcpy(b[2],a+i,i-1);
        int k[3]={n(b[0]),n(b[1]),n(b[2])};
        if(k[0]-k[1]==1||k[0]-k[1]==2||k[0]-k[2]==1||k[0]-k[2]==2){
            f=k[0];
            break;
        }
        i--;
    }
for(int i=0;i<l;i++){
    sprintf(b[0],"%d",f);
    if(strncmp(a+i,b[0],strlen(b[0]))==0)
    i+=strlen(b)-1;
    else{
        printf("%d",f);
        break;
    }
    f--;
}
}
