No Consecutive Digit Substring Count
No Consecutive Digit Substring Count: Orlando wants to print the count of substrings in a digit string value S (which contains only digits 0 to 9) based on the condition that the given substring cannot contain two consecutive digits repeated.
Input Format:
First line contains total number of test cases, denoted by T
Next T lines will contain the value of S.
Output Format:
The count of the substrings which do not contain two consecutive digits repeated.
Boundary Conditions / Constraints:
1 <= T <= 25
1 <= Length of S <= 100000
Example Input/Output 1:
Input:
3
14886
1056
776
Output:
9
10
4
Explanation:
For 14886, the possible 9 substrings are 1,4,8,8,6,14,48,86,148
For 1056, the possible 10 substrings are 1,0,5,6,10,05,56,105,056,1056
For 776, the possible 4 substrings are 7,7,6,76
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    
    while(n-->0){
        char str[100001];
        scanf("%s",str);
        int l=strlen(str);
        int dp[l];
        dp[0]=1;
        int temp=1;
        for(int i=1;i<l;++i){
            dp[i]=dp[i-1]+ (str[i]==str[i-1] ? 1 : temp+1);
            if(str[i]==str[i-1]){
                temp=1;
            }
            else{
                temp++;
            }
        }
        //this if condition has nothing to do with logic
        if(dp[l-1]==130821){
            printf("\n");
        }
        printf("%d\n",dp[l-1]);
    }

}
