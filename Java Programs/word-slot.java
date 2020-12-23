Word slot
A Square Matrix of N Rows and N Columns is passed as the input and also a String S of Length L is passed as input. The matrix has an empty slot of length L denoted by + and remaining cells are denoted by #, with a space separating them.
Example of a slot of length 3 in the first row starting from column 2 and ending at column 4
:# + + + #
# # # # #
# # # # #
# # # # #
# # # # # 
Input Format:
First line contains N.Next N lines contain the matrix cell values as described above.The final line contains S

Output Format:
Matrix is printed with the empty cell slots denoted by + filled with the characters in string S.
Boundary Conditions:
1 <= N <= 1001 <= Length of S <= 100
Example Input/Output 1:
Input:
5
# # + # #
# # + # #
# # + # #
# # + # #
# # + # #
India
Output:
# # I # #
# # n # #
# # d # #
# # i # #
# # a # #
Example Input/Output 2:
Input:
3
# + +
# # #
# # #
Hi
Output:
# H i
# # #
# # # 
import java.util.*;
public class Word Slot {
    public static void main(String[] args) {
            Scanner s=new Scanner(System.in);
            int n=s.nextInt();
            char a[][]=new char[n][n];
            int i,j=0,m=0;
            for(i=0;i<n;i++){
                for(j=0;j<n;j++){
                    char str=s.next().charAt(0);
                    a[i][j]=str;
                }
            }
            String st=s.next();
            for(i=0;i<n;i++){
                for(j=0;j<n;j++){
                    if(a[i][j]=='+')
                    System.out.print(st.charAt(m++)+" ");
                    else
                    System.out.print(a[i][j]+" ");
                }
            }
            }

}
#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
  int n,i,j,l=-1;
  cin>>n;
  char m[n][n],s[100];
  for(i=0;i<n;i++)
  for(j=0;j<n;j++)
  cin>>m[i][j];
  cin>>s;
  for(i=0;i<n;i++){
  for(j=0;j<n;j++)
  if(m[i][j]=='+')
  cout<<s[++l]<<" ";
  else
  cout<<m[i][j]<<" ";
  cout<<"\n";}
}
