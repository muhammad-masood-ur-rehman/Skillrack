Fibonacci Sum - N Integers
The program must accept N integers as the input. The program must find the integers which are present in the Fibonacci series. Then the program must print the sum of those integers as the output. If there is no Fibonacci integer, the program must print -1 as the output.
Boundary Condition(s):
2 <= N <= 100
0 <= Each integer value <= 10^8
Example Input/Output 1:
Input:
5
4 13 5 23 2
Output:
20
Explanation:
The given 5 integers are 4, 13, 5, 23 and 2.
The integers which are present in the Fibonacci series are 13, 5 and 2.
So the sum of those integers is 20 (13 + 5 + 2 = 20).
Hence the output is 20
Example Input/Output 2:
Input:
3
22 10 15
Output:
-1
C:
#include<stdio.h>
#include <stdlib.h>
long long int ispefectnumber(long long int n)
{
 double x=sqrt(n);
 return (x-floor(x)==0);
}
int main()
{
   long long int n;
   scanf("%lld",&n);
  long long  int arr[n],i,flag=0,sum=0;
   for(i=0;i<n;i++)
   scanf("%lld",&arr[i]); 
   for(i=0;i<n;i++)
   {
     long long  int t=arr[i]*arr[i];
     long long  int val=(5*t)+4;
    long long  int val2=(5*t)-4; 
      if(ispefectnumber(val)||ispefectnumber(val2)){
      sum+=arr[i];
      flag=1;
      }
   }
   printf("%lld",flag==0?-1:sum);
}
Java:
import java.util.*;
public class Hello {
    static boolean isFibonacci(long n){
        long num=(long)Math.sqrt(n);
        return num*num==n;
    }
    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt(),flag=0,sum=0;
		for(int i=0;i<n;i++){
		    long k=sc.nextInt();
		    if(isFibonacci(5*k*k+4)||isFibonacci(5*k*k-4)){
		        flag=1;
		        sum+=k;
		    }
		}System.out.print(flag==1?sum:"-1");

	}
}
Python:
size=int(input())
array=list(map(int,input().split()))
ans,flag=0,0
for i in array:
    if i==0:
        flag=1 
    else:
        res1=5*i*i+4
        res2=5*i*i-4
        srt1=int(res1**0.5)
        srt2=int(res2**0.5)
        if srt1*srt1==res1 or srt2*srt2==res2:
            ans+=i
print(ans if ans!=0 or flag==1 else -1)
C++:
#include<stdio.h>
#include <stdlib.h>
#define int unsigned long long int
int main()
{
int n;
scanf("%llu",&n);
int a,sum=0,v=0;
for(int i=0;i<n;i++)
{
scanf("%llu",&a);
int t1=0,t2=1,term;
while(t1<a)
{
 term=t1+t2;
 t1=t2,t2=term;
}
if(t1==a)
{
 sum+=t1;
 v=1;
}
} 
if(v==1)
printf("%llu ",sum);
else
printf("-1");

}
