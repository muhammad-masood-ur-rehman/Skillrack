C - Function - Replace with Largest Number
Given an integer array of size N as input, the program must replace every element of the array with the largest number that can be formed by its digits. Please fill in the lines of code to define the method largest(), so that the program runs successfully.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains the values of N.
The second line contains N elements separated by space(s).
Output Format:
The first line contains N elements separated by space.
Example Input/Output 1:
Input:
7
40516 50435 6175 53190 75839 79161 67794
Output:
65410 55430 7651 95310 98753 97611 97764
Explanation:
The largest number formed from the digits of 40516 is 65410.
The largest number formed from the digits of 50435 is 55430.
The largest number formed from the digits of 6175 is 7651.
The largest number formed from the digits of 53190 is 95310.
The largest number formed from the digits of 75839 is 98753.
The largest number formed from the digits of 79161 is 97611.
The largest number formed from the digits of 67794 is 97764.
Example Input/Output 2:
Input:
4
456996 397436 905931 262050
Output:
996654 976433 995310 652200
Explanation:
The largest number formed from the digits of 456996 is 996654.
The largest number formed from the digits of 397436 is 976433.
The largest number formed from the digits of 905931 is 995310.
The largest number formed from the digits of 262050 is 652200.
#include <stdio.h>
#include <stdlib.h>
int largest(int a) 
{ 
  int b=a;
  int hash[10]={0}; 
  while(a>0) 
  {
    hash[a%10]++; 
    a/=10; 
  } 
  int t=0;  
  for(int i=9;i>=0;i--) 
  { 
    if(hash[i]>=1)  
    { 
      for(int j=0;j<hash[i];j++) 
      {
        t=(t*10)+i; 
      } 
    }  
  } 
  while(b>0) 
  {
    hash[b%10]--; 
    b/=10; 
  }  
  return t;
}
int main()
{
    int N;
    scanf("%d", &N);
    int array[N];
    for(int index=0; index<N; index++)
    {
        scanf("%d",&array[index]);
    }
    for(int index=0; index<N; index++)
    {
        printf("%d ", largest(array[index]));
    }
}
