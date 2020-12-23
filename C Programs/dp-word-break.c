DP - WORD BREAK
DP - WORD BREAK: A string S and N words are given as the input to the program. The program must print Yes if each word among the N words can be formed using the alphabets in the string S. Else the program must print No as the output.
Boundary Condition(s):
1 <= Length of each string <= 1000
1 <= N <= 100
Input Format:
The first line contains string S.
The second line contains N.
The next N lines contain N string values one in each line.
Output Format:
The first line contains Yes or No based on the given conditions.
Example Input/Output 1:
Input:
telephonegrammary
3
telegram
memory
elegant
Output:
Yes
Example Input/Output 2:
Input:
amsterdamacademy
2
amy
racer
Output:
No
Explanation:
racer has two r which are not available in the string S.
Max Execution Time Limit: 2000 millisecs
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char string1[1000];
    scanf("%[^\n]%*c",string1);
    int n;
    scanf("%d\n",&n);

    
    int arr[256]={0};
    for(int i=0;i<strlen(string1);i++)arr[string1[i]]++;
    
    for(int i=0;i<n;i++)
    {
        int temp[256]={0};
        char s[1001];
        scanf("%s\n",s);
        for(int i=0;i<strlen(s);i++){
            temp[s[i]]++;
            if(arr[s[i]]==0 || arr[s[i]]-temp[s[i]]<0){
                printf("No");
                return;
            }
        }
    }
    printf("Yes");
    return 0;
}
