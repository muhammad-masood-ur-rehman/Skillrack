Maximum by Single Digit Replacement
Maximum by Single Digit Replacement: Two integers M and N are passed as the input to the program. The program must print the maximum value of M obtained by replacing exactly one digit in M by a digit from N.
Boundary Condition(s):
1 <= Number of digits in M <= 100
1 <= Number of digits in N <= 10
Input Format:
The first line contains M and N separated by space(s).
Output Format:
The first line contains the maximum value of M.
Example Input/Output 1:
Input:
56120 21
Output:
56220
Explanation:
The maximum value is obtained by replacing 1 in 56120 by 2.
Any other replacements would give smaller values.
Example Input/Output 2:
Input:
895496223 5
Output:
895596223
Maximum by Single Digit Replacement in Java
import java.util.*;
public class Hello {

    public static void main(String[] args)
    {
		Scanner sc=new Scanner(System.in); 
		String f=sc.next();
		String s=sc.next();
		char ff[]=f.toCharArray();
		char ss[]=s.toCharArray();   
		int maxi=0;
		for(int i=0;i<ss.length;i++)
		{
		    if(Integer.parseInt(String.valueOf(ss[i]))>maxi)
		    {
		        maxi=Integer.parseInt(String.valueOf(ss[i]));
		    }
		}
		int fl=0;
		for(int i=0;i<ff.length;i++)
		{
		    if(maxi>Integer.parseInt(String.valueOf(ff[i])))
		    {
		        ff[i]=(char)(maxi+'0');  
		        break;
		           
		    } 
		} 
		System.out.println(String.valueOf(ff));
	}
}
