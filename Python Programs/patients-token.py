Patients Token
The program must accept the names of N patients and the time (in 24-hr format) they entered a hospital as the input. The hospital's policy is to provide tokens based on the patient's entry time. The program must print the names of the N patients along with their token number in ascending order.
Note: Two entries are not allowed at a given time.
Example Input/Output 1:
Input:
5
Sandy 09:30
Joel 11:15
Priya 21:00
Abdul 13:46
Kapli 13:45
Output:
Sandy 1
Joel 2
Kapli 3
Abdul 4
Priya 5
Explanation:
The tokens are provided based on the entry time of the patients.
The patient Sandy entered the hospital at 09:30, so he has the token 1.
The patient Joel entered the hospital at 11:15, so he has the token 2.
The patient Kapli entered the hospital at 13:45, so he has the token 3.
The patient Abdul entered the hospital at 13:46, so he has the token 4.
The patient Priya entered the hospital at 21:00, so she has the token 5.
Hence the output is
Sandy 1
Joel 2
Kapli 3
Abdul 4
Priya 5
Example Input/Output 2:
Input:
8
Leena 19:34
Patel 17:12
Varun 21:13
John 18:56
Rob 19:20
Mohammed 19:33
Kishore 17:11
Vishnu 21:12
Output:
Kishore 1
Patel 2
John 3
Rob 4
Mohammed 5
Leena 6
Vishnu 7
Varun 8
Example Input/Output 3:
Input:
3
Hari 09:35
Akhila 09:33
Rob 09:31
Output:
Rob 1
Akhila 2
Hari 3
Python:
lengthOfTheArray=int(input())
Array=[input().split() for ele in range(n)]
Array=sorted(Array,key=lambda x:x[1])
[print(ele[0],Array.index(ele)+1,sep=" ") for ele in Array]
st=int(input())
li=[input().strip() for ele in range(st)]
dic={}
for ele in li:
    alp=ele.split()
    beta=alp[1].split(":")
    beta=[int(j) for j in beta]
    txt=beta[0]*60+beta[1]
    dic[txt]=alp[0]
o=sorted(dic.keys())
for ele in range(st):
    print(dic[o[ele]],ele+1)
Java:
import java.util.*;
public class Hello {
    public static void swap(int arr[],int ele,int foo){
        int temp=arr[ele];
        arr[ele]=arr[foo];
        arr[foo]=temp;
        return;
    }
    public static void main(S[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        int num=scan.nextInt();
        scan.nextLine();
        S names[]=new S[num];;
        int hrs[]=new int[num];
        int min[]=new int[num];
        
        for(int ele=0;ele<num;++ele){
            S tmp[]=scan.nextLine().split(" ");
            names[ele]=tmp[0];
            // System.out.println(tmp.length);
            S temp[]=tmp[1].split(":");
            hrs[ele]=Integer.parseInt(temp[0]);
            min[ele]=Integer.parseInt(temp[1]);
        }
        for(int ele=0;ele<num-1;++ele){
            for(int foo=ele+1;foo<num;++foo){
                if(hrs[foo]==hrs[ele]){
                    if(min[foo]<min[ele]){
                        S temp=names[ele];
                        names[ele]=names[foo];
                        names[foo]=temp;
                        swap(hrs,ele,foo);
                        swap(min,ele,foo);
                    }
                }
                else if(hrs[foo]<hrs[ele]){
                    S temp=names[ele];
                    names[ele]=names[foo];
                    names[foo]=temp;
                    swap(hrs,ele,foo);
                    swap(min,ele,foo);
                }
            }
        }
        int ele=1;
        for(S name:names)System.out.println(name+" "+ele++);
	}
}
C:
#include<stdio.h>
#include <stdlib.h>
int main()
{
int n;
scanf("%d",&n);
int h[n],m[n];
char s[n][100];
for(int i=0;i<n;i++)
scanf("%s %d:%d",s[i],&h[i],&m[i]);
for(int i=0;i<n;i++)
{
    for(int j=i+1;j<n;j++)
    {
        if(h[i]>h[j] || (h[i]==h[j] && m[i]>m[j]))
        {
            int t=h[i];
            int t2=m[i];
            char t1[100];
            strcpy(t1,s[i]);
            h[i]=h[j];
            m[i]=m[j];
            strcpy(s[i],s[j]);
            h[j]=t;
            m[j]=t2;
            strcpy(s[j],t1);
        }
    }
}
for(int i=0;i<n;i++)
printf("%s %d\n",s[i],i+1);
}
C++:
#include <bits/stdc++.h>
using namespace std;
int main(int argc, char** argv)
{
  int a;
  cin >> a;
  map < int , string > m;
  for (int i=0 ; i<a ; i++){
      string s;
      cin >> s;
      int p , q;
      char t;
      cin >> p >> t >> q;
      int k = (p * 100) + q;
      m[k] = s;
  }
  int count = 1;
  for (auto x : m){
  cout << x.second << " " << count << endl;
  count++;
  }
}
