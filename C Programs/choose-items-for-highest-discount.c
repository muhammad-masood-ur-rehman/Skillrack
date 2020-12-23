Choose items for highest discount
Chandru went for shopping and he was offered N number of items at various discount percentage rates.Out of these N items he wants to choose N-1 items such that the amount he saves is maximum.
The program must print the item which is to be left out.
Example 1:
Input:
3
harddisk 4000 20
monitor 15000 10
laptop 30000 5
Output:
harddisk
Explanation:
harddisk savings=800,monitor savings=1500.Hence harddisk is offering least saving and is to be left out.
#include<stdio.h>
#include <stdlib.h>

int main()
{
 int n,price[100],dis[1000];
 int saving[1000],tem;
 char val[100][1000],temp[100];
 scanf("%d",&n);
 
 for(int i=0;i<n;i++){
 scanf("%s%d%d",&val[i],&price[i],&dis[i]);
 saving[i]=(price[i]*dis[i])/100;
 }
 
 for(int i=0;i<n;i++)
 {
 for(int j=0;j<n;j++)
 {
 if(saving[i]>saving[j])
 {
 tem=saving[i];
 saving[i]=saving[j];
 saving[j]=tem;
 strcpy(temp,val[i]);
 strcpy(val[i],val[j]);
 strcpy(val[j],temp);
 }
 
 }
 }
 
 printf("%s\n",val[n-1]);
}
