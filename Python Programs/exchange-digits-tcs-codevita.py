Exchange Digits – TCS CodeVita
Compute the nearest larger number by interchanging its digits updated.Given 2 numbers a and b find the smallest number greater than b by interchanging the digits of a and if not possible print -1.
· Input Format
2 numbers a and b, separated by space.
· Output Format
A single number greater than b.If not possible, print -1
· Constraints
1 <= a,b <= 10000000
Example 1:
Sample Input:
    459 500
Sample Output:
    549
Example 2:
Sample Input:
    645757 457765
Sample Output:
    465577
#include <bits/stdc++.h>
using namespace std;
int main()
{
    string a, b;
    cin >> a >> b;
    sort(a.begin(), a.end());
    string temp = a;
    int flag = 1;
    while (stoi(temp) <= stoi(b))
    {

        bool temp1 = next_permutation(a.begin(), a.end());
        temp = a;
        if (!temp1)
        {
            flag = 0;
            break;
        }
    }
    if (flag)
        cout << stoi(a)<<endl;
    else
        cout << "-1\n";

    return 0;
}
from itertools import permutations
m = input()
n = input()
lst = sorted([int("".join(char)) for char in permutations(m)])
for i in lst:
if i > int(n):
print(i)
;break
