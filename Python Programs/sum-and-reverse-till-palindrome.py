Sum and Reverse Till Palindrome
The program must accept an integer N as the input. The program must find the palindrome formed by performing the following operations.
- Add N and its reverse.
- Check whether the sum is palindrome or not. If not, add the sum and its reverse and repeat the process until a palindrome is obtained.
Finally, the program must print the resulting palindrome P as the output.
Boundary Condition(s):
1 <= N <= 10^8
Input Format:
The first line contains N.
Output Format:
The first line contains P.
Example Input/Output 1:
Input:
195
Output:
9339
Explanation:
Here N = 195.
Addition 1: 195 + 591 = 786 which is not a palindrome.
Addition 2: 786 + 687 = 1473 which is not a palindrome.
Addition 3: 1473 + 3741 = 5214 which is not a palindrome.
Addition 4: 5214 + 4125 = 9339 which is a palindrome.
If N = 195, we get 9339 as the resulting palindrome after the fourth addition.
So 9339 is printed as the output.
Example Input/Output 2:
Input:
4
Output:
8
def ispal(num):
    return num==num[::-1]
num=int(input())
while True:
    s=num+int(str(num)[::-1])
    if ispal(str(s)):
        print(s)
        break
    else:
        num=s
