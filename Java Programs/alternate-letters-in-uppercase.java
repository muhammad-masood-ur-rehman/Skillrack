Alternate letters in uppercase
A str‌ing S (only alphabets) is passed as input. The printed output should contain alphabets in odd positions in each word in uppercase and alphabets in even positions in each word in lowercase.
Input Format: The first line will contain S.
Output Format: The first line will contain the resultant string value based on the conditions provided.
Boundary Conditions: Length of S is from 3 to 100.
Example Input/Output 1:
Input:
tREE GiVES us fruiTS
Output:
TrEe GiVeS Us FrUiTs
Example Input/Output 2:
Input:
FLoweR iS beauTIFUL
Output:
FlOwEr Is BeAuTiFuL
import java.util.*;
public class Hello {

    public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
String s=sc.nextLine();
String[] s1=s.split(" ");
for(String x:s1)
{
    int i=0;
    for(Character ch:x.toCharArray())
    {
        if(i%2==0)
            System.out.print(Character.toUpperCase(ch));
        else
            System.out.print(Character.toLowerCase(ch));
        i++;
    }
    System.out.print(" ");
}
}

}
