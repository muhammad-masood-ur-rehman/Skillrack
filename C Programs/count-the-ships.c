Count the Ships
Count the Ships: A sea is represented as an N*N matrix where # represents a part of a ship and - represents water. All the ships are surrounded by water. Series of # which are connected together forms a ship. The # can be connected to another # in any of the surrounding 8 cells to form a ship. The program must print the number of ships in the given map.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains N.
The next N lines contain N characters each.
Output Format:
The first line contains the count of the ship.
Example Input/Output 1:
Input:
6
------
-###--
-###--
------
-####-
-####-
Output:
2
Example Input/Output 2:
Input:
8
--#-----
--#-----
--#-----
-----#--
------#-
--#----#
#####---
--#-----
Output:
3
#include<stdio.h>
#include<stdlib.h>
void ship(int num,char arr[num][num+1],int c1,int c2){
    arr[c1][c2]='-';
    for(int ele=c1-1;ele<=c1+1;ele++){
        for(int foo=c2-1;foo<=c2+1;foo++){
            if(ele<0&&ele>=num&&foo>=num&&foo<0)
            continue;
            if(arr[ele][foo]=='#')
            ship(num,arr,ele,foo);
        }
    }
}

int main(){
    int num,ctr=0;
    scanf("%d",&num);
    char arr[num][num+1];
    
    for(int ele=0;ele<num;ele++)
    scanf("%s",arr[ele]);
    
    for(int ele=0;ele<num;ele++){
        for(int foo=0;foo<num;foo++){
            if(arr[ele][foo]=='#'){
                ctr++;
                ship(num,arr,ele,foo);
            }
        }
    }
printf("%d",ctr);
}
