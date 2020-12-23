Average Speed
A single line L with a set of space separated values indicating distance travelled and time taken is passed as the input. The program must calculate the average speed S (with precision upto 2 decimal places) and print S as the output.
Note: The distance and time taken will follow the format DISTANCE@TIMETAKEN. DISTANCE will be in kilometers and TIMETAKEN will be in hours.
Input Format: The first line contains L.
Output Format: The first line contains the average speed S.
Boundary Conditions: Length of L will be from 3 to 100.
Example Input/Output 1:
Input: 60@2 120@3
Output:
36.00 kmph
Explanation:
Total distance = 60+120 = 180 km.
Total time taken = 2+3 = 5 hours.
Hence average speed = 180/5 = 36.00 kmph
import java.util.*;
public class Hello {
    public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
String s=sc.nextLine();
String[] s1=s.split("\\s");
double t=0,t1=0;
for(int i=0;i<s1.length;i++)
{
String[] s2=s1[i].split("@");
t+=Integer.parseInt(s2[0]);
t1+=Integer.parseInt(s2[1]);
}
double avg=t/t1;
System.out.printf("%.2f kmph",avg);
            }

}
