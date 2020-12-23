Find numbers such that A*B = C*D
A set of numbers (atleast 4 numbers) will be passed as input. The program must find four numbers A,B,C,D such that A*B = C*D and print the value of A*B (that is C*D). (If multiple occurrences of such four numbers exist, print the desired value for the first occurrence).
Input Format:
First line will contain the set of numbers separated by one or more spaces.
Output Format:
The first line will contain the value of A*B or C*D (As both are equal)
Constraints:
The count of numbers in the set is from 4 to 100.

Example Input/Output:
Example 1:
Input:
30 60 180 20 10
Output:
1800
Explanation:
The four numbers A,B,C,D such that A*B=C*D are 30,60,180,10 as 30*60=180*10=1800

Example 2:
Input:
25 5 9 40 75 2 50 6
Output:
150
Explanation:
The four numbers A,B,C,D such that A*B=C*D are 25,6,75,2 as 25*6 = 75*2 = 150
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int arr[100000];
    int l=0;
    
    while(scanf("%d",&arr[l])==1){
        l++;
    }
    for(int i=0;i<l-3;++i){
        for(int j=i+1;j<l-2;++j){
            for(int k=j+1;k<l-1;++k){
                for(int m=k+1;m<l;++m){
                    int a=arr[i],b=arr[j],c=arr[k],d=arr[m];
                    if(a*b == c*d){
                        printf("%d",a*b);
                        return;
                    }
                    else if(a*c == b*d){
                        printf("%d",a*c);
                        return;
                    }
                    else if(a*d == b*c){
                        printf("%d",a*d);
                        return;
                    }
                }
            }
        }
    }
}
