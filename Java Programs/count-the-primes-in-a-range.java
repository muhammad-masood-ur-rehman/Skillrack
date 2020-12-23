Count the primes in a range
Two whole numbers N1 and N2 are passed as input. The program must print the number of primes present between N1 and N2 (the range is inclusive of N1 and N2)
Input Format: First line will contain the value of the first number N1 Second line will contain the value of the second number N2 
Output Format: First line will contain the count of prime numbers between N1 and N2 
SampleInput/Output: 
Example 1:
 Input: 
6142 
6200
Output: 
6 
Explanation: The prime numbers within the range 6142 to 6200 are 6143, 6151, 6163, 6173, 6197, 6199
 
Example 2: 
Input: 
38
70 
Output:
7 
Explanation: The prime numbers within the range 38 to 70 are 41, 43, 47, 53, 59, 61, 67
l,u=int(input()),int(input())
c=0
for i in range(l,u + 1):
   if  i> 1:
       for j in range(2,i):
           if (i%j) == 0:
               break
       else:
           c+=1
print(c)
import java.util.*;
public class Hello {

    public static void main(String[] args) {
  Scanner sc= new Scanner(System.in);
  int c=0,i,j;
  int l=sc.nextInt();
  int h=sc.nextInt();
  for(i=l;i<=h;i++)
  {
   for(j=2;j<i;j++)
       if(i%j==0)
       break;
    if(i==j)
       c++;
   }
   System.out.print(c);
 }

}
