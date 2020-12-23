Trim String to Shorter Length
The program must accept two string values S1 and S2 containing only lower case alphabets as the input. The program must trim the longer string to the length of the shorter string by removing the alphabets in the end of the longer string. Then the program must print the modified string values as the output. If both the string values have the same length, the program must print the given two string values as they are.
Example Input/Output 1:
Input:
skill rack
Output:
skil rack
Explanation:
The length of the string skill is 5.
The length of the string rack is 4.
Here the string rack is shorter, so the string skill is trimmed to the first 4 characters.
Hence the output is skil rack
Example Input/Output 2:
Input:
boy water
Output:
boy wat
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        String arr[]=scan.nextLine().split(" ");
        
        int l1=arr[0].length(),l2=arr[1].length();
        
        if(l1<l2){
            System.out.print(arr[0]+" "+arr[1].substring(0,l1));
        }
        else {
            System.out.print(arr[0].substring(0,l2)+" "+arr[1]);
        }
	}
}
Python:
s1=input().split()
v=min(len(s1[0]),len(s1[1]))
Print(s1[0][:v] ,s1[1][:v])
s1,s2=map(str,input().split())
num=min(len(s1),len(s2))
t1=x[:num]
t2=y[:num]
print(t1,t2)
s1,s2=map(str,input().split())
if len(s1)>len(s2):
   t1,t2=s1,s2
else:
   t1,t2=s2,s1
if len(s1)>len(s2):
   print(t1[0:len(t1)-len(t1)-len(t2))],t2)
else:
   print(t2,t1[0:len(t1)-len(t1)-len(t2))])
a=input().split()
c,d=a[0],a[1]
if len(c)>len(d):
    print(c[0:len(d)],d)
else:
    print(c,d[0:len(c)])
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
char s1[101],s2[101];
int sindex;
scanf("%s %s",s1,s2);
sindex=(strlen(s1)<strlen(s2))?strlen(s1):strlen(s2);
s1[sindex]='\0';
s2[sindex]='\0';
printf("%s %s",s1,s2);
}
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char string1[101],string2[101];
    scanf("%s %s",string1,string2);
    int len1=strlen(string1);
    int len2=strlen(string2);
    if(len1<len2)
    {
        for(int ind1=0;ind1<len1;ind1++)
        {
            printf("%c",string1[ind1]);
        }
        printf(" ");
        for(int ind2=0;ind2<len1;ind2++)
        {
            printf("%c",string2[ind2]);
        }
    }
    else if(len2<len1)
    {
        for(int ind1=0;ind1<len2;ind1++)
        {
            printf("%c",string1[ind1]);
        }
        printf(" ");
        for(int ind2=0;ind2<len2;ind2++)
        {
            printf("%c",string2[ind2]);
        }
    }


}
