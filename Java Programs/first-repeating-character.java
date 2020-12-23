First Repeating Character
A string S is passed as the input. S has at least one repeating character. The program must print the first repeating character C.
Input Format: The first line contains S.
Output Format: The first line contains C.
Boundary Conditions: Length of S will be from 3 to 100.
Example Input/Output 1:
Input:
abcdexyzbwqpoolj
Output:
b
import java.util.*;
public class Hello {
    public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
String s=sc.nextLine();
char[] c=s.toCharArray();
HashMap<Character,Integer> h=new HashMap<Character,Integer>();
for(char x:c)
{
    if(h.containsKey(x))
    h.put(x,h.get(x)+1);
    else
    h.put(x,1);
}
for(char x:c)
{
    if(h.get(x)>1)
    {
        System.out.println(x);
        break;
    }
}
}
}
