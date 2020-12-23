JAVA - Class - Constructor Plus Static Method
The main method in Hello.java is as shown below. Define the class Counter.java by filling in the code so that the program accepts a positive integer value X and prints twice the value of X.
import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        Counter ctr=null;
        for(int i=1; i <= x; i++){
            ctr = new Counter();
        }
        System.out.println(ctr.getCounter());
    }
}
Example Input/Output 1:
Input:
5
Output:
10
Example Input/Output 2:
Input:
55
Output:
110
public class Counter{
    static int var=0;
    Counter(){
        var++;
    }
    public int getCounter(){
        return var*2;
    }
}
