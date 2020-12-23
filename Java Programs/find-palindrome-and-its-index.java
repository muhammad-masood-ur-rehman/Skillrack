Find Palindrome and its index
A String is given S, we have to find the palindrome in that and print the starting and ending index.
Example I/O:
Example I/O:
Sample Input 1:
my madam know malayalam


Output:


madam 3 7 
ada 4 6 
malayalam 14 22 
alayala 15 21 
layal 16 20 
aya 17 19 


Sample Input 2:
himadamhi


Output:
madam 2 6 
ada 3 5 
Code:
import java.util.*;
import java.lang.*;
public class MyClass {
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        String[] s1=s.split(" ");
        int c=0;
        for(String x:s1)
        {
            int i=0,k=x.length();
            while(i<k-1)
            {
                String s2=x.substring(i,x.length()-i);
                StringBuilder sb=new StringBuilder(s2).reverse();
                if(s2.equals(sb.toString()))
                     System.out.print(s2+" "+(c+i)+" "+((c+i)+s2.length()-1)+" ");
                System.out.println();
                i++;
                k--;
            }
            c+=x.length()+1;
        }
    }
}
