Merge Strings
Two strings S1 and S2 can be concatenated to form string S3. If certain characters of the first part of S2 matches with those characters in the last part of S1, they can be merged to occur only once.
Given S1 and S2 as the input, the program must print the minimum possible length of S3.
Input Format:
The first line contains S1.
The second line contains S2.
Output Format:
The first line contains the integer value representing the minimum possible length of S3.
Boundary Conditions:
1 <= Length of S1 and S2 <= 1000
Example Input/Output 1:
Input:
abcdef
efghij
Output:
10
Explanation:
The common part is ef and hence S3 becomes abcdefghij whose length is 10.
#include<stdio.h>
#include <stdlib.h> 
int main(){
    char a[1001],b[1001];
    int i,l,u;
    scanf("%s %s",a,b);
    for(i=0;i<strlen(a);i++){
        if(a[i]==b[0]){
            l=i,u=0;
            while(l<strlen(a)&&a[l]==b[u++])
            l++;
            if(l==strlen(a))
            break; 
        }
    } 
printf("%d",strlen(a)+strlen(b)-u);
} 
