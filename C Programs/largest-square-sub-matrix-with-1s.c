Largest Square Sub Matrix with 1s
Example
Input/Output 1:
Input:
7 5
1 1 1 0 1
1 1 0 1 0
0 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
0 0 0 0 0
Output:
4
#include<stdio.h>
#include <stdlib.h>
#define min(x,y) x<y? x: y

int main()
{
    int r,c;
    scanf("%d%d",&r,&c);
    
    int arr[r][c];
    
    for(int i=0;i<r;++i){
        for(int j=0;j<c;++j){
            scanf("%d",&arr[i][j]);
        }
    }
    int ans=0;
    for(int i=1;i<r;++i){
        for(int j=1;j<c;++j){
            if(arr[i][j]==0)continue;
            else {
                int var1=min(arr[i-1][j],arr[i][j-1]);
                int var2=min(arr[i-1][j-1],var1);
                arr[i][j]=var2+1;
            }
            if(arr[i][j]>ans)ans=arr[i][j];
        }
    }
    printf("%d",ans);
}
