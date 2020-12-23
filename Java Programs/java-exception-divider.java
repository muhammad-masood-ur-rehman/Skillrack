JAVA - Exception - Divider
The class Divider.java is given below.
class Divider {

    private int A, B;

    Divider(int A, int B) {
        this.A = A;
        this.B = B;
    }

    int divide() {
        return A / B;
    }
}
Please fill in the missing lines of code for the main method class Hello.java so that the program prints the output as mentioned below.
Example Input/Output 1:
Input:
12 4
Output:
3
Example Input/Output 2:
Input:
12 0
Output:
INVALID
import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Divider divider = new Divider(scan.nextInt(), scan.nextInt());
try 
    {
      System.out.print(divider.divide());
    } 
    catch(Exception e) 
    {
      System.out.print("INVALID"); 
    }
    }
}
