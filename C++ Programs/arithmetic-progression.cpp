Arithmetic Progression
Accept three values related to an arithmetic progression - number of terms T, initial value I and the difference between the terms D.
Print the values of the T terms.
Input Format :
The first line contains the number of terms T.
The second line contains the initial value I.
The third line contains the difference between the terms D.
Output Format :
The first line contains the values of T terms in the progression.
Example Input/Output 1 :
Input :
5
1
2
Output :
1 3 5 7 9
Example Input/Output 2:
Input :
6
5
20
Output
5 25 45 65 85 105
#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{
int x,a,d;
cin >> x >> a >> d;
for(int i=1;i<=x;i++)
{
    cout << a + (i-1)*d << " ";
}
}
