Sort - Odd & Even Ascending
An array of N numbers is passed as the input. The program must sort the odd numbers and even numbers separately in ascending order. The odd and even numbers must retain their original odd even slots in the input.
Input Format:
The first line contains N indicating the count of numbers in the array.
The second line contains the N array elements separated by a space.
Output Format:
The first line contains the N sorted array elements separated by a space.
Boundary Conditions:
2 <= N <= 100
Example Input/Output 1:
Input:
9 169 181 298 16 147 263 102 155 141
Output: 141 147 16 102 155 169 298 181 263
import java.util.*;
public class Hello {

    public static void main(String[] args) {
    Scanner s=new Scanner(System.in);
    int n=s.nextInt();
    int x=0,w=0;
    Vector<Integer> v1=new Vector<Integer>();
    Vector<Integer> v2=new Vector<Integer>();
    Vector<Integer> v3=new Vector<Integer>();
    for(int i=0;i<n;i++){
    int y=s.nextInt();
    v3.add(y);
        if(y%2==0)
        v1.add(y);
        else
        v2.add(y);
    }
    Collections.sort(v1);
    Collections.sort(v2);
    for(int i=0;i<v3.size();i++)
    {
        if((v3.get(i))%2==0)
        System.out.print(v1.elementAt(x++)+" ");
        else
        System.out.print(v2.elementAt(w++)+" ");
    }
    }

}
