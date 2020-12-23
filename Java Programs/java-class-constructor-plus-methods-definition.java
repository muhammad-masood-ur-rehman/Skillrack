JAVA - Class - Constructor Plus Methods Definition
The main method in Hello.java is as shown below. Define the class SimpleCalculator.java by filling in the code so that the program accepts the two positive integers and prints their sum and the absolute value of their difference.
import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x=sc.nextInt(),y=sc.nextInt();
        SimpleCalculator calc = new SimpleCalculator(x,y);
        System.out.println(calc.getSum());
        System.out.println(calc.getDiff());
    }
}
Example Input/Output 1:
Input:
20 80
Output:
100
60
Example Input/Output 2:
Input:
90 20
Output:
110
70
public class SimpleCalculator{
    int x,y;
    SimpleCalculator(int x,int y){
        this.x=x;
        this.y=y;
    }
    public int getSum(){
        return x+y;
    }
    public int getDiff(){
        return Math.abs(x-y);
    }
}
