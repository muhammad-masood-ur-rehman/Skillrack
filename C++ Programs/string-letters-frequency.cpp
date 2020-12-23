String Letters Frequency
A string value S containing N unique letters is passed as the input. The program must print the letters in the string based on the count of their occurrence. The letters of higher frequency of occurrence must appear first. If two letters have same frequency of occurrence then they are arranged as per alphabetical order.
Input Format:
The first line contains S.
Output Format:
N lines containing letters based on their frequency of occurrence.
Boundary Conditions:
2 <= LENGTH(S) <= 10000
Example Input/Output 1:
Input:
MANAGEMENT
Output:
A2
E2
M2
N2
G1
T1
Example Input/Output 2:
Input:
ArrangemENt
Output:
r2
A1
E1
N1
a1
e1
g1
m1
n1
t1
#include<iostream>
#include<string>
using namespace std;
 
int main()
{
    string inp;
    static int frequency[52], order[52][2];
    int i,j,index,count=0,ind=0;
    cin>>inp;
    for(i=0; i<inp.size(); i++)
        if(isupper(inp[i]))
        {
            index = inp[i] - 'A';
            frequency[index]++;
        }
        else
        {
            index = inp[i] - 'a' + 26;
            frequency[index]++;
        }
    for(i=0; i<26; i++)
        if(frequency[i] != 0)
        {
            //cout<<char(i+65)<<frequency[i]<<endl;
            order[ind][0] = i+65;
            order[ind][1] = frequency[i];
            ind++;
        }
    for(i=26; i<52; i++)
        if(frequency[i] != 0)
        {
            //cout<<char(i+71)<<frequency[i]<<endl;
            order[ind][0] = i+71;
            order[ind][1] = frequency[i];
            ind++;
        }
    for(i=0; i<ind; i++)
        for(j=0; j<ind-i-1; j++)
            if(order[j][1] < order[j+1][1])
            {
                int temp[1][2];
                temp[0][0] = order[j][0];
                temp[0][1] = order[j][1];
                order[j][0] = order[j+1][0];
                order[j][1] = order[j+1][1];
                order[j+1][0] = temp[0][0];
                order[j+1][1] = temp[0][1];
            }
    for(i=0; i<ind; i++)
        cout<<char(order[i][0])<<order[i][1]<<endl;
    return 0;
}
