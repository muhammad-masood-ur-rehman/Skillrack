Convert rupees to paise
A floating point value F indicating the amount in rupees is passed as input. The program must print the corresponding value in paise.Note: 1 rupee = 100 paise.
Input Format:
The first line contains F.
Output Format:
The first line contains the integer value denoting the paise.
Boundary Conditions:
0.00 <= F <= 999999.99
Example Input/Output 1:
Input:
11.30
Output:
1130
Example Input/Output 2:
Input:
0.80
Output:
80
Example Input/Output 3:
Input:
0.0
Output:
0
import java.util.*;
public class Hello {
    public static void main(String[] args) {
 Scanner s=new Scanner(System.in);
    float f=s.nextFloat();
    System.out.print((int)(f*100));
    }
}
