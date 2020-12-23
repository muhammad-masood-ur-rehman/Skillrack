Array LEADERS [Zoho]
An array of N numbers is passed as input. The program must print all the LEADERS in the array. A number is a LEADER if it is greater than all the numbers to it's right.
Note: The rightmost number is always a leader.
Input Format:
The first line contains N numbers, each separated by a space.
Output Format:
The first line contains the LEADERS, each separated by a space.
Boundary Conditions:
1 <= N <= 9999
Example Input/Output 1:
Input:
10 17 4 3 5 2
Output:
17 5 2
l=list(map(int,input().split()));p=[]
for i in range(len(l)):
    k=0
    for j in range(i+1,len(l)):
        if l[i]<l[j]:k=1
    if k==0 and l[i] not in p:p.append(l[i])
print(*p)
import java.util.*;
public class Hello {

    public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    ArrayList<Integer> numbers = new ArrayList<Integer>();
	    while(sc.hasNextInt())
	    {
	        numbers.add(sc.nextInt());
	    }
	    int numberSize = numbers.size();
	    int j = 0;
	    for(int i=0;i<numberSize;i++)
	    {
	        for(j=i+1;j<numberSize;j++)
	        {
	            if(numbers.get(i)<=numbers.get(j))
	            {
	                break;
	            }
	        }
	        if(j==numberSize)
	            System.out.print(numbers.get(i)+" ");
	    }
	}
}
