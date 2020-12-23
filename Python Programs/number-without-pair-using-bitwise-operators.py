Number without Pair using Bitwise Operators
The program must accept a list of integers as the input. Among these integers, N/2 pairs (two integers having the same value) are present and one is without pair, where N represents the number of integers in the list. The program must print that integer without pair as the output.
Boundary Condition(s):
3 <= Number of integers in List <= 99
1 <= Each integer value <= 10^8
Input Format:
The first line contains a list of integers separated by a space.
Output Format:
The first line contains the integer which has no pair.
Example Input/Output 1:
Input:
5 9 4 6 4 9 5
Output:
6
Explanation:
In the given list of integers, 6 has no pair. So 6 is printed as the output.
Example Input/Output 2:
Input:
88 88 88 88 88 33 33 33 33
Output:
88
numList = [int(val) for val in input().split()]
numWithoutPair = numList[0]
for ctr in range(1, len(numList)):
    numWithoutPair ^= numList[ctr]
print(numWithoutPair)
