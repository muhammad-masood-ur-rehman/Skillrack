Winner of a Card Game
Arun, Balaji, and Chandra are playing a card game. The points collected at the end of the game is given as input. The program must print the winner of the game (who has scored the maximum points). If all the three players have the same score, print TIE. If any two players have the same score print their names in Alphabetical order.
Input Format:
The first line contains the points separated by space.
Output Format:
The first line contains TIE if all the points are equal, or the winner's name in alphabetical order if any two points are equal, or the winners name if none of the points are equal.
Boundary Conditions:
10 <= A,B,C <= 1000
Example Input/Output 1:
Input:
10 20 30
Output:
Chandra
Example Input/Output 2:
Input:
10 10 5
Output:
Arun Balaji
Example Input/Output 3:
Input:
30 30 30
Output:
TIE
#include<stdio.h>
int main()
{
int a,b,c;
scanf("%d %d %d",&a,&b,&c);
if(a==b&&b==c) printf("TIE");
else if(a==b&&b>c) printf("Arun Balaji");
else if(b==c&&b>a) printf("Balaji Chandra");
else if(a==c&&a>b) printf("Arun Chandra");
else if(a>b&&a>c) printf("Arun");
else if(b>c&&b>a) printf("Balaji");
else printf("Chandra");
}
import java.util.*;
public class Hello {

    public static void main(String[] args) {
                  Scanner sc=new Scanner(System.in);
                  int a=sc.nextInt();
                  int b=sc.nextInt();
                  int c=sc.nextInt();
                  int m;
                  m=a>b?a:b;
                  m=m>c?m:c;
                  if(a==m && b==m && c==m)
                  {
                  System.out.print("TIE");
                  System.exit(0);
                  }
                  if(a==m)
                  System.out.print("Arun ");
                  if(b==m)
                  System.out.print("Balaji");
                  if(c==m)
                  System.out.print("Chandra");
                }

}
#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
int a,b,c;
cin>>a>>b>>c;
if(a==b&&a==c&&b==c)
cout<<"TIE";
else if(a==b)
cout<<"Arun "<<"Balaji";
else if(a==c)
cout<<"Arun "<<"Chandra";
else if(b==c)
cout<<"Balaji "<<"Chandra";
else if(a>b&&a>c)
cout<<"Arun";
else if(b>a&&b>c)
cout<<"Balaji";
else if(c>a&&c>b)
cout<<"Chandra";

}
