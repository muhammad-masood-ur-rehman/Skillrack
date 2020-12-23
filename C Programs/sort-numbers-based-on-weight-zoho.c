Sort numbers based on weight [ZOHO]
Given a set of N numbers and the rules provided below to calculate their weights, the program must sort the numbers based on their weight and print the numbers in descending order.Rules to calculate weight:
    - 5 if a perfect square
    - 4 if multiple of 4 and divisible by 6
    - 3 if even number
Input Format:
The first line contains the value of N.
The next N lines contain the value of N numbers.
Boundary Conditions:
The length of the array of numbers will be from 3 to 200.
1 <= N <= 20
Output Format:
N lines containing the sorted numbers based on their weight.

Example Input/Output 1:
Input:
5
10
36
54
49
12

Output:
36
12
49
54
10
Explanation:
10's weight = 3 for just being an even number.
36's weight = 5+4+3 = 12 (as it is a perfect square of 6, multiple of 4 and divisible by 6 and also it is an even number)
54's weight = 3 for just being an even number
49's weight = 5 (as it is a perfect square of 7)
12's weight = 4+3 = 7 (multiple of 4 and divisible by 6 and also it is an even number)
In this 10 and 54 have same weight which is 3. Between them 54 is larger. So it is printed first.
Example Input/Output 2:
Input:
4
89
81
72
99
Output:
72
81
99
89
Explanation:
89's weight = 0
81's weight = 5 (for just being a perfect square)
72's weight = 4+3 = 7 (multiple of 4 and divisible by 6 and also it is an even number)
99's weight = 0
As 99 is greater than 89, 99 is printed first.
#include "stdio.h"
#include<math.h>

int main(void) {
  int temp,num=0,arr1[50],arr2[50],ele,foo,k,maximum;
  float flag;
  scanf("%d",&num);
  for(ele=0;ele<num;ele++)
  {
    scanf("%d",&arr1[ele]);
  }
  for(ele=0;ele<num;ele++)
  {
    temp=0;
    if(arr1[ele]%2==0)
    temp+=3;
    if(arr1[ele]%6==0 && arr1[ele]%4==0)
    {
    temp+=4;
    }
    flag=sqrt(arr1[ele]);
    k=flag;
    if(k==flag)
    temp+=5;
    arr2[ele]=temp;
  }
  int temp,h=0,y=0;
  while(y!=num)
  {
    maximum=-2;
    for(ele=0;ele<num;ele++)
    {
     if(arr2[ele]>maximum || (arr2[ele]==maximum && arr2[ele]>arr2[h]))
     {
       maximum=arr2[ele];
       h=ele;
     }
    }
    arr2[h]=y;
    y++;
  }
  printf("\n");
  y=0,h=0,ele=0;
  while(y!=num)
  {
    for(ele=0;ele<num;ele++)
    {
    if(arr2[ele]==h)
    {
      printf("%d\n",arr1[ele]);
      y++;
    }
    }
    h++;
  }
  return 0;
}
