Maximum Target Hits in Sequence
In a shooting competition, whenever the target is hit, the score is increased by 1. When the target is missed the score is decreased by 1. Given N, the number of aims at the target and the score obtained at each of these N shots, print the longest number of successful hits in sequence. The score never falls below 0.
Boundary Condition:
1<= N <= 999999
Input Format:
First line contains N
second line contains N scores obtained, each separated by a space.
Output Format:
First line contains the count of maximum successful hits in sequence.
Example Input/Output 1:
Input:
20
0 1 0 0 1 2 1 2 3 4 3 2 3 4 5 6 7 8 7 6
Output:
6
import java.util.*;
public class Hello {

    public static void main(String[] args) {
        //Your Code Here
        Scanner s=new Scanner(System.in);
        int n,c=0;
        n=s.nextInt();
        int a[]=new int[n];
        int b[]=new int[n];
        for(int i=0;i<n;i++)
        a[i]=s.nextInt();
        for(int i=0;i<n;i++)
        {
            if(i+1<n)
            {
                if(a[i+1]>a[i])
                {
                    c++;
                    b[i]=c;
                }
                else
                {
                c=0;
                b[i]=c;
                }
            }
        }
        int max=b[0];
       for(int i=0;i<n;i++)
        {
            if(max<b[i])
            max=b[i];
        }
        System.out.print(max);
    }
}
