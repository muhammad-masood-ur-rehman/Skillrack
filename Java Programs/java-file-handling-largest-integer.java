JAVA - File Handling - Largest Integer
Java Program to find the largest integer using file Handling
Java File Handling: An array of N integers is read from a file. The file name is stored in the variable fileName. Fill in the missing lines of code to print the largest of N integers.
Boundary Condition(s):
1 <= N <= 1000
Input File Format:
The first line contains N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains an integer.
Example Input/Output 1:
Input:
5
21 56 23 89 64
Output:
89
Example Input/Output 2:
Input:
6
102 456 28 10 23 666
Output:
666
Java File Handling
import java.io.; 
import java.util.;
 public class Hello {
     public static void main(String[] args) {
         Scanner scan = new Scanner(System.in);
         String fileName = scan.next();
         try {
             BufferedReader br=new BufferedReader(new FileReader(fileName));
             String l=br.readLine(); 
             int count=0;
             while(l!=null){   
                 count+=1; 
                 if(count==2){  
                     String arr[]=l.split(" "); 
                     int max=0;
                     for(int i=0;imax){
                             max=current;
                         }
                     } 
                     System.out.print(max);
                 }
                 l=br.readLine(); 
             }
         } 
         catch(Exception e){
         }
     }
 }
