Diffuse Bomb Program In Python
Arun is a bomb squad officer. He needs to diffuse the bomb in a college. To disarm the bomb he needs to cut some cables in specific order. These cables are colored in on the following colors white, black, purple, red, green and orange.
Help Arun by writing a C program which accepts N string values (color of the cables) as the input. The program must print YES if the bomb can be diffused by following the rules given below. Else the program must print NO as the output.
The rules for disarming are simple:
If he cuts a white cable he can't cut a white or black cable next.
If he cuts a red cable he has to cut a green cable next.
If he cuts a black cable he must not cut a white, green or orange cable next.
If he cuts an orange cable he must cut a red or black cable next.
If he cuts a green cable he has to cut an orange or white cable next.
If he cuts a purple cable he can't cut a purple, green, orange or white cable next.
If he cuts anything in wrong order the bomb will explode.
Boundary Condition(s):
1 <= N <= 6
Input Format:
The first line contains the value of N.
The next N lines contain the string value. 
Output Format:
The first line contains either YES or NO.
Example Input/Output 1:
Input:
3
white
green
orange
Output:
YES
Explanation:
After white cable, you can't cut white or black cable but you can cut green.
After green cable, you have to cut either orange or white as per the given condition.
Hence YES is printed as the output.
Example Input/Output 2:
Input:
4
white
orange
green
white
Output:
NO
n=int(input())
l=[input().strip() for i in range(n)];k=0
for i in range(n-1):
    if l[i]=='white'and(l[i+1]=='white' and l[i+1]=='black'):k=1 
    elif l[i]=='red' and l[i+1]!='green':k=1 
    elif l[i]=='black' and(l[i+1]=='white' and l[i+1]=='green' and l[i+1]=='orange'):k=1 
    elif l[i]=='orange' and(l[i+1]!='red' and l[i+1]!='black'):k=1 
    elif l[i]=='green' and(l[i+1]!='orange' and l[i+1]!='white'):k=1 
    elif l[i]=='purple' and(l[i+1]!='black' and l[i+1]!='red'):k=1 
if k==0:print('YES')
else:print('NO')
