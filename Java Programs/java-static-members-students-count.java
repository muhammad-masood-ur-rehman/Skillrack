JAVA - Static Members - Students Count
The main method in Hello.java is as shown below. Define the class Student.java by filling in the code so that the program creates a set of student objects and print the total number of student objects created.
Hello.java
import java.util.*;

public class Hello {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        Student[] students = new Student[N];
        for (int index = 0; index <= N - 1; index++) {
            students[index] = new Student();
        }
        System.out.println(Student.getCount());
    }

}
Example Input/Output 1:
Input:
3
Output:
3
Example Input/Output 2:
Input:
9
Output:
9
public class Student{
    static int no=0;
    Student(){
        no++;
    }
    public static int getCount(){
        return no;
    }
}
