Corona Virus
An integer matrix of size RxC containing only the values 0, 1 and 2 is given as the input to the program. The value 0 indicates an empty space, the value 1 indicates a person is healthy and the value 2 indicates a person is infected by the corona virus. Every day the virus is spread from infected person to other persons (all four adjacent persons). The program must print the minimum number of days required to spread the coronavirus to all individuals. If all the persons can not be affected by the corona virus, the program must print -1 as the output.
Boundary Condition(s):
1 <= R, C <= 1000
Input Format:
The first line contains R and C separated by a space.
The next R lines, each containing C integers separated by a space.
Output Format:
The first line contains -1 or the minimum number of days required to spread the coronavirus to all individuals.
Example Input/Output 1:
Input:
3 5
2 1 0 2 1
1 0 1 2 1
1 0 0 2 1
Output:
2
Explanation:
After Day 1:
2 2 0 2 2
2 0 2 2 2
1 0 0 2 2
After Day 2:
2 2 0 2 2
2 0 2 2 2
2 0 0 2 2
Example Input/Output 2:
Input:
3 5
2 1 0 2 1
0 0 1 2 1
1 0 0 2 1
Output:
-1
public class Main {

    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        int r=scan.nextInt(),c=scan.nextInt();
        
        int arr[][]=new int[r][c];
        for(int i=0;i<r;++i)for(int j=0;j<c;++j)arr[i][j]=scan.nextInt();
        
        int days=0;
        Queue<Integer> q=new ArrayDeque<>();
        int healthy=0;
        
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                if(arr[i][j]==2){
                    q.add((i*c) + j);
                }
                else if(arr[i][j]==1){
                    healthy++;
                }
            }
        }
        q.add(-1);
        while(!q.isEmpty()){
            int current=q.poll();
            if(current==-1){
                if(!q.isEmpty()){
                    days++;
                    q.add(-1);
                }
                continue;
            }
            int row=current/c;
            int col=current%c;
            if(row!=0 && arr[row-1][col]==1){
                arr[row-1][col]=2;
                q.add(((row-1)*c)+col);
                healthy--;
            }
            if(row!=r-1 && arr[row+1][col]==1){
                arr[row+1][col]=2;
                q.add((row+1)*c+col);
                healthy--;
            }
            if(col!=0 && arr[row][col-1]==1){
                arr[row][col-1]=2;
                q.add(row*c+(col-1));
                healthy--;
            }
            if(col!=c-1 && arr[row][col+1]==1){
                arr[row][col+1]=2;
                q.add(row*c + (col+1));
                healthy--;
            }
        }
        System.out.print(healthy==0? days: -1);
	}
}
