Street Travel Count
Mr.X has a bike and is travelling in a town which has N horizontal (West to East direction) and N vertical (North to South direction) streets. At the meeting junctions of these horizontal and vertical streets there may be a block. If there is a block Mr.X can take diversion to any other street and travel to his destination. A value of 1 indicates that a junction (meeting point of two roads) is NOT blocked and a value of 0 indicates that a junction is blocked. The streets are numbered from 0 to N-1 (similar to array indices). The source (starting junction of Mr.X and the destination junctions details are passed as the input. The program must print the number of streets through which Mr.X must travel to travel from the source to destination.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains N.
The next N lines each containing N values 1 or 0 separated by a space.
The (N+2)nd line contains the source junction co-ordinates separated by a space.
The (N+3)rd line contains the destination junction co-ordinates separated by a space.
Output Format:
The number of streets Mr.X must travel to travel from source to destination.
Example Input/Output 1:
Input:
3
1 0 1
1 0 1
1 1 1
0 0
0 2
Output:
3
Explanation:
The source is (0,0) indicated as S and the destination (0,2) by D.
S 0 D
1 0 1
1 1 1
0 implies block. Hence Mr.X must travel along 1s. Hence the path to travel is denoted by letter P from S to D.
S 0 D
P 0 P
P P P
Hence we can notice that Mr.X must travel through 3 streets to reach the destination.
Example Input/Output 2:
Input:
4
1 1 1 0
0 0 1 1
1 1 0 1
0 1 1 1
0 1
2 0
Output:
7
Explanation:
The path denoted by the letter P is
1 S P 0
0 0 P P
D P 0 P
0 P P P
Hence we can notice that Mr.X must travel through 7 streets to reach the destination.
Example Input/Output 3:
Input:
4
1 1 1 0
0 0 1 1
1 1 0 1
0 1 1 1
0 1
2 1
Output:
6
import java.util.*;
public class Main {
    static int n;
    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        n=scan.nextInt();
        int arr[][]=new int[n][n];
        
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j){
                arr[i][j]=scan.nextInt();
            }
        }
        int src=(scan.nextInt()*n )+scan.nextInt();
        int dest=(scan.nextInt()*n)+scan.nextInt();
        
        boolean visited[]=new boolean[n*n];
        Queue<Integer> q=new ArrayDeque<>();
        int streets[]=new int[n*n];
        
        q.add(src);
        streets[src]=0;
        visited[src]=true;
        
        while(!q.isEmpty()){
            int node=q.poll();
            ArrayList<Integer> list=getRelatedNodes(arr,node);
            for(int i=0;i<list.size();++i){
                int presentNode=list.get(i);
                if(visited[presentNode])continue;
                q.add(presentNode);
                streets[presentNode]=streets[node]+1;
                visited[presentNode]=true;
                if(presentNode==dest){
                    System.out.print(streets[presentNode]);
                    return;
                }
            }
        }
        
        
	}
	public static ArrayList<Integer> getRelatedNodes(int arr[][],int node){
	    ArrayList<Integer> list=new ArrayList<>();
	    int cRow=node/n;
	    int cCol=node%n;
	    for(int i=cRow;i<n;++i){
	        if(arr[i][cCol]==1){
	            list.add((i*n)+cCol);
	        }
	        else break;
	    }
	    for(int i=cRow;i>=0;--i){
	        if(arr[i][cCol]==1){
	            list.add((i*n)+cCol);
	        }
	        else break;
	    }
	    for(int j=cCol;j<n;++j){
	        if(arr[cRow][j]==1){
	            list.add((cRow*n)+j);
	        }
	        else break;
	    }
	    for(int j=cCol;j>=0;--j){
	        if(arr[cRow][j]==1){
	            list.add((cRow*n)+j);
	        }
	        else break;
	    }
	    return list;
	}
}
