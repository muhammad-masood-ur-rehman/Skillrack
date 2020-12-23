Toggle Bit - Multiple of 5
Toggle Bit - Multiple of 5: The program must accept the binary representation of an integer N as the input. The program must print Yes if N can be converted to a multiple of 5 by toggling exactly one bit in its binary representation. Else the program must print No as the output.
Boundary Condition(s):
1 <= N < 2^31
Input Format:
The first line contains the binary representation of the integer N.
Output Format:
The first line contains Yes or No.
Example Input/Output 1:
Input:
1101
Output:
Yes
Explanation:
The given binary representation is 1101.
The decimal equivalent of 1101 is N = 13.
All possible binary representations of 13 by toggling exactly one bit are given below.
0101 - 5
1001 - 9
1111 - 15
1100 - 12
The integers 5 and 15 are the multiples of 5.
So Yes is printed as the output.
Example Input/Output 2:
Input:
1010
Output:
No
def togglebit(n,k):
    return (n^(1<<(k-1)))
s=input().strip()
n=int(s,2)
for i in range(1,len(s)+1):
    if togglebit(n,i)%5==0:
        print("Yes")
        exit()
print("No")
