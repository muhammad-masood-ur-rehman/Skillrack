Knight Kills King
Knight Kills King: A knight in a chess game is determined to kill the enemy king. The chess board is of the size N*N. The knight can move through the empty cells but he cannot land on a cell where friendly units are placed. The knight is represented as K, the friendly units are represented as F, the enemy king is represented as E and the empty cells are represented as X. Find the minimum number of moves needed for the knight to reach the enemy king. The knight moves to a square that is two squares away horizontally and one square vertically, or two squares vertically and one square horizontally. The complete move therefore looks like the letter L.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains N.
The next N lines represent the chess board.
Output Format:
The first line contains the minimum number of moves required to reach the enemy king by the knight.
Example Input/Output 1:
Input:
5
KXXXX
XXXXX
XXXXX
XXXEX
XXXXX
Output:
2
Example Input/Output 2:
Input:
7
EXXXXXX
XXXXXXX
FFXXXXX
XXKXXXX
FXXXXFX
XXXXXXX
XXXXXXX
Output:
3
Max Execution Time Limit: 5000 millisecs
#include <bits/stdc++.h> 
using namespace std;
char arr[1000][1000];
struct cell { 
	int x, y; 
	int dis; 
	cell() {} 
	cell(int x, int y, int dis) : x(x), y(y), dis(dis) {} 
};
bool isInside(int x, int y, int Num) {
    return (x >= 0 && x < Num && y >=0 && y < Num);
} 
int minStepToReachTarget(int Num,int kx,int ky,int ex,int ey) 
{
	int dx[] = { -2, -1, 1, 2, -2, -1, 1, 2 }; 
	int dy[] = { -1, -2, -2, -1, 1, 2, 2, 1 };
	queue<cell> q;
	q.push(cell(kx, ky, 0)); 

	cell t; 
	int x, y; 
	bool visit[Num + 1][Num + 1];
	for (int ele = 1; ele <= Num; ele++){
		for (int foo = 1; foo <= Num; foo++){
			visit[ele][foo] = false;
		}
	}
	visit[kx][ky] = true;
	while (!q.empty()) { 
		t = q.front(); 
		q.pop();
		if (t.x == ex && t.y == ey){ 
			return t.dis;
		}
		for (int ele = 0; ele < 8; ele++){ 
			x = t.x + dx[ele]; 
			y = t.y + dy[ele]; 
			if (isInside(x, y, Num) && !visit[x][y]&&arr[x][y]!='F') { 
				visit[x][y] = true; 
				q.push(cell(x, y, t.dis + 1)); 
			} 
		} 
	} 
} 

int main(){
    int num,x,y,ex,ey;
    scanf("%d",&num);
    for(int ele=0;ele<num;ele++){
        for(int foo=0;foo<num;foo++){
            scanf(" %c ",&arr[ele][foo]);
            if(arr[ele][foo]=='K'){
                x=ele;
                y=foo;
            }
            if(arr[ele][foo]=='E'){
                ex=ele;
                ey=foo;
            }
        }
    }
    cout << minStepToReachTarget(num,x,y,ex,ey); 
} 
