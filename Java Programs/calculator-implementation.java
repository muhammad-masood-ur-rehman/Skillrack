Calculator Implementation
The interface Calculator defines the following methods.
public interface Calculator {
    int add(int x, int y);
    int subtract(int x, int y);
    int mutiply(int x, int y);
    int divide(int x, int y);
}
Define the class NormalCalculator so that it implements the interface Calculator.
Input Format:
First line contains x.
Second line contains y.
Output Format:
The first line contains the sum of x,y
....
...
The fourth line contains the value of x/y
Boundary Conditions:
1 <= x,y < = 99999
Example Input/Output 1:
Input:
10
5
Output:
15
5
50
2
public class NormalCalculator implements Calculator{
    int add(int x,int y) 
    { 
      return x+y; 
    } 
    int subtract(int x,int y) 
    {
      return x-y; 
    } 
    int multiply(int x,int y) 
    {
      return x*y; 
    } 
    int divide(int x,int y) 
    {
      return x/y; 
    }
}//End of class NormalCalculator
