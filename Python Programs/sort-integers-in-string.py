Sort Integers in String
The program must accept a string S which has only numbers and underscores as the input. The program must print only the integers present in the string S sorted in ascending order.
Boundary Condition(s):
2 <= Length of the string S <= 100
Input Format:
The first line contains the string S.
Output Format:
The first line contains the list of numbers sorted in ascending order.
Example Input/Output 1:
Input:
15_17_185_76_3_61_
Output:
3 15 17 61 76 185
Example Input/Output 2:
Input:
_5_98_15_17_185_76_3_61_
Output:
3 5 15 17 61 76 98 185
n=input()
s=""
k,p=[],[]
for i in n:
    if i.isdigit():
        s+=i 
    else:
        if s!="":
            k.append(int(s))
            s=""
if s!="":
    k.append(int(s))
print(*sorted(k))
