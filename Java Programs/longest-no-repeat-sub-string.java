Longest No Repeat Sub-String
Given a string S, the program must print the substring based on following conditions.
 -The substring must be the longest one of all the possible substring in the given string.
 -There must not be any repeating characters in the substring.
 -If there is more than one substring satisfying the above two conditions, then print the substring which occurs first.
 -The length of the substring must be atleast 3.
If there is no substring satisfying all the above conditions then the program must print -1.
Boundary Condition(s):
1 <= Length of S <= 10^5
Input Format:
The first line contains S.
Output Format:
The first line contains the substring or -1.
Example Input/Output 1:
Input:
manager
Output:
nager
Example Input/Output 2:
Input:
abcdabcdabcd
Output:
abcd
Example Input/Output 3:
Input:
abababbaab
Output:
-1
import java.util.*;
public class Hello{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next(), maxWord = "", newWord = "";
        int l = word.length(), i, j, max = 0;
        for (i = 0; i < l; i++) {
            newWord = word.substring(i);
            for (j = i + 1; j < l; j++){
                if (newWord.indexOf(word.charAt(j)) + i != j)
                break;
            }
            if (j - i > max) {
                max = j - i;
                maxWord = word.substring(i, j);
            }
        }
        int t=maxWord.length();
        if(t>=3){
            System.out.println(maxWord);
        }
        else{
            System.out.println("-1");
        }
    }
}
