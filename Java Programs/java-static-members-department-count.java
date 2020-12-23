JAVA - Static Members - Department Count
The main method in Hello.java is as shown below. Define the class Student.java by filling in the code so that the program accepts N students name and department and print the number of students in each department. Assume there are only three departments and are printed in the order as CSE, IT and ECE.
import java.util.*;

public class Hello {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = Integer.parseInt(scan.nextLine());
        Student[] students = new Student[N];
        for (int index = 0; index <= N - 1; index++) {
            String name = scan.next();
            String department = scan.next();
            students[index] = new Student(name, department);
        }
        Student.printDepartmentCount();
    }

}
Example Input/Output 1:
Input:
4
Rajesh CSE
Shanmugam ECE
Ramya ECE
Raja IT
Output:
CSE 1
IT 1
ECE 2
Example Input/Output 2:
Input:
5
Ravi ECE
Riyas CSE
Mukil IT
Chris CSE
Diana IT
Output:
CSE 2
IT 2
ECE 1
public class Student
{
	public static int cs=0,it=0,ec=0;
	Student(String a, String b){
	    if(b.equals("CSE")) cs++;
	    else if(b.equals("IT")) it++;
	    else if(b.equals("ECE")) ec++;
	}
	public static void printDepartmentCount(){
	    System.out.print("CSE "+cs+"\nIT "+it+"\nECE "+ec);
	}
}
