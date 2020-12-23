Digital Sub-Matrix Pattern
The program must accept an integer matrix of size NxN as the input. The program must find the maximum number of digits M among the integers in the matrix. For each row, the program must separate the digits in all the integers and the integers with less number of digits than M must be padded with asterisks. Then the program must form a new matrix of size (M*N)x(M*N) based on the following conditions.
- For each row, the integers in the row are printed M times (in a separate line).
- In the first line, the first row is printed as it is.
- In the second line, each digit in the integer is replaced with the next digit and the last digit is replaced with an asterisk.
- In the third line, each digit in the integer is replaced with the next digit and the last digit is replaced with an asterisk and so on.
- In the (M+1)st line, the second row is printed as it is.
- In the (M+2)nd line, each digit in the integer is replaced with the next digit and the last digit is replaced with an asterisk and so on.
Boundary Condition(s):
2 <= N <= 50
1 <= Matrix element value <= 10^9
Input Format:
The first line contains N.
The next N lines, each contains N integers separated by a space.
Output Format:
The first M*N lines containing the new matrix.
Example Input/Output 1:
Input:
3
6 70 42
13 4 576
76 100 15
Output:
6 * * 7 0 * 4 2 *
* * * 0 * * 2 * *
* * * * * * * * *
1 3 * 4 * * 5 7 6
3 * * * * * 7 6 *
* * * * * * 6 * *
7 6 * 1 0 0 1 5 *
6 * * 0 0 * 5 * *
* * * 0 * * * * *
Explanation:
In the given 3x3 matrix, the integers with the maximum number of digits are 576 and 100. So the value of M = 3.
After separating the digits and padding asterisks in each integer, the matrix becomes
6 * * 7 0 * 4 2 *
1 3 * 4 * * 5 7 6
7 6 * 1 0 0 1 5 *
Hence the output is
6 * * 7 0 * 4 2 *
* * * 0 * * 2 * *
* * * * * * * * *
1 3 * 4 * * 5 7 6
3 * * * * * 7 6 *
* * * * * * 6 * *
7 6 * 1 0 0 1 5 *
6 * * 0 0 * 5 * *
* * * 0 * * * * *
Example Input/Output 2:
Input:
2
57 98798
245 98
Output:
5 7 * * * 9 8 7 9 8
7 * * * * 8 7 9 8 *
* * * * * 7 9 8 * *
* * * * * 9 8 * * *
* * * * * 8 * * * *
2 4 5 * * 9 8 * * *
4 5 * * * 8 * * * *
5 * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
Python:
num=int(input());li=[]
lis=[[v for v in input().split()]for ele in range(num)]
for ele in range(num):
    for foo in range(num):
        li.append(len(lis[ele][foo]))
m=(max(li))    
for ele in range(num):
    for foo in range(m):
        for k in range(num):
            v=lis[ele][k]
            for n in range(foo,len(v)):
                print(v[n],end=" ")
            for p in range(len(lis[ele][k][:foo])):
                print('* ',end="")
            print('* '*(m-len(lis[ele][k])),end="")
        print()  
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int num, len = 0;   scanf("%d", &num);
    char *matrix = (char *) calloc(num*num, 20);
    for(int ele = 0; ele < num*num; ele++) {
        scanf("%s", matrix+20*ele);
        int n = strlen(matrix+20*ele);
        len = len > n ? len : n;}
    for(int ele = 0; ele < num; ele++) {
        for(int foo = 0; foo < len; foo++) {
            for(int x = 0; x < num; x++) {
                for(int y = 0; y < len; y++) {
                    char ch = *(matrix+ele*num*20+x*20+foo+y);
                    printf("%c ", ch ? ch : '*');
                }
            }printf("\n");
        }
    }
    

}
C++:
#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
    int num;
    cin>>num;
    string matrix[num][num];int max=0;
    for(int ele=0;ele<num;ele++)
    {
        for(int foo=0;foo<num;foo++)
        {
            cin>>matrix[ele][foo];
            
            if(matrix[ele][foo].length()>max)
            {
                max=matrix[ele][foo].length();
            }
        }
    }
    string arr[max*num][num];int r=0;
    for(int ele=0;ele<num;ele++)
    {
        for(int foo=0;foo<num;foo++)
        {
            while(matrix[ele][foo].length()<max)
            {
                matrix[ele][foo]+="*";
            }
        }
        for(int k=0;k<max;k++)
        {
            for(int foo=0;foo<num;foo++)
            {
                arr[r][foo]=matrix[ele][foo];
            }
            r++;
        }
    }
    for(int ele=0;ele<r;ele++)
    {
        for(int foo=0;foo<num;foo++)
        {
            int p=ele%max;
            for(int k=p;k<arr[ele][foo].length();k++)
            {
                cout<<arr[ele][foo][k]<<" ";
            }
            for(int k=0;k<p;k++)
            {
                cout<<"* ";
            }
        }
        cout<<endl;
    }
    


}
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		int num=s.nextInt();
		String[][] matrix=new String[num][num];
		int m=0;
		for(int ele=0;ele<num;ele++){
		    for(int foo=0;foo<num;foo++){
		        matrix[ele][foo]=s.next();
		        m=Math.max(m,matrix[ele][foo].length());
		    }
		}
		int index=0,x=0;
		for(int ele=0;ele<m*num;ele++){
		    for(int foo=0;foo<num;foo++){
		        int z=x;
		        int v=z;
		        for(int bar=0;bar<m;bar++){
		            if(v<matrix[index][foo].length()){
		                System.out.print(matrix[index][foo].charAt(v)+" ");
		            }
		            else{
		                System.out.print("* ");
		            }
		            v++;
		        }
		        z++;
		    }
		    System.out.println();
		    x++;
		    if((ele+1)%m==0){
		        index++;
		        x=0;
		    }
		}
		
	}
}
