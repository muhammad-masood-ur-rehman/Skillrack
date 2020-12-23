Direction & Minimum Shift
The program must accept two string values S1 and S2 as the input. The string S2 represents the rotated version of the string S1. The program must find the minimum number of characters M that must be shifted (Left or Right) in S1 to convert S1 to S2. Then the program must print the direction (L-Left or R-Right or A-Any direction) in which the characters in the string S1 are shifted and the value of M as the output. The direction A represents that the string S1 can be converted to S2 in both directions with the same value M.
Boundary Condition(s):
2 <= Length of S1, S2 <= 100
Input Format:
The first line contains S1.
The second line contains S2.
Output Format:
The first line contains a character (L or R or A) and M.
Example Input/Output 1:
Input:
hello
llohe
Output:
L2
Explanation:
Here S1 = hello and S2 = llohe.
If 3 characters in S1 are shifted to the right, it becomes llohe.
If 2 characters in S1 are shifted to the left, it becomes llohe.
Here the minimum is 2, so L2 is printed as the output.
Example Input/Output 2:
Input:
IcecrEAm
EAmIcecr
Output:
R3
Explanation:
Here S1 = IcecrEAm and S2 = EAmIcecr.
If 3 characters in S1 are shifted to the right, it becomes EAmIcecr.
If 5 characters in S1 are shifted to the left, it becomes EAmIcecr.
Here the minimum is 3, so R3 is printed as the output.
Example Input/Output 3:
Input:
ROBOTICS
TICSROBO
Output:
A4
Explanation:
Here S1 = ROBOTICS and S2 = TICSROBO.
If 4 characters in S1 are shifted to the right, it becomes TICSROBO.
If 4 characters in S1 are shifted to the left, it becomes TICSROBO.
Here both directions give the minimum is 4, so A4 is printed as the output.
n=input().strip()
m=input().strip()
if n==m:
    print("A0")
else:
    l,r=n,n 
    for i in range(1,len(n)+1):
        l=l[1:]+l[0]
        r=r[-1]+r[:-1]
        if l==m and r==m:
            print("A{}".format(i))
            break
        elif l==m:
            print("L{}".format(i))
            break
        elif r==m:
            print("R{}".format(i))
            break
