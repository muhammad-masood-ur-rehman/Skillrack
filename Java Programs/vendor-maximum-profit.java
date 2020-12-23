Vendor Maximum Profit
A vendor has a shop and he wants to purchase some items for a maximum of N rupees.
There are K items in a wholesale store that the vendor is going to buy.
Each item has the cost price and profit that the seller can sell.
The vendor can buy multiple items but not the same type.
The program must accept the value of N and the cost price and profit of the K items as the input.
The program must print the maximum profit that the vendor can earn by buying and selling the items as the output.
Example
Input/Output 1:
Input:
10 6
5 2
6 4
3 2
4 3
1 2
15 20
Output:
8
import java.util.*;

class Market implements Comparable<Market>{
    int price;
    int profit;
    public int compareTo(Market market){
        return price-market.price;
    }
}
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
		Scanner scan=new Scanner(System.in);
        ArrayList<Market> list=new ArrayList<>();
        int n=scan.nextInt(),k=scan.nextInt();
        
        for(int i=0;i<k;++i){
            Market obj=new Market();
            obj.price=scan.nextInt();
            obj.profit=scan.nextInt();
            list.add(obj);
        }
        Collections.sort(list);
        
        int dp[][]=new int[k+1][n+1];
        
        for(int i=1;i<=list.size();++i){
            Market item=list.get(i-1);
            if(item.price>n){
                System.out.print(dp[i-1][n]);
                return;
            }
            for(int amt=1;amt<=n;++amt){
                if(amt<item.price){
                    dp[i][amt]=dp[i-1][amt];
                }
                else{
                    int onbuying=item.profit+dp[i-1][amt-item.price];
                    dp[i][amt]=Math.max(onbuying,dp[i-1][amt]);
                }
            }
        }
        System.out.print(dp[k][n]);
        return;
	}
}
