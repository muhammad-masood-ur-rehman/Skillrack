JAVA - Method Overloading - Adder
The main method class Hello.java is given below.
import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        Adder twoAdder = new Adder(a, b);
        System.out.println(twoAdder.getSum());
        Adder threeAdder = new Adder(a, b, c);
        System.out.println(threeAdder.getSum());
    }
}
Please write the code for the class Adder.java so that the program prints the output as mentioned below.
Example Input/Output:
Input:
10 20 30
Output:
30
60
lass Adder 
{  
  int ans; 
  int a,b,c;
  Adder(int a,int b) 
  {
    this.a=a;
    this.b=b;  
    ans=a+b;
  } 
  Adder(int a,int b,int c) 
  {
    this.a=a;
    this.b=b;
    this.c=c; 
    ans=a+b+c;
  }
  public int getSum() 
  {
    return ans;
  } 
}
