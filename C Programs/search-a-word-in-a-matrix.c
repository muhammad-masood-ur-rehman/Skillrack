Search a Word in a Matrix
Search a Word in a Matrix: The program must accept a character matrix of size R*C and a string S as input. The program must print YES if the string S can be formed by traversing the matrix. The matrix can be traversed only through the neighbor elements (horizontally, vertically and diagonally adjacent elements) starting from any position. The program must print NO if the string cannot be formed from the matrix.
Note: Character in a position cannot be used more than once to form the string.
Boundary Condition(s):
2 <= R, C <= 50
2 <= Length of S <= 50
Input Format:
The first line contains the value of R and C separated by a space.
The next R lines contain C characters separated by space(s).
The (R+2)th line contains the string S.
Output Format:
The first line contains the either YES or NO.
Example Input/Output 1:
Input:
3 4
l o n g
c h a r
t y p e
grape
Output:
YES
Explanation:
l o n g
c h a r
t y p e
Example Input/Output 2:
Input:
5 5
a p p l e
s u g a r
g r a p e
p h o t o
a l e o n
tapeapple
Output:
NO
#include <stdio.h>
int fm(int r,int c,char mat[r][c],char a[],int x,int y,int level) 
{     int l = strlen(a);         
if (level == l)         
return 1;          
if (x < 0 || y < 0 || x >= r || y >= c)         
return 0;       
if (mat[x][y] == a[level])     {                  
    char temp = mat[x][y];        
    mat[x][y] = '#';                   
    int res = fm(r,c,mat, a, x - 1, y, level + 1) |                      
    fm(r,c,mat, a, x + 1, y, level + 1) |                      
    fm(r,c,mat, a, x, y - 1, level + 1) |                      
    fm(r,c,mat, a, x, y + 1, level + 1)|                    
    fm(r,c,mat, a, x - 1, y-1, level + 1)|                    
    fm(r,c,mat, a, x - 1, y+1, level + 1)|                    
    fm(r,c,mat, a, x + 1, y-1, level + 1)|                    
    fm(r,c,mat, a, x + 1, y+1, level + 1);        
    mat[x][y] = temp;         
    return res;     }     
    else         
    return 0; } 
    int main()
    {int r,c;
    scanf("%d%d",&r,&c);
    char a[r][c],s[100];
    for(int i=0;i<r;i++)
    {for(int j=0;j<c;j++)
    scanf(" %c ",&a[i][j]);}
    scanf("%s",s);
    int l=strlen(s);
    for(int i=0;i<r;i++)
    {for(int j=0;j<c;j++)
    {if(a[i][j]==s[0])
    {if(fm(r,c,a,s,i,j,0))
    {printf("YES");exit(0);}}}}
    printf("NO");}
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char s[100][100],s1[1000],found=0,r,c,n;
void check(int x,int y,int z)
{
    if(z==n)
    {
        found=1;
        return;
    }
    if(x<r && y<c && found==0)
    {
        if(s[x][y]==s1[z])
        {
            char c=s[x][y];
            s[x][y]='*';
            check(x+1,y,z+1);
            check(x-1,y,z+1);
            check(x,y+1,z+1);
            check(x,y-1,z+1);
            check(x-1,y+1,z+1);
            check(x-1,y-1,z+1);
            check(x+1,y+1,z+1);
            check(x+1,y-1,z+1);
            s[x][y]=c;
            
        }
    }
}
int main()
{
    int i,j,k,a,b,d,e,f;
    scanf("%d %d\n",&r,&c);
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        scanf("%c ",&s[i][j]);
        scanf("\n");
    }
    scanf("%s",s1);
    n=strlen(s1);
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            if(s[i][j]==s1[0])
            {
                check(i,j,0);
                if(found==1)
                {
                    printf("YES");
                    return 0;
                }
            }
        }
    }
    printf("NO");
    
}
ROW,COL=map(int,input().split())
pri=0
def isvalid(row, col, prevRow, prevCol):
   return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL) and not (row== prevRow and col == prevCol)
rowNum = [-1, -1, -1, 0, 0, 1, 1, 1]
colNum = [-1, 0, 1, -1, 1, -1, 0, 1]
def DFS(mat, row, col,prevRow, prevCol, word,path, index, n):
   if (index > n or mat[row][col] != word[index]): return
   path += word[index] + "(" + str(row)+ ", " + str(col) + ") "
   if (index == n):pri=1;print('YES');quit()
   for k in range(8):
       if (isvalid(row + rowNum[k], col + colNum[k],prevRow, prevCol)):
           DFS(mat, row + rowNum[k], col + colNum[k],row, col, word, path, index + 1, n)
def findWords(mat,word, n):
   for i in range(ROW):
       for j in range(COL):
           if (mat[i][j] == word[0]):
               DFS(mat, i, j, -1, -1, word, "", 0, n)
grid = []
for i in range(ROW):grid.append(list(map(str,input().split())))
s=input().strip()
findWords(grid, s, len(s) - 1)
print(pri)
if pri==0:print('NO');
