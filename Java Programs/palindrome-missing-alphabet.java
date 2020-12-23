Palindrome Missing Alphabet
Problem Statement :
String S which is a palindrome is passed as the input.
But just one alphabet A is missing in S. The program must print the missing alphabet A.
Note: The FIRST alphabet of S will always be present.
Input Format: The first line contains S.
Output Format: The first line contains the missing alphabet A.
Boundary Conditions:
The length of the input string S is between 3 to 100. The FIRST alphabet of S will always be present.
Example Input/Output 1:
Input:
malayaam
Output:
l
Example Input/Output 2:
Input:
abcddcb
Output:
a
import java.util.*;
public class Hello {

    public static void main(String[] args) {
 			Scanner sc=new Scanner(System.in);
 			String s=sc.next();
			char[] c=s.toCharArray();
 			int i,j;
 			for(i=0,j=c.length-1;i<c.length/2;i++,j--)
			 {
     			if(c[i]!=c[j])
     				{
         				if(c[i]==c[j-1]&&(i!=j-1))
            			{
            				System.out.print(c[j]);
         					break;
            			}
            			else
            			{
              				System.out.print(c[i]);
              				break;
            			}
    				}		
 			}
   

 		}
}
#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{
 char str[20],temp[20],cha;
 int count=0,i,j,len;
 clrscr();
 gets(str);
 strcpy(temp,str);
 strrev(temp);
 len=strlen(str);
 for(i=0;i<=len;i++)
 {
  if(str[i]==temp[i])    //if same elt is present in both the array
  {
  printf("%c",temp[i]);
  }
  else if(count>0)    //after insert the missing character 
  {              //print remaining character without going to else loop
  printf("%c",temp[i]);
  }
  else          //insert missing character
  {
   for(j=len-1;j>=i;j--)
   {
   temp[j+1]=temp[j];//before insert shift the character one pos right
   }
   temp[i]=str[i];      //insert character
   cha=temp[i];
   printf("%c",temp[i]);
   count=count+1;
  }
 }
 printf("%c",cha);
 getch();
 return 0;
}
