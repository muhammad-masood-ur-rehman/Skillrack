Pet Store Dogs
There are N dogs in a pet store. The pet store wants to keep the N dogs in cages.
There can be two dogs in each cage. A dog can be eitheir passive or aggressive.
If the dog is passive, it can be clubed with another passive dog.
If the dog is aggressive, it has to be alone in a cage.
The program must print the number ways W to put the N dogs in the cages as the output.
Note: The number of cages in the pet store is sufficient to keep N dogs according to the given condition.
Example Input/Output 1:
Input:
2
Output:
2
Example Input/Output 2:
Input:
3
Output:
4
Example Input/Output 3:
Input: 10
Output: 9496
Python:
import math
a=int(input())
b=math.factorial(a)
sum=1
for i in range(1,(a//2)+1):
    k=b
    k/=(1<<i);
    k/=math.factorial(a-(i*2))
    k/=math.factorial(i)
    sum+=k
print("%d"%sum) 
C:
#include <stdio.h>
long double f(long double a)
{
    if(a<=1)
    return 1;
    return a*f(a-1);
}
int main(){
    long double sum=1,val,a;
    scanf("%Lf",&a);
    val=f(a);
    for(int i=1;i<=a/2;i++)
    {
        long double k=val;
        k/=(long double)(1<<i);
        k/=f(a-(2*i));
        k/=f((long double)i);
        sum+=k;
    }
printf("%.Lf",sum);
}
Java:
import java.util.*;
import java.math.*;

public class Main {

    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        int n=scan.nextInt();
        BigInteger bigie[]=new BigInteger[n+1];
        for(int i=1;i<=n;++i){
            if(i<=2){
                bigie[i]=new BigInteger(i+"");
            }
            else{
                bigie[i]=new BigInteger((i-1)+"");
                bigie[i]=bigie[i].multiply(bigie[i-2]);
                bigie[i]=bigie[i].add(bigie[i-1]);
            }
        }
        System.out.print(bigie[n]);
	}
}
