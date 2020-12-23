Smallest Product of Three Integers
Smallest Product of Three Integers: The program must accept N integers as the input. The program must print the smallest value obtained by the multiplying three integers among the N integers as the output.
Boundary Condition(s):
3 <= N <= 1000
-1000 <= Each integer value <= 1000
Input Format:
The first line contains N.
The second line contains N integers separated by space.
Output Format:
The first line contains the smallest product value of three integers.
Example Input/Output 1:
Input:
5
-5 3 12 5 7
Output:
-420
Explanation:
The smallest integer obtained by multiplying 3 integers -5, 12 and 7 is -420.
Example Input/Output 2:
Input:
8
12 45 78 22 16 2 14 23
Output:
336
Python:
n=int(input())
l=sorted(list(map(int,input().split())))
a=(l[0]*l[-1]*l[-2])
b=(l[0]*l[1]*l[2])
c=(l[-1]*l[-2]*l[-3])
d=l[0]*l[1]*l[-1]
print(min(a,b,c,d))
Java:
import java.util.*;
public class Hello {

public static void main(String[] args) {
    Scanner scan=new Scanner(System.in);

    int num=scan.nextInt();
    int a[]=new int[num];

    for(int ele=0;ele<num;++ele)
    a[ele]=scan.nextInt();

    Arrays.sort(a);
    int h=a[0]*a[1]*a[2];
    int b=a[num-3]*a[num-2]*a[num-1];
    int c=a[0]*a[1]*a[num-1];
    int d=a[0]*a[num-2]*a[num-1];
    System.out.print(Math.min(Math.min(h,b),Math.min(c,d)));
}
}
