Find the lowest average temperature for N days
The temperature recorded in a city in a week will be passed as input. The program must print the lowest average temperature for any 3 consecutive days.

Input Format:
In the first line, the value of the temperatures will be passed as the input separated by space.
Output Format:
The lowest average temperature for any 3 consecutive days is printed as output (precision upto 2 decimal places)
Example Input/Output 1:
Input:
20 24 21 18 12 35 25
Output:
17.00
Explanation:
The lowest average is (21+18+12)/3 = 51/3 = 17.00
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int arr[1000],l=0;
    
    while(scanf("%d",&arr[l])==1){
        l++;
    }
    float ans=9999999;
    for(int i=0;i<l-2;++i){
        float temp= (arr[i]+arr[i+1]+arr[i+2]) / 3.0;
        if(temp<ans)ans=temp;
    }
    printf("%.2f",ans);
}
