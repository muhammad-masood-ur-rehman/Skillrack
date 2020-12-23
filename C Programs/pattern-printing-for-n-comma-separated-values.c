Pattern Printing for N Comma Separated Values
Pattern Printing for N Comma Separated Values: The below program must print the given array of numbers in the given format for a given size N. The values of N can be 3, 6, 10, 15, 21 and so on.
Input Format:
The first line will contain N comma separated integer values.
Output Format:
The desired pattern as given below.
Constraints:
N = 3, 6, 10, 15, 21, 28, 36, .... but less than 10000.
3 <= Length of input string <= 10000000
Example Input/Output 1:
Input:
11,12,13,14,15,16
Output:
11
12 14
13 15 16
Example Input/Output 2:
Input:
11,12,13,14,15,16,17,18,19,20
Output:
11
12 15
13 16 18
14 17 19 20
Example Input/Output 3:
Input:
100,201,555
Output:
100
201 555
#include<stdio.h>
#include <stdlib.h>
int main()
{
    char str[10000001];
    scanf("%s",str);
    int l=strlen(str),ind=0;
    int arr[10000001];
    int num=0;
    for(int i=0;i<l;++i)
    {
        if(str[i]==','){
            arr[ind++]=num;
            num=0;
        }
        else{
            num= (num*10) + (str[i]-'0');
        }
    }
    arr[ind++]= num;
    l=ind;
    
    int n= 0;
    while(((n*(n+1))/2)!=l){
        n++;
    }
    int prev=1;
    for(int i=1;i<=n;++i){
        prev=i-1;
        printf("%d ",arr[i-1]);
        for(int j=2;j<=i;++j){
            printf("%d ",arr[n-j+prev+1]);
            prev=n-j+prev+1;
        }
        printf("\n");
    }
    return 0;
}
