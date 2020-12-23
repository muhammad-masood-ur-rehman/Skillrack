JAVA - Class - Constructor Definition
The main method in Hello.java is as shown below. Define the class Marks.java by filling in the code so that the program accepts the marks in three subjects and prints the total marks.
import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int maths = sc.nextInt();
        int physics = sc.nextInt();
        int chemistry = sc.nextInt();
        Marks m = new Marks(maths,physics,chemistry);
        System.out.println(m.getTotal());
    }

}
Example Input/Output:
Input:
80
80
90
Output:
250
public class Marks{
    static int a,b,c;
    Marks(int a,int b,int c){
        this.a=a;
        this.b=b;
        this.c=c;
    }
    public static int getTotal(){
        return a+b+c;
    }
}
