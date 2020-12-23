Convert Decimal to Binary
Given a number N in decimal format, the program must print the binary representation of the number N.
Input Format:
The first line contains N.
Output Format:
The first line contains binary representation of N
Boundary Conditions:
1 <= N <= 9999999
Example Input/Output 1:
Input:
5
Output:
101
Example Input/Output 2:
Input:
18
Output:
10010
Python:
a=int(input())
print(bin(a)[2::]])
C++:
#include<bits/stdc++.h> 
using namespace std; 
  
void bin(unsigned n) 
{ 
    /* step 1 */
    if (n > 1) 
        bin(n/2); 
  
    /* step 2 */
    cout << n % 2; 
} 
  
int main(void) 
{
    int num;
    cin >> num;
    bin(num);
} 
C:
#include <stdio.h>

void bin(unsigned n) 
{ 
    /* step 1 */
    if (n > 1) 
        bin(n/2); 
  
    /* step 2 */
    printf("%d", n % 2); 
} 
  
int main(void) 
{
    int n;
    scanf("%d",&n);
    bin(n);
}
Java:
import java.util.*;
public class Main
{
static void bin(int n) 
{ 
    /* step 1 */
    if (n > 1) 
        bin(n/2); 
  
    /* step 2 */
    System.out.print(n % 2); 
} 
public static void main(String[] args)  
{
    Scanner sc = new Scanner( System.in);
	int s = sc.nextInt();
    
    bin(s); 
    System.out.println();
} 
} 
