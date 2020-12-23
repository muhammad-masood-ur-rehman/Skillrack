Print Strings for Number
A number N is passed as the input to the program. Each digit in the number represents an alphabet (a for 1, b for 2 ...) based on the alphabet position. Also, two digits can be combined to form an alphabet in the corresponding position (m for 13). The program must print all possible words which can be formed using the given number without reordering or removing any digit in it.
Note: The list of strings must be sorted in ascending order lexicographically and all the alphabets must be in lowercase.
Boundary Condition(s):
1 <= Number of digits in N <= 18
Input Format:
The first line contains N
Output Format:
The first line contains all possible words separated by a space.
Example Input/Output 1:
Input:
121
Output:
aba au la
Explanation:
The possible digit combinations are,
1, 2 and 1 -> aba
1 and 21 -> au
12 and 1 -> la
Example Input/Output 2:
Input:
12131
Output:
abaca abma auca laca lma
#include <stdio.h>
#include <string.h>
void comb(char s[], char arr[], int num , int k, int s1) {
  if (s1 == k) {
    for (int j = 0; j < num ; j++)
    printf("%c", s[j]);
    printf(" ");
    return;
    } 
    else if (s1 > k)
    return;
    s[ num ] = arr[s1] - '0' + 96;
    comb(s, arr, num +1, k, s1 + 1);
    if (((arr[s1] - '0') * 10) + (arr[s1] - '0') <= 26 && s1 + 1 < k)
    {
        s[ num ] = ((arr[s1] - '0') * 10) + (arr[s1 + 1] - '0') + 96;
        comb(s, arr, num +1, k, s1 + 2);
    }
}

int main()
{
  char arr[20];
  scanf("%s", arr);
  char s[20] = "";
  comb(s, arr, 0, strlen(arr), 0);
}
