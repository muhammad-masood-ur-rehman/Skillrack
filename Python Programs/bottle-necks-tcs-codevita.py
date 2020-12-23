Bottle Necks - TCS CodeVita
The program must accept the radii of N bottles as the input. Once a bottle is enclosed inside another bottle, it ceases to be visible. A bottle X is enclosed inside another bottle Y only if the following conditions are fulfilled.
1) The bottle X itself is not enclosed in another bottle.
2) The bottle Y does not enclose any other bottle.
3) The radius of the bottle X is smaller than bottle Y.
The program must print the minimum number of visible bottles based on the given conditions.
Note: Optimize your logic to avoid Time Limit Exceed error.
Boundary Condition(s):
1 <= N <= 10^5
1 <= Radius of each bottle <= 10^18
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains an integer representing the minimum number of visible bottles.
Example Input/Output 1:
Input:
8
2 3 1 1 4 5 5 3
Output:
2
Explanation:
The radii of the given 8 bottles are 2 3 1 1 4 5 5 3.
The 3rd bottle(1) can be kept in the 1st bottle(2). Now there are 7 visible bottles are 2, 3, 1, 4, 5, 5, 3.
Similarly, after performing the following operations, the following will be the corresponding visible bottles.
Operation [Visible bottles]
1 -> 3 [2, 3, 4, 5, 5, 3]
2 -> 3 [3, 4, 5, 5, 3]
3 -> 4 [4, 5, 5, 3]
4 -> 5 [5, 5, 3]
3 -> 5 [5, 5]
Finally, there are 2 bottles that are visible. Hence the output is 2.
1 -> 2 -> 3 -> 4 -> 5
1 -> 3 -> 5
Example Input/Output 2:
Input:
11
1 1 5 5 6 7 8 2 3 4 5
Output:
3
Explanation:
There are 3 bottles that are visible. The one possible way is given below.
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
1 -> 5
5
a=int(input())
s=1
k={}
for i in list(map(int,input().split())):
    if not k.get(i):
        k[i]=1
    else:
        k[i]+=1
        s=max(k[i],s)
print(s)
ln = list(int(x) for x in input().strip().split())[0]

arr = list(int(x) for x in input().strip().split())

buf = []; arr.sort()
visible_count = 0

for i in range(ln):
  flag = True
  for j in range(len(buf)):
    if arr[i] > buf[j]:
      buf[j] = arr[i]
      flag = False
      break
  if flag==True:
    buf.append( arr[i] )
    visible_count += 1

print( visible_count )
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
        int n;
        Scanner scan=new Scanner(System.in);
        n=scan.nextInt();
        long arr[]=new long[n];
        for(int i=0;i<n;++i)arr[i]=scan.nextLong();
        
        Arrays.sort(arr);
        
        List<Long> list=new ArrayList<>();
        list.add(arr[0]);
        
        for(int i=1;i<n;++i){
            long top=list.get(0);
            long cur=arr[i];
            list.add(cur);
            if(cur==top)continue;
            list.remove(0);
        }
        System.out.print(list.size());
	}
}
