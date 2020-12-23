Matrix Column-wise Sort
Given a matrix M containing the elements in  R rows and C columns. Sort the matrix elements in ascending order along each column. Print the column-wise sorted matrix in the matrix format.
Input Format:
The first line contains the values of R and C separated by a space.
The next R lines (denote the values of matrix M) each containing C values separated by a space.
Output Format:
R lines contain the column-wise sorted matrix each containing C values separated by a space.
Boundary Conditions:
1 < R, C < 50
Example Input/Output 1:
Input:
2 2
1 0
0 1
Output:
0 0
1 1
Example Input/Output 2:
Input:
3 5
4 8 9 4 1
2 6 1 9 4
0 5 4 2 6
Output:
0 5 1 2 1
2 6 4 4 4
4 8 9 9 6
Python:
a,b=map(int,input().split())
m=[list(map(int,input().split())) for i in range(a)];y=[]
for j in range(b):
    x=[]
    for i in range(a):
        x.append(m[i][j])
    x.sort()
    y.append(x)
z=zip(*y)
s=[list(i) for i in z]
for i in s:
    print(*i)
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
        int r,c;
        Scanner scan=new Scanner(System.in);
        r=scan.nextInt();
        c=scan.nextInt();
        List<PriorityQueue<Integer>> list=new ArrayList<>();
        for(int j=0;j<c;j++)list.add(new PriorityQueue<>());
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                int t=scan.nextInt();
                PriorityQueue<Integer> obj=list.get(j);
                obj.add(t);
            }
        }
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                System.out.print(list.get(j).poll()+" ");
            }
            System.out.println("");
        }
	}
}
