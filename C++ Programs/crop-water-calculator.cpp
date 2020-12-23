Crop Water Calculator
A farmer wants to plant paddy crops in his farm. So he visited a near by agriculture shop to buy seeds. The shopkeeper showed the farmer various varieties of paddy seed. Each variety of paddy seed  varies from one another especially on the 
Number of Days D needed to water and it Growth Rate G.
The quantity of water in certain units required by a single crop in a single day is same as the growth rate on that particular day.
The Growth Rate G reduces by a value Reveryday which will reduce the water consumption by crops.
The shopkeeper issued S number of seeds to the farmer and assuming all seeds will grow.
write a program to find the units of Water Consumption W for D days.
Input Format
The first line contains the value of Number of Seeds S, Growth Rate G, Number of Days D to grow and the Reduction in Growth Rate R
each separated by a space.
Output Format:
The first line contains the total units of Water Consumption W in D days.
Boundary Conditions:
1 <= S, G, D, R <= 999999
Example Input/Output 1:
Input:
10 5 5 1
Output:
150
Explanation:
The total number of seeds S the farmer will buy is 10
The number of days D the crop has to be watered is 5
The growth rate G of each seed is 5.
The growth rate G is reduced by R-value 1 on every day. So, for the day 1 G is 5, day 2 G is 4, day 3 it is 3 and so on.
The Water Consumption W for 5 days = 105 + 104 + 103 + 102 + 10*1 = 150 units
Example Input/Output 2:
Input:
100 10 10 0
Output:
10000
#include<stdio.h>
#include <stdlib.h>

int main()
{
long int s,g,d,r;
scanf("%li %li %li %li",&s,&g,&d,&r);
long int i,sum=0;
for(i=0;i<d;i++)
{
    sum+=s*g;
    g-=r;
}
printf("%li",sum);

}
#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{
long int seeds,growth,days,growth_red,water = 0;
cin >> seeds >> growth >> days >> growth_red;
for(int i=0;i<days;i++)
{
    water += seeds*growth;
    growth = growth - growth_red;
}
cout << water;
}
import java.util.*;
public class Hello {

    public static void main(String[] args) {
Scanner s=new Scanner(System.in);
long se,g,d,r,w=0;
se=s.nextLong();
g=s.nextLong();
d=s.nextLong();
r=s.nextLong();
for(int i=1;i<=d;i++)
{
    w+=se*g;
    g-=r;
}
System.out.print(w);
    }
}
