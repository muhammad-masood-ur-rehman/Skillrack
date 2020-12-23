Max Value Bags Carry Capacity
Max Value Bags Carry Capacity: A man has the capacity to lift only C kilograms. There are N bags containing grocery items to be carried to yet another location. The weight of the bags are distinct (that is the weight of each bag is different from yet another bag). There is a price tag on each bag denoting the value of the bag. The program must calculate the maximum value that can be transported by the man in his first trip considering the fact that he can lift only C kilograms in a trip. Then the program must print the weight of the bags (in the same order of input) to be carried so that the value carried in the first trip is maximum.
Boundary Condition(s):
1 <= N <= 50
1 <= C <= 10000
1 <= Weight of a bag <= 1000
1 <= Value of price tag on a bag <= 1000
Input Format:
The first line contains N and C separated by a space.
The next N lines contain the weight of the related bag and it's price tag value separated by a space.
Output Format:
The weight of the bags to be carried in the first trip so that the value carried is maximum.
Example Input/Output 1:
Input:
4 8
2 3
5 6
4 7
3 2
Output:
2 4
Explanation:
Here N=4 and C=8.
The man carry a maximum of 8 kilograms. There are 4 bags.
The weight of the 1st bag is 2 kgs and the value is 3.
The weight of the 2nd bag is 5 kgs and the value is 6.
The weight of the 3rd bag is 4 kgs and the value is 7.
The weight of the 4th bag is 3 kgs and the value is 2.
So now when he carries the bags with weight 2 kgs and 4 kgs, the value is maximum 3+7 = 10.
Note:
-When he carries the bags with weight 2 kgs and 5 kgs, the value is 3+6=9 (which is less than 10).
-When he carries the bags with weight 3 kgs and 5 kgs, the value is 2+6=8 (which is less than 10).
-When he carries the bags with weight 3 kgs and 4 kgs, the value is 2+7=9 (which is less than 10).
#include <stdio.h>
int max(int a, int b){
    return (a > b) ? a : b;
}
void kp(int W, int wt[], int val[], int n,int p[]) 
{ 
	int i, w,h=0; 
	int K[n + 1][W + 1];
	for (i = 0; i <= n; i++) { 
		for (w = 0; w <= W; w++) { 
			if (i == 0 || w == 0) 
				K[i][w] = 0; 
			else if (wt[i - 1] <= w) 
				K[i][w] = max(val[i - 1] + 
					K[i - 1][w - wt[i - 1]], K[i - 1][w]); 
			else
				K[i][w] = K[i - 1][w]; 
		} 
	}int res = K[n][W];	 
	w = W; 
	for (i = n; i > 0 && res > 0; i--) {
		if (res == K[i - 1][w]) 
			continue;		 
		else {
			p[h++]=wt[i-1];
			res = res - val[i - 1]; 
			w = w - wt[i - 1]; 
		} 
	} 
}
int main(){
    int n,w;
    scanf("%d%d",&n,&w);
    int a[n],b[n],c[n];
    for(int i=0;i<n;i++){
        scanf("%d%d",&a[i],&b[i]);
        c[i]=0;
    }
    kp(w,a,b,n,c);
    for(int i=n-1;i>=0;i--){
        if(c[i]!=0)
        printf("%d ",c[i]);
    }
} 
