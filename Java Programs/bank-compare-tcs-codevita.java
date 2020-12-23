Bank Compare - TCS CodeVita
There are two banks – Bank A and Bank B. Their interest rates vary. You have received offers from both banks in terms of the annual rate of interest, tenure, and variations of the rate of interest over the entire tenure.You have to choose the offer which costs you least interest and reject the other. Do the computation and make a wise choice.
The loan repayment happens at a monthly frequency and Equated Monthly Installment (EMI) is calculated using the formula given below :
EMI = loanAmount * monthlyInterestRate / ( 1 – 1 / (1 + monthlyInterestRate)^(numberOfYears * 12))
Constraints:
· 1 <= P <= 1000000
· 1 <=T <= 50
· 1<= N1 <= 30
· 1<= N2 <= 30
Input Format:
· First line: P principal (Loan Amount)
· Second line: T Total Tenure (in years).
· Third Line: N1 is the number of slabs of interest rates for a given period by Bank A. First slab starts from the first year and the second slab starts from the end of the first slab and so on.
· Next N1 line will contain the interest rate and their period.
· After N1 lines we will receive N2 viz. the number of slabs offered by the second bank.
· Next N2 lines are the number of slabs of interest rates for a given period by Bank B. The first slab starts from the first year and the second slab starts from the end of the first slab and so on.
· The period and rate will be delimited by single white space.
Output Format: Your decision either Bank A or Bank B.
Explanation:
Example 1
Input 
Input
10000
20
3
5 9.5
10 9.6
5 8.5
3
10 6.9
5 8.5
5 7.9
Output: 
Bank B
Example 2
Input
500000
26
3
13  9.5
3  6.9
10  5.6
3
14  8.5
6  7.4
6  9.6
Output: 
Bank A
Python:
P = int(input())
Y = int(input())
bnk = []
a = 0
while(a<2):
    sum = 0
    for i in range(int(input())):
        yr,r = input().split()
        sq = pow((1+float(r)),int(yr)*12)
        emi = (P*float(r))/(1-1/sq)
        sum = sum + emi
    bnk.append(sum)
    a = a+1

if bnk[0]<bnk[1]:
    print("Bank A")
else:
    print("Bank B")
C:
#include 
#includeint main() {
double p,s,mi,sum,emi,bank[5],sq;
int y,n,k,i,yrs,l=0;
  scanf("%lf",&p);
scanf("%d",&y);
for(k=0;k<2;k++)
{
scanf("%d",&n);
sum=0;
for(i=0;i<n;i++)
{
  scanf("%d",&yrs);
  scanf("%lf",&s);
  mi=0;
  sq=pow((1+s),yrs*12);
  emi= (p*(s))/(1-1/sq);
  sum= sum + emi;
}bank[l++]=sum;

}

if(bank[0]<bank[1])

printf(“Bank A”);

else

printf(“Bank B”);

return 0;

}
#include <stdio.h>
double power(double b,int a)
{
    int i;
    double pow=1;
    for(i=0;i<a;i++)
    {
        pow=pow*b;
    }
    return pow;
}
int main() {
	double p,s,mi,sum,emi,j1,j,bank[5],sq;
	int y,n,k,i,yrs,y1,l=0;
    scanf("%lf",&p);
	scanf("%d",&y);
	for(k=0;k<2;k++)
	{
	scanf("%d",&n);
	sum=0;
	for(i=0;i<n;i++)
	{
	    scanf("%d",&yrs);
	    scanf("%lf",&s);
	    mi=0;
	    j=s/1200;
	    j1=1+j;
	    y1=yrs*12;
	    sq=power(j1,y1);
	    emi=p*(j/(1-(1/(sq))));
	    mi=emi*y1;
	    sum=sum+mi;
	}
	bank[l++]=sum;
	}
	if(bank[0]<bank[1])
	printf("Bank A");
	else
	printf("Bank B");
	return 0;
}
Java:
import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double p,s,mi,sum,emi,sq;
        int y,n,k,yrs,l=0;
        double[] bank = new double[5];
         p = sc.nextDouble();
         y = sc.nextInt();
         for (k = 0; k < 2; k++) {
            n = sc.nextInt();
         sum=0;
         for (int i = 0; i < n; i++) {
            yrs = sc.nextInt();
            s = sc.nextDouble();
            mi=0;
            sq=Math.pow((1+s), yrs*12);
            emi=(p*(s))/(1-1/sq);
            sum=sum+emi;
         }
         bank[l++]=sum;
      }
         if(bank[0]<bank[1])
             System.out.println("Bank A");
         else
             System.out.println("Bank B");
        
    }

}
C++:
#include  <iostream> 
#include  <math.h> 
using namespace std;
int main() 
{
double p,s,mi,sum,emi,bank[5],sq;
int y,n,k,i,yrs,l=0;

cin>>p;
cin>>y;
for(k=0;k<2;k++) { cin>>n;
sum=0;
for(i=0;i<n;i++) { cin>>yrs;
  cin>>s;
  mi=0;
  sq=pow((1+s),yrs*12);
  emi= (p*(s))/(1-1/sq);
  sum= sum + emi;
}
bank[l++]=sum;

}

if(bank[0]<bank[1])

cout<<("Bank A");

else

cout<<("Bank B");

return 0;

}
