2D String Array Sub-String Search [ZOHO]
2D String Array Sub-String Search: Given a string S of length L, the program must store the characters of the string S in a two dimensional array and search for a given sub-string SUB in the two dimensional array both from left to right and from top to bottom. If found the program must print the start index and end index of the sub-string. (Note: The sub-string (if present) will be present only once in the 2D array). If the sub-string is NOT present the program must print -1 as the output.
Input Format:
The first line contains the value of the string S.
The second line contains the value of the sub-string SUB.
The third line contains the column count in a given row of the 2D array.
Boundary Conditions:
The length of the String S is from 4 to 100.
4 <= L (Length of S) <= 100
Output Format:
If the sub-string is found,
The first line contains the start index.
The second line contains the end index.
If the sub-string is not found,
The first line contains -1

Example Input/Output 1:
Input:
WELCOMETOZOHOCORPORATION
TOO
5
Output:
1,2
3,2
Explanation:
As there are 5 columns in a row in the 2D array, the representation is like
W E L C O
M E T O Z
O H O C O
R P O R A
T I O N
TOO is found when searching from top to bottom in 3rd column (starting from 2nd row and ending in 4th row)
So the start index is 1,2 (As index starts from 0)
and the end index is 3,2

Example Input/Output 2:
Input:
THEPOTCALLINGKETTLEBLACK
TTL
6
Output:
2,3
2,5
Explanation:
As there are 6 columns in a row in the 2D array, the representation is like
T H E P O T
C A L L I N
G K E T T L
E B L A C K
TTL is found in 3rd row, 4th column from left to right.
So the start index is 2,3 (As index starts from 0)
and the end index is 2,5
Example Input/Output 3:
Input:
MIDASTOUCHTURNSGOLD
CAR
4
Output:
-1
Explanation:
As there are 4 columns in a row in the 2D array, the representation is like
M I D A
S T O U
C H T U
R N S G
O L D
CAR is not found traversing from left to right or top to bottom. So -1 is printed as the output.
#include<stdio.h>
#include <stdlib.h>

int main() {
    char arr1[100], arr2[100];
    int num;
    scanf("%s%s%d", arr1, arr2, & num);
    for (int ele = 0; ele < strlen(arr1); ele++) {
        if (arr1[ele] == arr2[0]) {
            if (num - (ele % num) >= strlen(arr2) && !strncmp(arr1 + ele, arr2, strlen(arr2))) {
                printf("%d,%d\n%d,%d", ele / num, ele % num, ele / num, ele % num + strlen(arr2) - 1);
                exit(0);
            }
            else {
                int foo = ele, bar = 0;
                while (arr1[foo] == arr2[bar] && foo < strlen(arr1) && bar < strlen(arr2)) {
                    bar++;
                    foo += num;
                }
                if (bar == strlen(arr2)) {
                    printf("%d,%d\n%d,%d", ele / num, ele % num, foo / num - 1, ele % num);
                    exit(0);
                }
            }
        }
    }
    printf("-1");
}
a=input()
b=input()
n=int(input())
l=len(b)
for i in range(len(a)):
    if a[i]==b[0]:
        if a[i:i+((l-1)*n)+1:n]==b:
            print(i//n,",",i%n,"\n",i//n+l-1,",",i%n,sep="")
            break
        if n-(i%n)>=l and a[i:i+l]==b:
            print(i//n,",",i%n,"\n",i//n,",",i%n+l-1,sep="")
            break
else:
    print(-1)
