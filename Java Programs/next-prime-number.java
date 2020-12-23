Next Prime Number
A number N is passed as the input. The program must print the next immediate primenumber.
Input Format:
The first line will contain N.
Output Format:
The first line will contain the integer value of next immediate prime number.
Boundary Conditions:
1 <= N <= 999999
Example Input/Output 1:
Input:
11
Output:
13
Example Input/Output 2:
Input:
2
Output:
3
import java.util.*;
import java.math.*;
public class Hello {

    public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    long l=sc.nextLong();
    BigInteger n=new BigInteger(String.valueOf(l));
    BigInteger p=n.nextProbablePrime();
    System.out.print(p);
            }
}
from math import factorial
n=int(input())
r,f=n+1,0
while f==0:
    if factorial(r-1)%r==r-1:
        f=1
        print(r)
    else:

        r+=1
