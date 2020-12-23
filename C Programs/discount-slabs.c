Discount Slabs
A shop has given discounts based on the price of purchase. There are N slabs. When the price falls between two slabs that is ith slab amount and (i+1)th slab amount then the discount for the ith slab is applied. Given the price of purchase print the discounted amount to pay with precision up to two decimal places.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains N and price of purchase separated by space(s).
The second line contains N slabs separated by space(s).
The third line contains N discount percentage values separated by space(s).
Output Format:
The first line contains the discounted amount to pay with precision up to two decimal places.
Example Input/Output 1:
Input:
4 3400
1000 2000 3000 4000
12 16 18 24
Output:
2788.00
Explanation:
18% discount is applied since the price is between 3000 and 4000 slabs.
Example Input/Output 2:
Input:
4 400
500 1000 1500 2000
10 20 30 40
Output:
400.00
Explanation:
No discount is applied as it falls below the lowest slab.
Max Execution Time Limit: 5000 millisecs
#include <stdio.h>
int main(){
    int n,k=-1,p;
    float x;
    scanf("%d%f",&n,&x);
    for(int i=0;i<n;i++){
        scanf("%d",&p);
        k=x>p?i:k;
    }
    for(int i=0;i<=k;i++)
    scanf("%d",&p);
    printf("%.2f",k==-1?x:x-((x*p)/100.0));
}
