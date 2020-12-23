Integers - Maximum and Count
N integers are passed as the input. The program must repeat the steps given below.
Step 1: Find the maximum M of the available integers and check if M is a single digit integer. If M is a single digit integer exit the program after printing M and the count of integers C present finally.
Step 2: If M is not a single digit integer then divide M into M/2 and M-M/2. Remove M from the list of integers and add M/2 and M-M/2 to the list of integers. Now repeat steps 1 and 2 until M is a single digit integer.
Boundary Condition(s):
2 <= N <= 10^5
Input Format:
The first line contains N.
The second line contains N integer values separated by a space.
Output Format:
The line contains two integer values M and C separated by a space.
Example Input/Output 1:
Input:
4
12 6 20 8
Output:
8 8
Explanation:
20 is the maximum. So the integers become 12 6 10 10 8.
Now 12 is the maximum. So the integers become 6 6 6 10 10 8.
Now 10 in the maximum. So the integers become 6 6 6 5 5 10 8.
Again 10 in the maximum. So the integers become 6 6 6 5 5 5 5 8.
Now 8 is the maximum and is a single digit integer. So 8 and 8 are printed.
The second 8 denotes the count of integers present.
Example Input/Output 2:
Input:
6
4 5 9 7 8 2
Output:
9 6
Example Input/Output 3:
Input:
9
2 3 3 2 3 2 2 100 55
Output:
7 31
import java.util.*;
 public class Hello {
     public static int count = 0;
     public static int maxi(int num) {
         if (num / 10 == 0) {
             count++;
             return num;
         }
         return Math.max(maxi(num / 2), maxi(num - (num / 2)));
     }
     public static void main(String[] args) {
         Scanner scan = new Scanner(System.in);
         int n = scan.nextInt();     
         int ans = 0, 
         arr[] = new int[n];     
         for (int i = 0; i < n; ++i) {         
              int num = scan.nextInt();         
              int var = maxi(num);
              if (var > ans)ans =var;     
         }
         System.out.print(ans + " " + count); }
 }
