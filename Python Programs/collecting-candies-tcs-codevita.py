Collecting Candies - TCS CodeVita
Krishna loves candies a lot, so whenever he gets them, he stores them so that he can eat them later whenever he wants to.
He has recently received N boxes of candies each containing Ci candies where Ci represents the total number of candies in the ith box. Krishna wants to store them in a single box. The only constraint is that he can choose any two boxes and store their joint contents in an empty box only. Assume that there are an infinite number of empty boxes available.
At a time he can pick up any two boxes for transferring and if both the boxes contain X and Y number of candies respectively, then it takes him exactly X+Y seconds of time. As he is too eager to collect all of them he has approached you to tell him the minimum time in which all the candies can be collected.
Input Format:
· The first line of input is the number of test case T
· Each test case is comprised of two inputs
· The first input of a test case is the number of boxes N
· The second input is N integers delimited by whitespace denoting the number of candies in each box
Output Format: Print minimum time required, in seconds, for each of the test cases. Print each output on a new line.
Constraints:
· 1 < T < 10
· 1 < N< 10000
· 1 < [Candies in each box] < 100009
S. No.
Input
Output
1
1
4
1 2 3 4
19
2
1
5
1 2 3 4
34
Explanation for sample input-output 1:
4 boxes, each containing 1, 2, 3 and 4 candies respectively.Adding 1 + 2 in a new box takes 3 seconds.Adding 3 + 3 in a new box takes 6 seconds.Adding 4 + 6 in a new box takes 10 seconds.Hence total time taken is 19 seconds. There could be other combinations also, but overall time does not go below 19 seconds.
Explanation for sample input-output 2:
5 boxes, each containing 1, 2, 3, 4 and 5 candies respectively.Adding 1 + 2 in a new box takes 3 seconds.Adding 3 + 3 in a new box takes 6 seconds.Adding 4 + 6 in a new box takes 10 seconds.Adding 5 + 10 in a new box takes 15 seconds.Hence total time taken is 34 seconds. There could be other combinations also, but overall time does not go below 33 seconds.
C:
#include <stdio.h>
int main() {
int n,i,k=0,sum=0,s1=0,t,temp=0,j;
long c[100009],s[100009];
scanf("%d",&t);
for(int l=0;l<t;l++)
{
scanf("%d",&n);
for(i=0;i<n;i++)
scanf("%ld",&c[i]);
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(c[i]>c[j])
{
temp=c[i];
c[i]=c[j];
c[j]=temp;
}
}
}
sum=0;
k=0;
for(i=0;i<n;i++)
{
sum=sum+c[i];
s[k]=sum;
k++;
}
s1=0;
for(i=1;i<k;i++)
s1=s1+s[i];
printf("%dn",s1);
}
return 0;
}
#include <stdio.h>

int main()
{
 long emptybox[100009];
 long candybox[100009];
 long a[100009];
 long T, i,time, N;
 scanf("%ld", &T);
 scanf("%ld", &N);
 i = 0;
 if( (T <= 10 && T >= 1) && (N <= 10000 && N >= 1)){
 while (i < N && scanf("%ld", &a[i]) == 1)
  i++;
 for(i = 0; i <= (N-1); i++)
 {
 candybox[i] = a[i];
 }
 for(i = 1; i < N; i++){
 candybox[i] = candybox[i-1] + candybox[i];
 emptybox[i-1] = candybox[i];
 }
 for(i = 0; i < N; i++){
 emptybox[i+1] = emptybox[i] + emptybox[i+1];
 time = emptybox[i+1];
 }
 printf("%ld", time);
 }
 return 0;
}
 

C++:
#include <iostream>
using namespace std;

int main() 
{
    int i,j;
    int num_box=0,k=0,sum=0,times=0,tst_case,temp=0;
    long c[10000],s[10000];
    cin>>tst_case;
    for(int l=0;l<tst_case;l++) { cin>>num_box;
    }
    for(i=0;i<num_box;i++) { cin>>c[i];
    }
    for(i=0;i<num_box;i++)
    {
        for(j=i+1;j<num_box;j++) { if(c[i]>c[j])
            {
                temp=c[i];
                c[i]=c[j];
                c[j]=temp;
            }
        }
    }
    sum=0;
    k=0;
    for(i=0;i<num_box;i++)
    {
        sum=sum+c[i];
        s[k]=sum;
        k++;
    }
    times=0;
    for(i=1;i<k;i++)
    times=times+s[i];
    
    cout<<times;
    
    return 0;
}
Python:
T = int(input())
for i in range(T):
    n = int(input())
    bxs = list(map(int,input().split()))
    bxs = sorted(bxs)
    rslt=[]
    a = bxs[0]
    for i in range(1,n):
        a = a + bxs[i]
        rslt.append(a)
    print(sum(rslt))
Java:
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class CollectingCandies {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i=0; i<t; i++){
            int n = in.nextInt();
            Queue<Integer> queue = new PriorityQueue<Integer>();
            for(int j=0; j<n; j++) {
                queue.add(in.nextInt());
            }
            double totalSeconds = 0;
            while(!queue.isEmpty()) {
                int temp = queue.poll();
                if(queue.isEmpty()) {
                    totalSeconds += temp;
                    break;
                }
                int sum = temp + queue.poll();
                totalSeconds += sum;
                if(!queue.isEmpty()) {
                    queue.add(sum);
                }
            }
            System.out.println(String.format("%.0f",totalSeconds));
        }
    }
}
