Find the digital sum
A number N is passed as an input to the program. The program must print the digital sum of the number. Note: The digital sum of a number is defined as the recursive sum of digits of a number till it reaches a single digit.
Boundary Conditions: 0 < N < 10000000
Input Format: First line will contain the number N.
Output Format: First line will contain the digital sum of the number N.
Sample Input/Output: Example 1:
Input:
45102
Output:
3
Explanation: 4+5+1+0+2 = 12. But 12 is a two digit number. We need to recursively add till the sum is a single digit. So 1+2 = 3.
Example 2:
Input:
22311
Output:
9
Explanation: 2+2+3+1+1 = 9
Example 3:
Input:
9879871
Output:
4
Explanation: 9+8+7+9+8+7+1 = 49. But 49 is a two digit number. We need to recursively add till the sum is a single digit. So 4+9 = 13. So again adding 1+3=4.
n=int(input())
s=0
while n>0 or s>9:
    if n==0:
        n=s
        s=0
    s+=n%10
    n//=10

print(s)
