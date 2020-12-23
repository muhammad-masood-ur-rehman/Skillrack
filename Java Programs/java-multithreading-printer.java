JAVA - MultiThreading - Printer
The class Hello.java is given below.
import java.util.Scanner;
public class Hello {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        Thread thread1 = new Thread(new Printer(N/2));
        Thread thread2 = new Thread(new Printer(N/2));
        thread1.start();
        thread2.start();
    }
}
Please write the code for the class Printer.java so that the program prints 1 for N times as mentioned below. Assume N is always even.
Example Input/Output 1:
Input:
6
Output:
1 1 1 1 1 1
Example Input/Output 2:
Input:
4
Output:
1 1 1 1
public class Printer implements Runnable{
    int limit;
    Printer(int n){
        limit=n;
    }
    public void run(){
        for(int i=0;i<limit;++i)System.out.print("1 ");
    }
}
