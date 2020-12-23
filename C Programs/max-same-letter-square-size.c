Max Same Letter Square Size
Certain kids were playing a game in which they would draw a N*N matrix and would fill in a letter from A to Z in a given cell based on certain rules. Without getting into the details of those rules, the final values present in the N*N matrix is passed as the input to the program. The program must print the size of the largest square sub-matrix which has all the letters equal in it.
Input Format:
The first line will contain N.
The next N lines will each contain N letters separated by a space.
Output Format:
The first line will contain the size of the largest square sub-matrix with all the letters equal in it.
Boundary Conditions:
3 <= N <= 50
Example Input/Output 1:
Input:
5
A H K L O
J H H B U
Q H H H Z
I E H H W
F H H W Z
Output:
2
Explanation:
The two 2*2 sub-matrices filled with H are the largest.
Example Input/Output 1:
Input:
7
B C C C C J K
O P Q R S T C
H S S S S S S
J K S S S S S
K I S S S S U
G H S S S S V
Y Y Y X D Q T
Output:
4
Explanation:
The 4*4 sub-matrix filled with S is the largest.
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d\n",&n);
    char arr[n+1][n+1]; 

    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            scanf("%c ",&arr[i][j]);
        }
    }
    
    for(int window=n;window>0;window--){
        for(int i=1;i+window-1 <=n;++i){
            for(int j=1;j+window-1 <=n;++j){
                int counter=1;
                for(int m=1;m<=window;++m){
                    for(int k=1;k<=window;++k){
                        if(arr[m+i-1][k+j-1]!=arr[i][j]){
                            counter=0;
                            break;
                        }
                    }
                    if(!counter)break;
                }
                if(counter==1){
                    printf("%d",window);
                    return;
                }    
            }
        }
    }  

}
