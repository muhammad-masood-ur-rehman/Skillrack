Decode Ways - Secret Message [Zoho]
A top secret message string S containing letters from A-Z (only upper case letters) is encoded to numbers using the following mapping:
'A' -> 1, 'B' -> 2 and so on till Z -> '26'
The program has to print the total number of ways in which the received message can be decoded.
Input Format:
The first line contains the string S containing numbers.
Output Format:
The first line contains the number of ways in which S can be decoded.
Boundary Conditions:
1 <= Length of S <= 100
Example Input/Output 1:
Input:
123
Output:
3
Explanation:
1-A 2-B 3-C 12-L 23-W.
Hence 123 can be decoded as ABC or AW or LC, that is in 3 ways.
Example Input/Output 2:
Input:
1290
Output:
0
def decode(s):
    n=len(s)
    dp=[0 for i in range(n)]
    if s[0]!='0':
        dp[0]=1
    for i in range(1,n):
        x=int(s[i])
        y=int(s[i-1:i+1])
        if x>=1 and x<=9:
            dp[i]+=dp[i-1]
        if y>=10 and y<=26:
            if i-1>0:
                dp[i]+=dp[i-2]
            else:
                dp[i]+=1 
    return dp[-1]
n=(input())
print(decode(n))
import java.util.*;
public class Main {

    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        char str[]=scan.next().toCharArray();
        int ways=1,prevWays=1;
        int l=str.length;
        if(str[l-1]=='0'){
            ways=0;
        }
        for(int i=l-2;i>-1;--i){
            int backUp=prevWays;
            prevWays=ways;
            if(str[i]=='0'){
                ways=0;
                continue;
            }
            int twoDigi=Integer.parseInt(str[i]+""+str[i+1]);
            if(twoDigi<=26){
                ways=ways+backUp;
            }
        }
        System.out.print(ways);
	}
}
