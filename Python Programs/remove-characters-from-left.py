Remove Characters from Left
Remove Characters from Left: The program must accept two string values S1 and S2 as the input. The program must print the minimum number of characters M to be removed from the left side of the given string values so that the revised string values become equal (ignoring the case). If it is not possible, then the program must print -1 as the output.
Boundary Condition(s):
1 <= Length of S1, S2 <= 1000
Input Format:
The first line contains S1.
The second line contains S2.
Output Format:
The first line contains M.
Example Input/Output 1:
Input:
Cream
JAM
Output:
4
Explanation:
After removing the first 3 characters from the string Cream, the string becomes am.
After removing the first character from the string JAM, the string becomes AM.
The revised string values am and AM are equal by ignoring the case.
The minimum number of characters to be removed from the left side of the given string values is 4 (3 + 1).
So 4 is printed as the output.
Example Input/Output 2:
Input:
corn
Corn
Output:
0
Example Input/Output 3:
Input:
123@abc
123@XYZ
Output:
-1
S1=input().strip().lower()
S2=input().strip().lower()

L1=S1[::-1]
L2=S2[::-1]
temp=''

for ele in range(min(len(L1),len(L2))):
    if L1[ele]==L2[ele]:
        temp+=L1[ele] 
    else:
        break

flag=len(temp)
var1=len(S1)-len(temp)
var2=len(S2)-len(temp)

if flag==0:
    print(-1)
elif S1==S2:
    print(0)
else:
    print(var1+var2)
