Reverse String Till Underscore
String S is passed as the input to the program. S may or may not have a single underscore embedded in it. The program must reverse the String S till the first underscore and print it as the output.
Input Format: The first line contains S.
Output Format: The first line contains the string S modified based on the given conditions.
Boundary Conditions: Length of S is from 3 to 100.
Example Input/Output 1:
Input:
abcd_pqrs
Output:
dcba_pqrs
Example Input/Output 2:
Input:
_kilo
Output:
_kilo
Example Input/Output 3:
Input:
nounderscore
Output:
erocsrednuon
import java.util.*;
public class Hello {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        String s1=s.nextLine();
        int u=s1.indexOf('_');
        if(u==-1)
        System.out.print(new StringBuffer(s1).reverse().toString());
        else if(u==0)
        System.out.print(s1);
        else
        {
           if(u==s1.length()-1)
           {
               String[] s2=s1.split("_");
               System.out.print(new StringBuilder(s2[0]).reverse().toString()+"_");
           }
           else
           {
               String[] s2=s1.split("_");
               System.out.print(new StringBuilder(s2[0]).reverse().toString()+"_"+s2[1]);
           }
        }
    }
}
s=input()
n=s.index("_")
if n==-1:
    print(s[::-1])
elif n==len(s)-1:
    print(s[:len(s)-1]+"_")
else:

    print(s[:n][::-1]+s[n:])
