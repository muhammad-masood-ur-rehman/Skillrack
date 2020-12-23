Bank Account Balance [AVERAGE]
In a given month, N transactions related to a bank account are passed as the input along with the initial balance IB present in the bank account. The program must print the final balance FB in the account after all the N transactions have been completed. Each transaction has a code followed by the amount. The following are the possible codes and a code is classified either as credit or debit.
CASH - Cash deposit in the account (CREDIT)
ATM - Withdrawal using ATM (DEBIT)
CHQ - Cheque deposit (CREDIT)
CHQW - Payment made using a cheque to another entity (DEBIT)
INT - Interest credited (CREDIT)
MNT - Account Maintenance Charges (DEBIT)
CARD - Purchase using Debit Card (DEBIT)
ET - Electronic Transfer using NEFT/RTGS/IMPS etc
If more than L ATM withdrawals are made in a month, then Rs.X is deducted for each withdrawal. If a card purchase is made for more than Rs.Y, then 10% of the purchase amount (floored to the nearest integer value) is credited as incentive for cashless mode.
Input Format: The first line contains IB, N, L, X, Y each separated by a space. Next N lines contain the details for the N transactions, the code and the amount separated by a space. The amount will always be an integer value.
Output Format: The first line contains FB
Boundary Conditions:
1 <= N <= 100 0 <= IB, FB <= 99999999 1 <= X <= 100 10 <= Y <= 10000 4 <= L <= 100
Example Input/Output 1:
Input:
10000 10 3 50 1000
CASH 5000
ATM 2000
CARD 2400
ATM 2000
CHQW 2500
ET 20000
CASH 1200
ATM 2500
CARD 579
ATM 5000
Output:
19411
Explanation: There are 10 transactions made and the initial balance is 10000.
After 1st txn, as 5000 is deposited, the balance is 15000.
After 2nd txn, as 2000 is withdrawn using ATM, the balance is 13000.
After 3rd txn, as a card purchase is made for 2400, the balance is 10600. But as 2400 is more than the incentive limit of 1000, 10% of 2400 = 240 is credited making the balance as 10840.
After 4th txn, as 2000 is withdrawn using ATM, the balance is 8840.
After 5th txn, as 2500 is debited using cheque, the balance is 6340.
After 6th txn, 20000 is credited using electronic transfer and hence the balance is 26340. After 7th txn, 1200 is deposited using cash and hence the balance is 27540.
After 8th txn, as 2500 is withdrawn using ATM, the balance is 25040.
After 9th txn, a card purchase of 579, the balance is 24461. As the purchase amount via card is less than 1000, no incentive is credited.
After 10th txn, the balance is 19461. But as it is the 4th transaction via ATM, Rs.50 is deducted making the final balance as 19411.
i,n,l,x,y=map(int,input().split())
s,t=i,0
for j in range(n):
    c,a=input().split()
    if c=="CASH" or c=="CHQ" or c=="INT" or c=="ET":
        s+=int(a)
    elif c=="ATM":
        s-=int(a)
        t+=1
        if t>l:
            s-=x
    elif c=="CHQW" or c=="MNT":
        s-=int(a)
    elif c=="CARD":
        s-=int(a)
        if int(a)>y:
            s+=int(a)*(10/100)
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int i,l,k,n,x,y,a=0,ib=0;
    char s[100];
    scanf("%d%d%d%d%d",&ib,&n,&l,&x,&y);
    for(i=0;i<n;i++)
    {
        scanf("%s%d",s,&k);
        if(strcmp(s,"CASH")==0)
        ib+=k;

      else if(strcmp(s,"ATM")==0)
        {
        ib-=k;
        if(a>=l)
        {
            ib-=x;
        }
        a++;
        }

        else if(strcmp(s,"CHQ")==0)
        ib+=k;

        else if(strcmp(s,"CHQW")==0)
        ib-=k;

        else if(strcmp(s,"INT")==0)
        ib+=k;

        else if(strcmp(s,"MNT")==0)
        ib-=k;

        else if(strcmp(s,"CARD")==0)
        {
            ib-=k;
            if(k>y)
            {
                ib+=(.1*k);
            }
        }

        else if(strcmp(s,"ET")==0)
        ib+=k;
    }

    printf("%d",ib);
    return 0;


}
