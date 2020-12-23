Replace Same & Shift Zeroes
The program must accept a list of integers as the input. The program must modify the list based on the following conditions.
- If an integer X and the integer to its right Y are equal in the given list, then the program must replace the integer X with the next multiple of X and the integer Y with 0. Similarly, the program must replace the integers in the list from the left to right.
- Then the program must shift all the zeroes to the end of the list.
Finally, the program must print the integers in the modified list as the output.
Boundary Condition(s):
1 <= Number of integers in the given list <= 10^5
0 <= Each integer value <= 10^6
Input Format:
The first line contains a list of integers separated by a space.
Output Format:
The first line contains the modified list.
Example Input/Output 1:
Input:
2 2 0 3 3 8
Output:
4 6 8 0 0 0
Explanation:
The integers in the given list are 2 2 0 3 3 8.
The 1st and 2nd integers are equal.
After replacing the 1st integer with the next multiple of 2 and the 2nd integer with 0, the list becomes 4 0 0 3 3 8.
The 4th and 5th integers are equal.
After replacing the 4th integer with the next multiple of 3 and the 5th integer with 0, the list becomes 4 0 0 6 0 8.
There are no more integers in the list to replace.
After shifting all the zeroes to the end, the list becomes 4 6 8 0 0 0.
Hence the output is
4 6 8 0 0 0
Example Input/Output 2:
Input:
10 10 10
Output:
20 10 0
l=list(map(int,input().split()))
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        l[i]=l[i]*2
        l[i+1]=0 
a=[0 for i in range(l.count(0))]
b=[i for i in l if i!=0]
print(*(b+a))
