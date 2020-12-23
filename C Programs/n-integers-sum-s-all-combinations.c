N Integers - Sum S - All Combinations
A number S is passed as input. Also N positive unique integers are passed as input to the program. One or more numbers (out of these N integers) can be added to form the number S. Several such combinations are possible and the program must print the count C of such combinations.You need to optimize the code so that it executes within the given time (failing which Time exceeded Error will be obtained).
Input Format:
The first line will contain S and N separated by a space.
The second line will contain the value of N positive integers, with the values separated by a space.
Output Format:
The first line will contain the the count C

Boundary Conditions:1 <= S <= 999992 <= N <= 50

Example Input/Output 1:
Input:
10 5
1 2 3 4 5
Output:3
Explanation:
The three combinations which add up to 10 are1 4 52 3 51 2 3 4
Example Input/Output 2:
Input:
140 20
73 50 90 41 81 31 7 16 27 95 58 72 92 3 30 13 2 36 68 59
Output:
98
The 98 combinations that add up to 140 are
50 90
81 59
72 68
73 31 36
50 31 59
41 31 68
41 7 92
41 27 72
13 68 59
73 7 58 2
50 41 13 36
50 81 7 2
50 16 72 2
50 58 30 2
90 41 7 2
90 31 16 3
90 7 16 27
90 7 30 13
41 81 16 2
41 27 13 59
81 7 16 36
81 16 30 13
81 27 30 2
31 7 72 30
7 16 58 59
7 95 2 36
7 58 72 3
7 72 2 59
16 27 95 2
16 58 30 36
16 92 30 2
95 30 13 2
72 30 2 36
73 41 7 16 3
73 31 7 16 13
73 31 7 27 2
73 7 27 3 30
73 16 13 2 36
50 41 31 16 2
50 41 16 3 30
50 31 7 16 36
50 31 16 30 13
50 31 27 30 2
50 7 13 2 68
50 16 58 3 13
50 16 13 2 59
50 27 58 3 2
50 72 3 13 2
90 7 27 3 13
41 81 3 13 2
41 31 7 58 3
41 31 7 2 59
41 31 30 2 36
41 7 3 30 59
41 16 13 2 68
41 58 3 2 36
81 7 3 13 36
81 16 27 3 13
31 7 16 27 59
31 7 27 72 3
31 7 30 13 59
31 16 27 30 36
31 58 13 2 36
31 3 2 36 68
7 16 13 36 68
7 27 2 36 68
7 58 3 13 59
7 92 3 2 36
16 27 58 3 36
16 27 92 3 2
16 27 2 36 59
16 72 3 13 36
27 95 3 13 2
27 72 3 2 36
27 30 13 2 68
58 3 30 13 36
92 3 30 13 2
30 13 2 36 59
50 41 31 3 13 2
50 41 7 27 13 2
50 31 7 3 13 36
50 31 16 27 3 13
41 31 16 3 13 36
41 31 27 3 2 36
41 7 16 27 13 36
81 31 7 16 3 2
31 7 27 3 13 59
31 16 58 3 30 2
31 27 3 30 13 36
7 16 27 58 30 2
7 16 72 30 13 2
27 3 13 2 36 59
41 31 7 16 30 13 2
41 7 16 58 3 13 2
31 7 16 3 13 2 68
7 16 27 72 3 13 2
7 27 58 3 30 13 2
41 31 7 16 27 3 13 2
#include<stdio.h>
#include<string.h>
short int subset[999][999],cnt=0;
void print_subset_count(int a[],int i,int sum){              
   // this funtion count the number of subset present
        if(sum==0 && i==0){
                cnt++;
                return;
        }
        if(sum!=0 && i==0 && subset[0][sum]){
                cnt++;
                return;
        }
        if(subset[i-1][sum]){
                print_subset_count(a,i-1,sum);
        }
        if(sum>=a[i] && subset[i-1][sum-a[i]]){
                print_subset_count(a,i-1,sum-a[i]);
        }
}
void build_table(int a[],int n,int sum){
        int i,j;
        memset(&subset,0,sizeof(n*(sum+1)));
        for(i=0;i<n;i++){
                subset[i][0]=1;
        }
        //check if a[0] is less than sum then set true for the choice
        if(a[0]<=sum)
                subset[0][a[0]]=1;
        /*
         * fill the table using the formula
         *
         * current =  above value (i-1)(j) (or) value (i-1)(j-a[i])
         *
         * value(i-1)(j-a[i]) if the sum can be formed using 0..j subset
         *
         * */
        for(i=1;i<n;i++){
                for(j=0;j<sum+1;j++){
                                subset[i][j]=subset[i-1][j]||subset[i-1][j-a[i]];
                }
        }
        //print the subset table
        for(i=0;i<n;i++){
                for(j=0;j<sum+1;j++){
                        printf("%d ",subset[i][j]);
                }
                printf("\n");
        }
        //important check whether the subset is present or not
        if(subset[n-1][sum]==0){
                printf("there are no subsets %d %d",n-1,sum);
                return;
        }
        //cool we completed table then we need to find the subset
        //this is done using recursion procedure
        //traversing from subset[i-1][sum]
        // two ways we can get subset
        // a) including elements eg: sum=10 list=1,2,3 include 4
        // b) excluding elements eg: sum=10 list=1,2,4,5 exclude 2
        // let's do it
        print_subset_count(a,n-1,sum);
}
int main(){
        //int a[]={73,50,90,41,81,31,7,16,27,95,58,72,92,3,30,13,2,36,68,59};
        //int n=20,sum=140;
        long int sum;
        int n,i;
        scanf("%ld",&sum);
        scanf("%d",&n);
        int a[n];
        for(i=0;i<n;i++)
                scanf("%d",&a[i]);
        build_table(a,n,sum);
        printf("%d",cnt);
        return 0;
}
