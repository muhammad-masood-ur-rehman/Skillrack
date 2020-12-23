JAVA - Package - EvenPrinter
The class Hello.java is given below.
import java.util.Scanner;
import com.skillrack.util.EvenPrinter;

public class Hello {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int from = scan.nextInt();
        int to = scan.nextInt();
        EvenPrinter.printEvenRange(from, to);
    }
}
Please write the code for the class EvenPrinter.java so that the program prints the output as mentioned below.
Example Input/Output 1:
Input:
5 10
Output:
6 8 10
Example Input/Output 2:
Input:
12  24
Output:
12 14 16 18 20 22 24
package com.skillrack.util;
public class EvenPrinter{
    public static void printEvenRange(int from,int to){
        while(from<=to){
            if(from%2==0)System.out.print(from+" ");
            from++;
        }
        return;
    }
}
