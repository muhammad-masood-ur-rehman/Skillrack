JAVA - Generics - String Sort
An array of N strings is passed as input. Implement the function to sort the strings in ascending order and print the strings as mentioned in the Example Input/Output section.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains N.
The next N lines contain a string in each line.
Output Format:
The first N lines contain the strings in sorted order.
Example Input/Output 1:
Input:
4
mary
jane
spidey
miracle
Output:
jane
mary
miracle
spidey
import java.util.*;

public class Hello {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        List<String> strings = new ArrayList<>(N);
        for(int ctr = 1; ctr<=N; ctr++){
            strings.add(scan.next());
        }
        sortAndPrint(strings);
    }
    public static void sortAndPrint(List<String>s){
        Collections.sort(s);
        for(String s1:s){
             System.out.println(s1);
        }
     }
}
