Fraction Reduce
Given a fraction A/B the program must reduce it and print the output.
Input Format:
The first line contains A/B
Output Format:
The first line contains C/D where C/D is the reduced form of A/B.
Boundary Conditions:
1 <= A,B <= 9999999
Example Input/Output 1:
Input:
15/25
Output:
3/5
Example Input/Output 2:
Input:
40/10
Output:
4/1
import java.util.;
public class Hello {
public static void main(String[] args) {

Scanner sc = new Scanner(System.in);
String s = sc.next();
String a [] = s.split("/");
int x = Integer.parseInt(a[0]);
int y = Integer.parseInt(a[1]);
for(int i=2;i<16;i++)
{
    if(x%i==0 && y%i==0)
    {
        x = x/i;
        y = y/i;
    }
}
System.out.print(x + "/" + y);

}
}
