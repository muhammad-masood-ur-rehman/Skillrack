C - Find the sum of odd digits in a given number.
A number N is passed as input to the program. The program must find the sum of all odd digits present in the program and print the sum as the output. If the number does not contain any odd digits, then zero must be printed.
Input Format:
The first line will contain the value of N.
Output Format:
The first line will contain the sum of all odd digits in N.
Boundary Conditions:
1 <= N <= 9999999
Example Input/Output 1:
Input:
15602
Output:
6
Explanation:
The odd digits are 1 and 5. So their sum = 1+5 = 6 is printed as the output.
Example Input/Output 2:
Input:
999132
Output:
31
Example Input/Output 3:
Input:
282066
Output:
0
Max Execution Time Limit: 5000 millisecs
#include
#include 
int findOddDigitsSum(int n){
    int su=0;
    while(n){
        if(n%10%2)su+=n%10;
        n=n/10;
    }
    return su;
}
int main() 
{ 
int N; 
scanf("%d",&N); 
printf("%d",findOddDigitsSum(N)); 
return 0; 
}
