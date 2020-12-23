JAVA - File Handling - Count 1s
An array of N integers is given in a file. The program must print the number of 1s in the input. The name of the file is stored in the variable fileName.
Boundary Condition(s):
1 <= N <= 1000
Input File Format:
The first line contains N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains an integer.
Example Input/Output 1:
Input:
4
2 1 3 1
Output:
2
Example Input/Output 2:
Input:
5
1 2 1 1 1
Output:
4
import java.io.*;
import java.util.*;

public class Hello {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String fileName = scan.next();
    FileReader file;
    int count=0;
    try{
        file=new FileReader(fileName);
        Scanner sc=new Scanner(file);
        int n=sc.nextInt();
        while(sc.hasNext()){
            int num=sc.nextInt();
            if(num==1)count++;
        }
        System.out.print(count);
    }
    catch(Exception r){
        
    }
    }
}
