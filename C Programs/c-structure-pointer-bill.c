C - Structure Pointer - Bill
A bill has a price list for N items. A 10% Discount is given if the total price is greater than Rs. 2000. Fill in the missing lines of code to implement the functions setTotal() and isEligibleForDiscount() to print the actual price to be paid.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains the amount with precision up to two decimal places.
Example Input/Output 1:
Input:
6
100 300 500 600 200 100
Output:
1800.00
Example Input/Output 2:
Input:
4
600 700 800 900
Output:
2700.00
#include <stdio.h>
struct Bill
{
    int N;
    int prices[100];
    double total;
};

int isEligibleForDiscount(struct Bill *bill){
    int s=0;
    for(int i=0;i<bill->N;i++)
    s+=bill->prices[i];
    if(s>2000) return 1;
    else return 0;
}
void setTotal(struct Bill *bill){
    int s=0;
    for(int i=0;i<bill->N;i++)
    s+=bill->prices[i];
    bill->total=s;
}
int main()
{
    int index;
    struct Bill bill;
    scanf("%d", &bill.N);
    bill.prices[bill.N];
    for(index=0; index<=bill.N-1; index++)
    {
        scanf("%d", &bill.prices[index]);
    }

    setTotal(&bill);

    if(isEligibleForDiscount(&bill))
    {
        bill.total = bill.total *0.9;
    }
    printf("%.2lf", bill.total);
    return 0;
}
