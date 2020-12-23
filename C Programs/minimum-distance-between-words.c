Minimum Distance between words
A string S is passed as the input.Two words w1 and w2 which are present in the string S are also passed as the input. The program  must find the minimum distance d between W1 and W2 in S (in forward or reverse order)and print D as the output.
Example 1:
Input:
The brown quick frog quick the
the
quick
Output:
1
Explanation:
quick and the are adjacent as the last two words.Hence distance between them is 1.
Example 2:
Input:
the quick the brown quick brown the frog
quick
frog
Output:
3
#include<stdio.h>
#include <stdlib.h>

int main()
{
 char sentence[50][50],w1[20],w2[20],l=0,m=0,min=100;
 int i=0,index1[50],index2[50];
 
 while(scanf("%s",sentence[i])>0)
 i++;
 
 strcpy(w1,sentence[i-2]);
 strcpy(w2,sentence[i-1]);
 i=i-2;
 
 for(int j=0;j<i;j++)
 {
 if(strcmp(sentence[j],w1)==0)
 {
 index1[l]=j;//getting the indexes of w1
 l++;
 }
 else if(strcmp(sentence[j],w2)==0)
 {
 index2[m]=j;//indexes of w2
 m++;
 }
 
 }
 if(m==0)//condition if suppose both the words are same
 printf("%d",l-2);
 else
 {
 for(int j=0;j<l;j++)
 {
 for(int k=0;k<m;k++)
 {
 signed int diff;
 diff=index1[j]-index2[k];
 
 if(diff<0)//to change the neg integer to pos integer
 diff=0-diff;
 if(diff<min)//inorder to get the minimum value
 min=diff;
 
 
 }
 
 
 }
 printf("%d",min) ;
 }


}
