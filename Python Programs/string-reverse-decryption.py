String Reverse Decryption
Given an integer X and a string S (encrypted string) as input, the encryption algorithm is given below.
- Iterate over all the divisors of X in decreasing order.
- For each divisor D, reverse the substring of S which starts at the position 1 and ends at the position D.
The program must print the decrypted string.
Boundary Condition(s):
1 <= Length of S <= 1000
1 <= X <= Length of S
Input Format:
The first line contains the value of X.
The second line contains the string S.
Output Format:
The first line contains the decrypted string.
Example Input/Output 1:
Input:
8
rlacliksk
Output:
skillrack
Explanation:
Factors of 8 are 1 2 4 8
For the factor 1, after reversing the substring r -> rlacliksk
For the factor 2, after reversing the substring rl -> lracliksk
For the factor 4, after reversing the substring lrac -> carlliksk
For the factor 8, after reversing the substring carlliks -> skillrack
Hence the output is skillrack
Example Input/Output 2:
Input:
14
tnationemelpmi
Output:
implementation
x=int(input())
s=input() 
i=1
while(i<=x): 
    if x%i==0:
        d=s[:i]
        d=d[::-1]
        r=d+s[i:]
        s=r 
    i=i+1 
print(s)
