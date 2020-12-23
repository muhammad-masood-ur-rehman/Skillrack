JAVA - Class - Static Method Definition
The main method in Hello.java is as shown below. 
Define the class Marks.java by filling in the code so that the program accepts the marks in three subjects and prints the total marks.
import java.util.Scanner;
public class Hello {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int maths = sc.nextInt();
        int physics = sc.nextInt();
        int chemistry = sc.nextInt();
        System.out.println(Marks.findTotal(maths, physics, chemistry));
    }
}
Example Input/Output:
Input:1009070
Output:
260
public class Marks{
    public static int findTotal(int a,int b,int c){
        return a+b+c;
    }
}
