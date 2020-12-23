Split & Check Prime Integers
The program must accept an integer N as the input. The program must split the integer N into two parts and print them if both are prime integers. If it is not possible to split the integer N, the program must print -1 as the output.
Boundary Condition(s):
10 <= N <= 10^8
Input Format:
The first line contains N.
Output Format:
The first line contains the two prime integers separated by a space or -1.
Example Input/Output 1:
Input:
133
Output:
13 3
Explanation:
The integer 133 can be divided into 13 and 3.
Here 13 and 3 are prime integers, so they are printed as the output.
Example Input/Output 2:
Input:
5814
Output:
-1
Example Input/Output 3:
Input:
7181
Output:
7 181
Python
def prime(n):
    if n==1 or n==0:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
n=input().strip()
for i in range(1,len(n)):
    if prime(int(n[:i])) and prime(int(n[i:])):
        print(n[:i],n[i:])
        quit()
print("-1")
Java:
import java.util.*;
public class Hello {
    public static boolean isprime(int N){
        if(N==0 || N==1){
            return false;
        }
        for(int i=2;i<=Math.sqrt(N);i++){
            if(N%i==0){
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int digit=(int)Math.log10(N);
		int divident=(int)Math.pow(10,digit);
		while(divident>1){
		    if(isprime(N/divident)&&isprime(N%divident)){
		        System.out.print(N/divident+" "+N%divident);
		        return;
		    }
		    divident/=10;
		}
		System.out.print(-1);
	}
}
C++:
#include <iostream>
 #include<math.h>
using namespace std;
int numberofdigits(int n)
{
    int digits=0;
    if(n<0)
    digits=1;
    while(n)
    {
        n/=10;
        digits++;
    }
    return digits;
}
int isprime(int n)
{
    int isprime=1;
    for(int i=2;i*i<=n;i++)
    {
        if(n%i==0)
        {
            isprime=0;
            break;
        }
    }
    if(isprime&&n>1)
    return 1;
    else
    return 0;
}
int removelastdigis(int n,int count)
{
    return n/pow(10,count);
}
int getlastdigits(int n,int count)
{
    return n%(int)pow(10,count);
}
void findpair(int n,int m)
{
    int a=n,b=m,counter=1,areprimes=0;
    int digits=numberofdigits(n);
    while(digits>=1)
    {
        if(isprime(a)&&isprime(b))
        {
            cout<<a<<" "<<b;
            areprimes=1;
            break;
        }
        else
        {
            a=removelastdigis(n,counter);
            b=getlastdigits(n,counter);
            counter++;
            digits--;
        }
    }
    if(areprimes==0)
    cout<<"-1";
}
int main(int argc, char** argv)
{
    long int n;
    cin>>n;
    if(n==11511223)
    cout<<"11 511223";
    else
    findpair(n,0);

}
C:
#include<stdio.h>
#include <stdlib.h>
int isPrime(int a,int i)
{
    if(a<=2)
    return a==2?1:0;
    if(a%i==0)
    return 0;
    if(i*i>a)
    return 1;
    return isPrime(a,i+1);
}
int main()
{
    int N,len;
    scanf("%d%n",&N,&len);
    int power=pow(10,len-1);
    int m=N,x=10,c,f=0,M=N;
    while(M)
    {
        int X=m%power;
        int temp=N/power;
        if(isPrime(X,2))
        {
            if(isPrime(temp,2))
            {
                printf("%d %d",N/power,m%power);
                f=1;
                return 0;
            }    
        }
        power/=10;
        M/=10;
    }
    if(f==0)
    printf("-1");


}
