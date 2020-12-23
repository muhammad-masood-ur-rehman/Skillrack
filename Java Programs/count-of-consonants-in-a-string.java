Count of Consonants in a String
Given a string,program must print the count of Consonants in a string
Example input/output 1:
Input:
abcde
output:
3
Example input/output 2:
Input:
abcdeABCDE
output:
6
import java.util.*;
class Consonants
{
 public static void main (String[] args)
 {
 Scanner s=new Scanner(System.in);
 String str1=s.nextLine();
 int y=0;
 String[] str=str1.split("[aeiou|AEIOU]");
 for(int i=0;i<str.length;i++){
 y+=str[i].length();
 }
 System.out.print(y);
 }
}
