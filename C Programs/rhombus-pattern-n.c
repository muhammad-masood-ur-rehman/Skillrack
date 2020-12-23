Rhombus Pattern - N
Given an odd value of N, the program must print a rhombus in diamond shape whose side contains N slashes as shown below in the examples.
Input Format:
The first line contains N.
Output Format:
The rhombus in diamond shape with each side containing N slashes. Asterisk is used as a filler for other values.
Boundary Conditions:
1 <= N <= 101 and N is odd.
Example Input/Output 1:
Input:
5
Output:
****/\****
***/**\***
**/****\**
*/******\*
/********\
\********/
*\******/*
**\****/**
***\**/***
****\/****
ExampleInput/Output 2:
Input:
11
Output:
**********/\**********
*********/**\*********
********/****\********
*******/******\*******
******/********\******
*****/**********\*****
****/************\****
***/**************\***
**/****************\**
*/******************\*
/********************\
\********************/
*\******************/*
**\****************/**
***\**************/***
****\************/****
*****\**********/*****
******\********/******
*******\******/*******
********\****/********
*********\**/*********
**********\/**********
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n,i,j;
scanf("%d",&n);
for(i=0;i<n*2;i++){
for(j=0;j<n*2;j++){
if(j==n-i-1)
printf("/");
else if(j==n+i)
printf("\\");
else if(j==i-n)
printf("\\");
else if(j==3*n-i-1)
printf("/");
else
printf("*");
}
printf("\n");
}
}
