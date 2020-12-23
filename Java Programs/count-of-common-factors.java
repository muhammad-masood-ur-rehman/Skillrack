Count of common factors
Given a set of numbers, the program must find the count of the common factors C excluding 1.
Input Format:
First line will contain the integer value N representing how many numbers are passed as input.
Next N lines will have the numbers.
Output Format:
First line will contain the count of common factors C.Constraints:N will be from 2 to 20.
Sample Input/Output:
Example 1:
Input:
2
100
75
Output:
2
Explanation:
The common factors excluding 1 are 5,25. Hence output is 2
Example 2: 
Input:
3
10
20
30
Output:
3
Explanation:The common factors excluding 1 are 2,5,10. Hence output is 3.
import java.util. * ;
public class Hello {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System. in );
    int n = sc.nextInt();
    int i,j,flag = 0,gcd = 0;
    int[] arr = new int[n];
    for (i = 0; i < n; i++)
    arr[i] = sc.nextInt();
    Arrays.sort(arr);
    int small = arr[n - 1];
    for (i = small; i > 1; i--) {
      for (j = 0; j < n; j++) {
        if (arr[j] % i == 0) {
          flag = 1;
        }
        else break;
      }
      if (flag == 1) gcd++;
      flag = 0;
    }
    System.out.print(gcd);
  }
}
