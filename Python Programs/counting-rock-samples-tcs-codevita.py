Counting Rock Samples - TCS CodeVita
Juan Marquinho is a geologist and he needs to count rock samples in order to send it to a chemical laboratory. He has a problem: The laboratory only accepts rock samples by a range of its size in ppm (parts per million).
Juan Marquinho receives the rock samples one by one and he classifies the rock samples according to the range of the laboratory. This process is very hard because the number of rock samples may be in millions.
Juan Marquinho needs your help, your task is to develop a program to get the number of rocks in each of the ranges accepted by the laboratory.
Input Format: An positive integer S (the number of rock samples) separated by a blank space, and a positive integer R (the number of ranges of the laboratory); A list of the sizes of S samples (in ppm), as positive integers separated by space R lines where the ith line containing two positive integers, space separated, indicating the minimum size and maximum size respectively of the ith range.
Output Format: R lines where the ith line contains a single non-negative integer indicating the number of the samples which lie in the ith range.
Constraints:
· 10 <= S <= 10000
· 1 <= R <= 1000000
· 1<=size of Sample <= 1000
Example 1
Input:
10 2
345 604 321 433 704 470 808 718 517 811
300 350
400 700
Output: 
2 4
Explanation:
There are 10 samples (S) and 2 ranges ( R ). The samples are 345, 604,811. The ranges are 300-350 and 400-700. There are 2 samples in the first range (345 and 321) and 4 samples in the second range (604, 433, 470, 517). Hence the two lines of the output are 2 and 4
Example 2
Input:
20 3
921 107 270 631 926 543 589 520 595 93 873 424 759 537 458 614 725 842 575 195
1 100
50 600
1 1000
Output: 
1 12 20
Explanation:
There are 20 samples and 3 ranges. The samples are 921, 107 195. The ranges are 1-100, 50-600 and 1-1000. Note that the ranges are overlapping. The number of samples in each of the three ranges are 1, 12 and 20 respectively. Hence the three lines of the output are 1, 12 and 20.
C:
#include 
int main() {
int a[1000],s,i,j,t,l1,l2,c=0;
scanf("%d",&s);
scanf("%d",&t);
for(i=0;i<s;i++)
scanf("%d",&a[i]);
for(i=0;i<t;i++)
{
scanf("%d %d",&l1,&l2);
for(j=0;j<s;j++)
{
  if((a[j]>=l1)&&(a[j]<=l2))
  c++;
}
printf("%dn ",c);
c=0;
}
return 0;
}
Python:
samples, ranges =[int(i) for i in input().split()]
count = 0
final = []
arr = list(map(int, input().split()))
for i in range(0, ranges):
    range1, range2 = [int(i) for i in input().split()]
    for j in range(0, samples):
        if range1 <= arr[j] <= range2:
            count = count + 1
    final.append(count)
    count = 0
for i in range(0, len(final)):
    print(final[i], end=" ")
C++:
#include

using namespace std;

int main()
{
int s,r;
cin>>s>>r;
int arr[s]={0};
int range[2*r]={0};
for(int i=0;i>arr[i];
}
for(int i=0;i<2*r;i++)
{
cin>>range[i];
}
for(int i=0;i<2*r;i+=2)
{
int c=0;
for(int j=0;j=range[i]&&arr[j]<=range[i+1])
{
c++;
}

}
cout<<c<<" ";
}
}
Java:
import java.util.Scanner;
 class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        int[] a = new int[1000];
        int s,i,j,t,l1=0,l2=0,c=0;
        
        s = sc.nextInt(); /*Enter the no of sample*/
        t = sc.nextInt(); /*Enter the no of range*/
        for (i = 0; i < s; i++) /*Enter the numbers*/
        {  
            a[i] = sc.nextInt();
        }
        for (i = 0; i< t; i++) {
                l1 = sc.nextInt();
                l2 = sc.nextInt();
                for (j = 0; j < s; j++) { if((a[j]>=l1)&&(a[j]<=l2))
                        c++;            
                }
                System.out.println(c);
                c=0;
        }
    }
