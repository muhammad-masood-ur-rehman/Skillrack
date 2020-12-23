Numbers - Range Count
Given N distinct integers, the program must print the number of ranges R present. A range is defined as two or more consecutive integers.
Input Format:
The first line contains N.
The second line contains N integer values separated by a space.
Output Format:
The first line contains R.
Boundary Conditions:
2 <= N <= 100000
1 <= R <= 10000
Example Input/Output 1:
Input:
5
2 1 4 9 3
Output:
1
Explanation:
The only range which is present is 1 2 3 4.
9 is not a range (as a range needs two or more consecutive integers).
Example Input/Output 2:
Input:
7
1 3 11 -15 -20 9 5
Output:
0
import java.util.*;

public class Main {

    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        
        int n=scan.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;++i)arr[i]=scan.nextInt();
        
        Arrays.sort(arr);
        
        int count=0,counter=0;
        
        for(int i=0;i<n-1;++i){
            if(Math.abs(arr[i+1]-arr[i])==1){
                if(counter==0)count++;
                counter=1;
            }
            else{
                counter=0;
            }
        }
        System.out.print(count);
	}
}
