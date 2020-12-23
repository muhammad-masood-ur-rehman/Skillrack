Codu and Sum Love
Given N number of x's, perform logic equivalent of the below Java code and print the output.
import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long sum = 0;
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            final long x = sc.nextLong(); // Read the value of x
            String str = Long.toString((long) Math.pow(1 << 1, x));
            str = str.length() > 2 ? str.substring(str.length() - 2) : str;
            sum += Integer.parseInt(str);
        }
        System.out.println(sum % 100);
    }
}
Boundary Condition(s):
1 <= N <= 10^7
0 <= x <= 10^18
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains an integer representing the output of the given code by taking inputs as specified above.
Example Input/Output 1:
Input:
4
8 6 7 4
Output
64
Example Input/Output 2:
Input:
3
1 2 3
Output:
14
Example Input/Output 3:
Input:
4
5645456444645465 10000 265444 999999999999
Output:
12
#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    
    long long int x,a[n],s=0,power[22];
    for(int i=0;i<22;i++){
        power[i]=(1<<i);
    }
    for(int i=1;i<=n;i++){
        scanf("%lld",&x);
        if(x<=21){
            s+=power[x]%100;
        }
        else{
            int re=x%20;
            if(re==0){
                re=20;
            }
            else if(re==1){
                re=21;
            }
            s+=(power[re])%100;
        }
    }
    printf("%lld",s%100);
    
}
