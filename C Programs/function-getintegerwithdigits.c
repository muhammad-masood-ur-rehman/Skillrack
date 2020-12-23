Function - getIntegerWithDigits
C:
#include <stdio.h>
unsigned long long int getIntegerWithDigitsCount(int N)
{
  unsigned long long int m=N,k,l=0,a=0,count;
  while(m>0)
  {
      count=1;
      k=m/10;
      while(k>0)
      {
          if(m%10==k%10)
          count++;
          else
          break;
          k/=10;
      }
      l+=(m%10)*pow(10,a);
      a++;
      l+=(count)*pow(10,a);
      a++;
      m=k;
  }
  return l;
}
int main()
{
    int N;
    scanf("%d",&N);
    printf("%llu",getIntegerWithDigitsCount(N));
}
Java:
import java.util.*;

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.print(getIntegerWithDigitsCount(N));
    }

private static long getIntegerWithDigitsCount(int N) {
String str=String.valueOf(N),ans="";int len=str.length(),i,j,count=0;
for(i=0;i<len;i++)
{
    count=1;
    for(j=i+1;j<len;j++)
    {
        if(str.charAt(i)==str.charAt(j))
        count++;
        else
        break;
    }
    ans=ans+String.valueOf(count)+String.valueOf(str.charAt(i));
    i=(j-1);
}
long n=Long.parseLong(ans);
return n;

}
}
