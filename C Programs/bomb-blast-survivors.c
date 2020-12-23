Bomb Blast Survivors
An N*N grid is passed as input to the program. There are bombs planted in the grid. Each bomb is detonated and destroys all the blocks in its explosion radius (If the radius is 1, the bomb can destroy all the 8 blocks surrounding it). There are people inside the grid represented by P. The bombs are represented by an integer which is the explosion radius of the bombs. The program must print the number of survivors after the explosion of all bombs.
Boundary Condition(s):
1 <= N <= 100
1 <= Explosion radius <= 9
Input Format:
The first line contains N
The next N lines contain N characters each.
Output Format:
The first line contains the count of survivors.
Example Input/Output 1:
Input:
6
**P***
****P*
*P*1**
*****P
***P*P
***PP2
Output:
2
Explanation:
After explosion the grid becomes (X represents exploded area),
**P***
**XXX*
*PX1X*
**XXXX
***XXX
***XX2
Example Input/Output 2:
Input:
6
*2*P**
******
*P*1P*
*P****
*****P
*1*P**
Output:
3
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int num, count = 0;
	scanf("%d", &num);
	char arr[100][101];
	for (int ele = 0; ele < num; ele++)
		scanf("%s", arr[ele]);
	for (int ele = 0; ele < num; ele++)
	{
		for (int foo = 0; foo < num; foo++)
		{
			if (isdigit(arr[ele][foo]))
			{
				int p = arr[ele][foo] - '0';
				int s = ele - p >= 0 ? ele - p : 0, s1 = ele + p < num ? ele + p : num - 1, e = foo - p >= 0 ? foo - p : 0, e1 = foo + p < num ? foo + p : num - 1;
				for (int k = s; k <= s1; k++)
				{
					for (int l = e; l <= e1; l++)
						arr[k][l] = arr[k][l] == '*' || arr[k][l] == 'P' || arr[k][l] == 'p' ? 'X' : arr[k][l];
				}
			}
		}
	}
	for (int ele = 0; ele < num; ele++)
	{
		for (int foo = 0; foo < num; foo++)
			count += (arr[ele][foo] == 'P');
	}
	printf("%d ", count);
}
