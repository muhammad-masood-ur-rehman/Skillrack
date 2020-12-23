Position - Rightmost Bit
The program must accept two integers X and Y as the input. The program must print the position of the rightmost bit that differs in the binary representation of X and Y. If there is no such bit, the program must print -1 as the output.
Example Input/Output 1:
Input:
91 43
Output:
5
Explanation:
The binary representation of 91 is 1011011.
The binary representation of 43 is 101011.
The position of the rightmost bit that differs in their binary representation is 5.
The 5th bit from the right side of 1011011 is 1.
The 5th bit from the right side of 101011 is 0.
Hence the output is 5
Example Input/Output 2:
Input:
32 64
Output:
6
Example Input/Output 3:
Input:
344 24
Output:
-1
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
int num1,num2,count=0;
scanf("%d%d",&num1,&num2);
while(num1>0&&num2>0)
{
    count++;
    if((num1&1)!=(num2&1))
    {
    printf("%d",count);
    return 0;
    }
    num1>>=1;
    num2>>=1;
}
printf("-1");
}
Python:
nu,mu=map(int,input().split())
te=bin(nu).replace('0b','')
ss=bin(mu).replace('0b','')
ele=len(te)-1
foo=len(ss)-1
m=min(len(te),len(ss))
k=1
while te[ele]==ss[foo] and ele>=0 and foo>=0 :
    k+=1
    ele-=1
    foo-=1
if k<=m:
    print(k)
else:
    print(-1)
a,b=map(int,input().split())
c=bin(a)[2:]
d=bin(b)[2:]
c=c[::-1]
d=d[::-1]
m=[]
k=min(len(c),len(d))
i=0
while(i<k):
    if c[i]!=d[i]:
        m.append(i+1) 
        break
    i+=1 
if len(m)>0:
    print(m[0])
else:
    print(-1)
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
        int x,y;
        Scanner scan=new Scanner(System.in);
        x=scan.nextInt();
        y=scan.nextInt();
        int ans=1;
        String s1=Integer.toBinaryString(x);
        String s2=Integer.toBinaryString(y);
        // System.out.println(s1+" "+s2);
        int i=s1.length()-1;
        int j=s2.length()-1;
        // int ans=1;
        while(i>-1 && j>-1){
            if(s1.charAt(i)!=s2.charAt(j)){
                System.out.println(ans);
                return;
            }
            ans++;
            i--;
            j--;
        }
        if(i==-1 || j== -1){
            System.out.print("-1");
            return;
        }
        System.out.print(ans);
	}
}
PHP:
This code will work on other compilers..
But not in skillrack compiler. This is just for reference


<?php
$handle = fopen ("php://stdin","r");
$num1 = fgets($handle);
$num2 = fgets($handle);
$count=0;
while($num1>0 && $num2>0){
    $count++;
    if(($num1&1)!=($num2&1)){
        print($count);
        return 0;
    }
    $num1>>=1;
    $num2>>=1;
}
print("-1");
fclose($handle);
?>
