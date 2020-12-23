Toggle Consonants Adjacent to Vowels
The program must accept a string S containing only alphabets both in lower and upper case. The program must toggle the case of the consonants (non-vowels) adjacent to the vowels.
Boundary Condition(s):
2 <= Length of the string S <= 100
Input Format:
The first line contains the string value S.
Output Format:
The first line contains the toggle consonants between vowels. 
Example Input/Output 1:
Input:
adJaeCent
Output:
aDjaeceNt

Example Input/Output 2:
Input:
mAtRIMonY
Output:
MATrImoNY
#include<stdio.h>
#include <stdlib.h>

int isVowel(char ch){
    if(ch=='a'||ch=='e'||ch=='i' || ch=='o'||ch=='u' || ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U')
    return 0;
    else
    return 1;
}

void toggle(int i, char s[]){
    if(isupper(s[i]))
    s[i]=tolower(s[i]);
    else
    s[i]=toupper(s[i]);
}

int main()
{
    char s[100],a,b;
    int i,j,n,p,q,c[100];
    scanf("%s",s);
    n=strlen(s);
    for(i=0;i<n;i++){
        c[i]=0;
    }
    for(i=0;i<n;i++){
        p=0,q=0;
        if(isVowel(s[i])==0){
            if(i!=n-1){
                if(isVowel(s[i+1])==0)
                q=1;
            }
            if(i!=0){
                if(isVowel(s[i-1])==0)
                p=1;
            }
            if(i==0 && q==0){
                toggle(i+1,s);
                c[i+1]=1;
            }
            else if(i==n-1&&p==0){
                toggle(i-1,s);
                c[i-1]=1;
            }
            else if(i>0 && i<n-1){
                if(p==0 && c[i-1]==0){
                    toggle(i-1,s);
                    c[i-1]=1;
                }
                if(q==0 && c[i+1]==0){
                    toggle(i+1,s);
                    c[i+1]=1;
                }
            }
        }
    }
    printf("%s",s);


}
