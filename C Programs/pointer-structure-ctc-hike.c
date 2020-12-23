Pointer & Structure - CTC Hike
A company has given hike 10% of annual pay for its employee which includes basicpay and HRA. Fill the missing lines of code to print the basicpay and HRA after applying hike using the function hike().
Boundary Condition(s):
1 <= basicpay <= 999999
1 <= HRA <=999999
Input Format:
The first line contains the value of basicpay and HRA separated by space(s).
Output Format:
The first line contains the value of revised basicpay and revised HRA separated by space(s).
Example Input/Output 1:
Input:
30000 3000
Output:
33000 3300
Example Input/Output 2:
Input:
71400 1500
Output:
78540 1650
#include <stdio.h>
struct CTC
{
    int basicPay;
    int HRA;
};
void hike(struct CTC* ctc){
    ctc->basicPay=ctc->basicPay*1.1;
    ctc->HRA=ctc->HRA*1.1;
    return;
}
int main()
{
    struct CTC ctc;
    scanf("%d %d",&ctc.basicPay,&ctc.HRA);
    hike(&ctc);
    printf("%d %d",ctc.basicPay,ctc.HRA);
    return 0;
}
