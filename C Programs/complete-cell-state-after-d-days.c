Complete Cell State After D Days
There is a colony of 8 cells arranged in a straight line where each day every cell competes with its adjacent cells(neighbours). Each day, for each cell, if it's neighbours are both active or both inactive, the cell becomes inactive the next day, otherwise it becomes active the next day.
The two cells at the ends have only single adjacent cell, so the other imaginary adjacent cell can be assumed to be always inactive.
On a given day, even after updating the cell state, consider it's previous day's state for updating the state of other cells.
Complete the function cellComplete which takes an 8 element array of integer cells representing the current state of 8 cells and an integer D days representing the number of days to simulate.
An integer value of 1 represents an active cell and value of 0 represents an inactive cell.
Input Format:
The first line contains 8 integer values representing the initial state of the cells.
The second line contains D - which represents the number of days.
Output Format:
The first line contains the state of the cells after D days.
Boundary Conditions:
1 <= D <= 1000
Example Input/Output 1:
Input:
1 0 0 0 0 1 0 0
3
Output:
0 0 1 1 1 0 1 0
Example Input/Output 2:
Input:
1 0 0 0 0 1 0 0
2
Output:
1 0 1 1 0 0 0 1
#include <stdio.h>
//As the CELL COUNT IS FIXED as 8
#define CELLSCOUNT 8

int* cellComplete(int* cells, int days) {
    int arr[8]={0};
    while(days>0){
        arr[0]=cells[1]!=0;
        for(int i=1;i<7;++i){
            arr[i]=cells[i-1]!=cells[i+1];
        }
        arr[7]=cells[6]!=0;
        for(int i=0;i<8;++i){
            cells[i]=arr[i];
        }
        days--;
    }
    return cells;
}
 int main() {
        int cells[CELLSCOUNT];

        //Accept the input for the cell values
        int index;
        for (index = 0; index < CELLSCOUNT; index++) {
            scanf("%d",&cells[index]);
        }

        int DAYS;
        scanf("%d",&DAYS); //Get the number of days
        int* modified = cellComplete(cells, DAYS);

        //Print the modified cell values
        for (index = 0; index < CELLSCOUNT; index++) {
            printf("%d ",modified[index]);
        }
    }
