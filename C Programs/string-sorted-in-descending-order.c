String Sorted in Descending Order
The program must accept N string values as the input. The program must print the N string values sorted lexicographically in descending order as the output. 
Note: All the alphabets are lowercase in each string. 
Boundary Condition(s): 1 <= N <= 50 1 <= Length of each string <= 1000 
Input Format: The first line contains the integer N. The next N lines contain a string in each line. 
Output Format: The first N lines contain the string values sorted lexicographically in descending order. 
Example Input/Output 1: 
Input: 
4 
project 
elephant 
tiger 
time 
Output: 
time tiger project elephant 
Example Input/Output 2: Input: 
5 
orange watermelon  pineapple lemon strawberry 
Output: watermelon strawberry pineapple orange lemon
#include<stdio.h>
#include <stdlib.h>
#include<string.h>
int main()
{
    int n;
    scanf("%d",&n);
    char str[1001][1001],temp[1001][1001];
    int i,j;
    for(i=0;i<n;i++)
    scanf("%s",str[i]);
    for(i=0;i<n;i++)
        for(j=i+1;j<n;j++){
            if(strcmp(str[i],str[j])>0){
                strcpy(temp[i],str[i]);
                strcpy(str[i],str[j]);
                strcpy(str[j],temp[i]);
            }
        }
    for(i=n-1;i>=0;i--)
    printf("%s\n",str[i]);
}                       
