JAVA - Constructor - Sum and Product
The main method in Hello.java is as shown below. Define the class Calculator.java by filling in the code so that the program accepts an integer N and N more integers. If N is 2 the program must print the sum of two integers else if N is 3 the program must print the product of three integers.
import java.util.*;

public class Hello {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        if (N == 2) {
            Calculator calculator = new Calculator(num1, num2);
            System.out.println(calculator.getResult());
        } else if (N == 3) {
            int num3 = scan.nextInt();
            Calculator calculator = new Calculator(num1, num2, num3);
            System.out.println(calculator.getResult());
        }

    }

}
Example Input/Output 1:
Input:
2
1 2
Output:
3
Example Input/Output 2:
Input:
3
1 2 3
Output:
6
public class Calculator
{
	private int res;
	Calculator(int a, int b){
	    res=a+b;
	}
	Calculator(int a, int b, int c){
	    res=a*b*c;
	}
	public int getResult(){
	    return res;
	}
}
