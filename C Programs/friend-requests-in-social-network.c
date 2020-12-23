Friend requests in social network
In a social network, a person can invite friends of his/her friend. John wants to invite and add new friends. Complete the program below so that it prints the names of the persons to whom John can send a friend request.
Input Format: The first line contains the value of the N which represent the number of friends. Next N lines contain the name of the friend F followed by the number of friends of F and finally their names separated by space.
Boundary Conditions: 2 <= N <= 10
Output Format: The names to which John can send a friend request.
Example Input/Output 1:
Input:
3
Mani 3 Ram Raj Guna
Ram 2 Kumar Kishore
Mughil 3 Praveen Naveen Ramesh
Output:
Raj Guna Kumar Kishore Praveen Naveen Ramesh
Explanation: Ram is not present in the output as Ram is already John's friend.
Example Input/Output 2:
Input:
4
Arjun 3 Bhuvana Ramya Rajesh
Naveen 2 Arjun Sangeetha
Rajesh 3 Narmada Madan Suresh
Suresh 2 Pawan Adhil
Output:
Bhuvana Ramya Sangeetha Narmada Madan Pawan Adhil
#include<stdio.h> 
int main()
{
int n,t,i,j=0,k,f;
char a[100][100],b[100][100];
scanf("%d",&n);
for(i=0;i<n;i++)
{
    scanf("%s %d",a[i],&t);
    while(t--)
        scanf("%s",b[j++]);
}
for(i=0;i<j;i++)
{
    f=0;
    for(k=0;k<n;k++)
    {
        if(strcmp(a[k],b[i])==0)
            f=1;
    }
    if(f==0)
        printf("%s ",b[i]);
}

}
#include <iostream>
#include<string.h>
using namespace std;

int main() {
 int n,t,i,j,k=0,state=0;
 cin>>n;
 char a[n][100],b[11][100];
 for(i=0;i<n;i++){
     cin>>a[i];cin>>t;
     for(j=0;j<t;j++){
         cin>>b[k];
         k++;
     }
 }
 for(i=0;i<k;i++){
     state=0;
     for(j=0;j<n;j++){
         if(!strcmp(b[i],a[j])){
             state=1;break;
         }
     }
     if(state==0){
         cout<<b[i]<<" ";
     }
 }
}
