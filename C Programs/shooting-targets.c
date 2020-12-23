Shooting Targets
N shooting targets are placed in a two dimensional grid and their x and y co-ordinates are provided. The x and y co-ordinates are integer values. When a bullet is fired along a straight line (either parallel to x-axis or y-axis) it eliminates all the targets along it's path. Assuming a bullet can be fired from negative infinity to positive infinity along a straight line parallel to both x and y-axis, find the minimum number of bullets that need to be fired to eliminate all targets.
Boundary Condition(s):
1 <= N <= 100
-100 <= x, y <= 100
Input Format:
The first line contains N.
The next N lines contain two integers(x and y) in each line separated by space(s).
Output Format:
The first line contains the minimum number of bullets that need to be fired to eliminate all targets.
Example Input/Output 1:
Input:
9
4 0
4 1
3 0
2 1
1 1
-2 0
1 2
-1 -1
-2 -1
Output:
4
Explanation:
The first bullet is fired parallel to X-axis through the line Y = 0
The second bullet is fired parallel to X-axis through the line Y = 1
The third bullet is fired parallel to X-axis through the line Y = -1
The fourth bullet is fired parallel to X-axis through the line Y = 2
Example Input/Output 2:
Input:
8
2 3
-5 -1
0 4
1 2
7 2
4 0
3 5
1 1
Output:
7
#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int x[n+1];
    int y[n+1];
    int arr[201][201]={0};
    
    int xaxis[201]={0},yaxis[201]={0};

    for(int i=0;i<n;++i){
        int tempx,tempy;
        scanf("%d%d",&tempx,&tempy);
        tempx=tempx+100;
        tempy=tempy+100;
        arr[tempx][tempy]++;
        x[i]=tempx;
        y[i]=tempy;
        xaxis[tempx]++;
        yaxis[tempy]++;
    }
    
    int counter=0,ans=0;
    
    while(counter!=-1){
        counter=-1;
        int max=0,maxind;
        for(int i=0;i<n;++i){
            if(xaxis[x[i]]>max){
                max=xaxis[x[i]];
                maxind=x[i];
                counter=1;
            }
        }
        for(int i=0;i<n;++i){
            if(yaxis[y[i]]>max){
                max=yaxis[y[i]];
                maxind=y[i];
                counter=2;
            }
        }
        if(counter==1){
            for(int i=0;i<n;++i){
              if(x[i]==maxind){
                arr[maxind][y[i]]--;
                yaxis[y[i]]--;
              }
            }
            xaxis[maxind]=0;
        }
        else if(counter==2){
            for(int i=0;i<n;++i){
              if(y[i]==maxind){
                arr[x[i]][maxind]--;
                xaxis[x[i]]--;
              }
            }
            yaxis[maxind]=0;
            
        }
        ans++;
    }
    printf("%d",ans-1);
    return 0;
}
#include <stdio.h>
struct p{
    int xy,c;
};
int f(int a,struct p *k,int l){
    for(int i=0;i<l;i++){
        if(k[i].xy==a)
        return i;
    }
    return -1;
}
void r(struct p *a,int x,int p[][2],int k,int l,int n){
    for(int i=0;i<n;i++){
        if(p[i][k]==x){
            int h=f(p[i][k^1],a,l);
            a[h].c--;
        }
    }
}
struct p * m(struct p *k,int l){
    struct p *m=k;
    for(int i=1;i<l;i++){
        if(m->c<k[i].c)
        m=k+i;
    }
    return m;
}
int main(){
    int n;
    scanf("%d",&n);
    int p[n][2],xc=0,yc=0,k,t=0,c=0;
    struct p x1[n],y1[n],*tempx,*tempy;
    for(int i=0;i<n;i++){
        scanf("%d%d",&p[i][0],&p[i][1]);
        k=f(p[i][0],x1,xc);
        if(k==-1){
            x1[xc].xy=p[i][0];
            x1[xc++].c=1;
        }
        else
        x1[k].c++;
        k=f(p[i][1],y1,yc);
        if(k==-1){
            y1[yc].xy=p[i][1];
            y1[yc++].c=1;
        }
        else
        y1[k].c++;
    }
    tempy=m(y1,yc);
    tempx=m(x1,xc);
    while(t!=n){
        if(tempx->c>tempy->c){
            t+=tempx->c;
            tempx->c=0;
            r(y1,tempx->xy,p,0,yc,n);
            tempx=m(x1,xc);
        }
        else{
            t+=tempy->c;
            tempy->c=0;
            r(x1,tempy->xy,p,1,xc,n);
            tempy=m(y1,yc);
        }
        c++;
    }
    printf("%d",c);
}
