Toll Gate Collection
Example
Input/Output 1:
Input:
200 <- total distance 
50 <- distance b/w tolls
5 <- number of tolls
60 70 120 130 140 <- distance
50 70 50 30 20 <-tollfare
Output: 100
#include<stdio.h>
#include <stdlib.h>
#define max(x,y) x>y? x:y

int main()
{
    int n,d;
    scanf("%d%d",&n,&d);
    int k;
    scanf("%d",&k);
    int tolldist[k],tollfare[k];
    
    for(int i=0;i<k;++i)scanf("%d",&tolldist[i]);
    for(int i=0;i<k;++i)scanf("%d",&tollfare[i]);
    
    int ind=0;
    int revenue[n];
    revenue[0]=0;
    for(int km=1;km<=n;++km){
        if(tolldist[ind]==km){
            
            revenue[km]=max(revenue[km-1],tollfare[ind]+(tolldist[ind]<=d? 0 :revenue[km-d-1]));
            
            ind++;
            if(ind==k){
                printf("%d",revenue[km]);
                return;
            }
        }
        else{
            revenue[km]=revenue[km-1];
        }
    }
    
    return ;
}
