Train Journey - Initial Boarding Count
In a train journey, there are N stations between station A and B (The train starts from station A). The number of passengers who alighted in station B is passed as the input. The number of passengers who alighted and boarded in the N stations in between is also passed as the input. The program must print the number of passengers who boarded the train at station A.
Input Format: The first line contains N and the number of passengers who alighted at station B (which is the last station), separated by a space. N lines containing the number of passengers who alighted and boarded the train in the N stations in between A and B, with the values separated by a space.
Output Format: The first line contains the number of passengers who boarded the train at station A.
Boundary Conditions: 1 <= N <= 50
Example Input/Output 1:
Input:
3 50
30 40
40 10
60 30
Output:
100
Explanation: There are 3 stations in between A and B.
100 passengers boarded the train at station A. In the 2nd station (first after A), 30 got down and 40 boarded the train.
So now passengers in the train is 100-30+40 = 110 In the 3rd station (second after A), 40 got down and 10 boarded.
So passengers left in the train = 110-40+10 = 80 In the 4th station, passengers left in the train = 80-60+30 = 50.
These 50 passengers will alight in the last station which is station B.
#include <stdio.h>
int main() {
    int n,b,i,s,n1,n2;
    scanf("%d %d",&n,&b);
    for(i=0;i<n;i++)
    {
        scanf("%d %d",&n1,&n2);
        s=b+n1-n2;
        b=s;
    }
    printf("%d",s);

}
