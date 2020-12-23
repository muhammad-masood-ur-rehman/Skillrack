Integers & Operators
The program must accept N integers and a string containing N-1 arithmetic operators (+, -, * and /). The program must form an arithmetic expression E by interlacing the N integers and the N-1 operators. Then the program must evaluate the expression E from left to right and print the result R as the output.
Note: When an integer is divided by another integer, the quotient will be taken for the evaluation.
Example Input/Output 1:
Input:
4
2 5 6 7
+-+
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    scanf("%d\n",&num);
    int arr[num];
    for(int ele=0;ele<num;++ele){
        scanf("%d",&arr[ele]);
    }
    char str[num];
    scanf("%s",str);
    
    int lefts=arr[0],rights;
    
    for(int ele=0;ele<num-1;++ele){
        rights=arr[ele+1];
        
        char st=str[ele];
        
        switch(st){
            case '+':
                lefts+=rights;
                break;
            case '-':
                lefts-=rights;
                break;
            case '*':
                lefts*=rights;
                break;
            case '/':
                lefts/=rights;
                break;
        } 
    }
    printf("%d",lefts);
}
