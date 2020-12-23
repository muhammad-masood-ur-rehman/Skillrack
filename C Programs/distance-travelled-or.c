Distance Travelled + or -
The program must accept a string S representing the direction of movement as the input. The string S contains only the characters + and -. A boy moves 1 unit left side if the character in S is -. The boy moves 1 unit right side if the character in S is +. The program must print the distance between the starting position of the boy and the final position at the end of the string as the output.
Boundary Condition(s):
1 <= Length of S <= 1000
Input Format:
The first line contains the string S.
Output Format:
The first line contains the distance between the starting and final position of the boy.
Example Input/Output 1:
Input:
-+++-
Output:
1
Explanation:
The first character is - so he moves 1 unit towards his left.
The second character is + so he moves 1 unit towards his right so he reaches the starting position again.
The third character is + so he moves 1 unit towards his right. Now he is 1 unit away from the starting position.
The fourth character is + so he moves 1 unit towards his right. Now he is 2 units away from the starting position.
The fifth character is - so he moves 1 unit towards his left. Now he is 1 unit away from the starting position.
So the output is 1.
Example Input/Output 2:
Input:
+++++-
Output:
4
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char s[1000];
    int position=0;
    scanf("%s",s);
    for(int i=0;s[i]!=NULL;i++)
    {
        if(s[i]=='+') position++;
        else position--;
    }
    printf("%d",abs(position));
}
