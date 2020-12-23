JAVA Constructor and Methods - Base Conversion
The main method in Hello.java is as shown below. Define the class BaseConverter.java by filling in the code so that the program accepts an integer N then converts and prints the Binary, octal and hexadecimal values of N.
import java.util.*;

public class Hello {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = Integer.parseInt(scan.nextLine());
        BaseConverter converter = new BaseConverter(N);
        System.out.println(converter.toBinary());
        System.out.println(converter.toOctal());
        System.out.println(converter.toHexadecimal());
    }

}
Example Input/Output 1:
Input:
10
Output:
1010
12
a
Example Input/Output 2:
Input:
255
Output:
11111111
377
ff
import java.lang.*;
public class BaseConverter{
    static int n;
    BaseConverter(int n){
        this.n=n;
    }
    public static string toBinary(){
        return Integer.toBinaryString(n);
    }
    public static string toOctal(){
        return Integer.toOctalString(n);
    }
    public static string toHexadecimal(){
        return Integer.toHexadecimalString(n);
    }
}
