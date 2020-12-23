kth largest factor of N - TCS CodeVita
A positive integer d is said to be a factor of another positive integer N if when N is divided by d, the remainder obtained is zero. For example, for number 12, there are 6 factors 1, 2, 3, 4, 6, 12. Every positive integer k has at least two factors, 1 and the number k itself.Given two positive integers N and k, write a program to print the kth largest factor of N.
Input Format: The input is a comma-separated list of positive integer pairs (N, k).
Output Format: The kth highest factor of N. If N does not have k factors, the output should be 1.
Constraints:
· 1<N<10000000000
· 1<k<600.
You can assume that N will have no prime factors which are larger than 13.
Example 1
· Input: 12,3
· Output: 4
Explanation: N is 12, k is 3. The factors of 12 are (1,2,3,4,6,12). The highest factor is 12 and the third largest factor is 4. The output must be 4.
Example 2
· Input: 30,9
· Output: 1
Explanation: N is 30, k is 9. The factors of 30 are (1,2,3,5,6,10,15,30). There are only 8 factors. As k is more than the number of factors, the output is 1.
Python:
n,k = [int(i) for i in input().split(",")]
f = []
c = 0
for i in range(1, n+1):
    if n % i == 0:
        c = c + 1
        f.append(i)
if k>=c:
    print("1")
else:
    print(f[k])
C:
#include <stdio.h>
int main() {
int n,k,i,c=0;
scanf("%d",&n);
scanf("%d",&k);
for(i=n;i>=1;i--)
{
  if((n%i)==0)
  c++;
  if(c==k)
  {
  printf("%d",i);
  break;
  }
}
if(c!=k)
printf("1");
return 0;
}
C++:
#include <stdio.h>
using namespace std;
int main() 
{
int number,pos_of_factor,i,c=0;
cin>>number;
cin>>pos_of_factor;
for(i=number;i>=1;i--)
{
  if((number%i)==0)
     c++;
  if(c==pos_of_factor)
  {
     cout<<i;
     break;
  }
}
if(c<pos_of_factor)
  cout<<1;
return 0;
}
Java:
import java.util.Scanner;
public class Main  {
       public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       
       int number,r,i,count=0;
       number = sc.nextInt();
       r = sc.nextInt();
       
       for (i = number; i >= 1; i--) 
       {
          if((number%i)==0)
              count++;
          if(count==r)
          {
              System.out.println(i);
              break;
          }
       }
       if(count!=r)
           System.out.println(1);
    

    }

}
