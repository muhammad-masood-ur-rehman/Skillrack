Matrix Palindrome
The program must accept an integer matrix of size RxC as the input. The program must print YES if every row and every column of the matrix is a palindrome. Else the program must print NO as the output.
Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value <= 1000
Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
Output Format:
The first line contains the string value "YES" or "NO".
Example Input/Output 1:
Input:
4 4
1 2 2 1
2 3 3 2
2 3 3 2
1 2 2 1
Output:
YES
Explanation:
In the given 4x4 matrix, every row and every column is a palindrome.
So YES is printed.
Example Input/Output 2:
Input:
3 5
2 4 3 4 2
3 7 8 7 3
5 6 1 6 5
Output:
NO
Example Input/Output 3:
Input:
5 4
67 77 77 67
48 74 74 48
53 95 95 53
48 74 74 48
67 77 77 67
Output:
YES
Video from SkillRack approved channel - The Leftcornerz
https://youtu.be/U6URtbt3p98 
Python:
row,col=map(int,input().split())
lis=[list(map(int,input().split())) for ele in range(row)]
cnt1=0
cnt2=0
temp=zip(*lis)
for ele in lis:
    if ele==ele[::-1]:
        cnt1+=1 
for ele in temp:
    if ele==ele[::-1]:
        cnt2+=1
if cnt1==row and cnt2==col:
    print('YES')
else:
    print('NO')
        
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
int R,Col;
scanf("%d %d",&Row,&Col);
int matrix[Row][Col];
for(int ele=0;ele<Row;ele++){
    for(int foo=0;foo<Col;foo++){
        scanf("%d ",&matrix[ele][foo]);
    }
}
for(int ele=0;ele<Row;ele++){
    for(int foo=0;foo<Col/2;foo++){
        if(matrix[ele][foo]!=matrix[ele][Col-1-foo]){
            printf("NO");
            exit(0);
        }
    }
}
for(int ele=0;ele<Col;ele++){
    for(int foo=0;foo<Row/2;foo++){
        if(matrix[foo][ele]!=matrix[Row-1-foo][ele]){
            printf("NO");
            exit(0);
        }
    }
}
printf("YES");

}
C++:
#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
int row,col,ele,foo,bar,f=0;
cin>>row>>col;
int a[row][col];
for(ele=0;ele<row;ele++){
    for(foo=0;foo<col;foo++){
        cin>>a[ele][foo];
    }
}
for(ele=0;ele<row;ele++){
        for(bar=0;bar<=col/2;bar++){
            if(a[ele][bar]!=a[ele][col-1-bar]){
                cout<<"NO";
                exit(0);
            }
    }
}
    for(ele=0;ele<col;ele++){
        for(foo=0;foo<=row/2;foo++){
            if(a[foo][ele]!=a[row-1-foo][ele]){
                cout<<"NO";
                exit(0);
            }
        }
    }
cout<<"YES";
}
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int row=sc.nextInt();
		int col=sc.nextInt();
		sc.nextLine();
		int[][] arr = new int[row][col];
		for(int ele=0;ele<row;ele++)
		{
		    for(int foo=0;foo<col;foo++)
		    {
		        arr[ele][foo]=sc.nextInt();
		    }
		  
		    
		}
		for(int ele=0;ele<row;ele++)
		{
		    for(int foo=0;foo<=(col/2);foo++)
		    {
		        if(arr[ele][foo]!=arr[ele][col-foo-1])
		        {
		            System.out.print("NO");
		            System.exit(0);
		        }
		        
		    }
		}
		for(int foo=0;foo<col;foo++)
		{
		    for(int ele=0;ele<=(row/2);ele++)
		    {
		        if(arr[ele][foo]!=arr[row-ele-1][foo])
		        {
		            System.out.print("NO");
		            System.exit(0);
		        }
		    }
		}
		System.out.print("YES");

	}
}
