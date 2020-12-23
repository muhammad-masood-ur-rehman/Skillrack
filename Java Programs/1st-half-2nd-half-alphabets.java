1st Half / 2nd Half Alphabets
Leela is a science teacher for class V and she wants to divide the class into two halves based on the starting letter of the names of the students. Accept the first letter of name L of the students in the class and print 1st half, if the name of the student starts with A to M Print 2nd half; if the name of the student starts with N to Z.
Input Format
The first line contains a character L
Output Format:
Print 1st half or 2nd half for the input value L based on the conditions given.
Example Input/Output 1:
Input:
A
Output:
1st half
Example Input/Output 2:
Input:
x
Output:
2nd half
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
        Scanner sc = new Scanner(System.in);
        char a = sc.next().charAt(0);
        if((a>=97 && a<=109) || (a>=65 && a<=77))
        {
            System.out.println("1st half");
        }
        else{
            System.out.println("2nd half");
        }
	}
}
