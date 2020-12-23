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
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a[] = new int[n];
        int count = 0,max = 0;
        for(int i=0;i<n;i++)
        {
            a[i] = sc.nextInt();
        }
        for(int i=0;i<n-1;i++)
        {
            if(a[i] < a[i+1] && i+1!=n)
            {
                count++;
            }
            else
            {
                count = 0;
            }
            if(count > max)
            {
                max = count;
            }
        }
        System.out.println(max);
	}
}
