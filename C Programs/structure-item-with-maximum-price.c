Structure - Item with Maximum Price
N items are passed as the input along with id, name and price. All the N items will have distinct price. Print the item details which has the maximum price. Please fill in the missing lines of code so that the program is executed successfully.
Boundary Condition(s):
2 <= N <= 50
Input Format:
The first line contains the value of N.
The next N lines contain the item id, name and price.
Output Format:
The first line contains the item details which has the maximum price.
Example Input/Output 1:
Input:
3
101 pencil 15
102 bags 505
103 box 100
Output:
102 bags 505
Example Input/Output 2:
Input:
5
500 ice cream 120
501 cake 500
502 chocolates 300
503 pizza 800
504 burger 200
Output:
503 pizza 800
#include<stdio.h>

struct Item
{
    int itemID;
    char itemName[100];
    int itemPrice;
};

int main()
{
    int N;
    scanf("%d", &N);
    struct Item item[N];
    int index = 0;

    // Read the item details

    for(index = 0; index < N; index++)
    {
        scanf("%d %s %d", &item[index].itemID, &item[index].itemName, &item[index].itemPrice);
    }

int maxPrice=item[0].itemPrice,ind=0;
    
    for(int i=1;i<N;++i){
        if(item[i].itemPrice >maxPrice){
            ind=i;
            maxPrice=item[i].itemPrice;
        }
    }
    printf("%d %s %d",item[ind].itemID,item[ind].itemName,maxPrice);
} // end of the main method
