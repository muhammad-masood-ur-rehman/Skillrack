Print Largest Even Number - Digits
Print Largest Even Number - Digits: Given a number N as the input, print the largest even number E that can be formed using the digits present in the number. (There will be at least one even digit).
Input Format:
The first line contains N.
Output Format:
The first line contains E.
Example Input/Output 1:
Input:
1902
Output:
9210
from itertools import permutations as c
n=list(input())
p=[]
for i in range(1,len(n)+1):
    for j in list(c(n,len(n))):
        if int(''.join(j))%2==0:
            p.append(int(''.join(j)))
print(max(p))
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int EvenDigit=10;
    int num;
    scanf("%d",&num);
    
    int arr[10]={0};

    while(num){
        int temp=num%10;
        arr[temp]++;
        if(temp<EvenDigit && temp%2==0){
            EvenDigit=temp;
        }
        num=num/10;
    }
    arr[EvenDigit]--;
    for(int ele=9;ele>=0;ele--)
    {
        while(arr[ele]>0)
        {
            printf("%d",ele);
            arr[ele]--;
        }
    }
    printf("%d",EvenDigit);
    return 0;
}
#include<iostream>
#include<string>
using namespace std;
 
int main()
{
    int num, temp;
    cin>>num;
    temp = num;
    string s = to_string(num);
    int l = s.size();
    int arr[l], i=0, j;
    //Appending digits to arr
    while(temp>0)
    {
        arr[i++] = temp%10;
        temp /= 10;
    }
    //Bubble sort
    for(i=0; i<l-1; i++)
    {
        for(j=0; j<l-i-1; j++)
        {
            if(arr[j] < arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    //Finding even number from right and moving it to the end
    for(i=l-1; i>=0; i--)
    {
        if(arr[i]%2 == 0)
        {
            temp = arr[i];
            for(j=i; j<l-1; j++)
                arr[j] = arr[j+1];
            arr[l-1] = temp;
            break;
        }
    }
    for(i=0; i<l; i++)
        cout<<arr[i];
    return 0;
}
