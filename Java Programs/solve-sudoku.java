Solve Sudoku
The program must accept an integer matrix of size 9x9 representing a sudoku as the input. The sudoku matrix contains the integers from 0 to 9 where 0 represents the empty cells. If the sudoku matrix is valid, the program must fill in the empty cells of the sudoku matrix and print it as the output. Else the program must print Not Solved as the output.
Sudoku:
Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contain all of the digits from 1 to 9.
Input Format:
The first 9 lines each contain 9 integers separated by a space.
Output Format:
The first 9 lines each contain 9 integers separated by a space or the first line contains Not Solved.
Example Input/Output 1:
Input:
0 0 0 2 6 0 7 0 1
6 8 0 0 7 0 0 9 0
1 9 0 0 0 4 5 0 0
8 2 0 1 0 0 0 4 0
0 0 4 6 0 2 9 0 0
0 5 0 0 0 3 0 2 8
0 0 9 3 0 0 0 7 4
0 4 0 0 5 0 0 3 6
7 0 3 0 1 8 0 0 0
Output:
4 3 5 2 6 9 7 8 1
6 8 2 5 7 1 4 9 3
1 9 7 8 3 4 5 6 2
8 2 6 1 9 5 3 4 7
3 7 4 6 8 2 9 1 5
9 5 1 7 4 3 6 2 8
5 1 9 3 2 6 8 7 4
2 4 8 9 5 7 1 3 6
7 6 3 4 1 8 2 5 9
Example Input/Output 2:
Input:
0 6 0 3 0 0 8 0 4
5 3 7 0 9 0 0 0 0
0 4 0 0 0 6 3 0 7
0 9 0 0 5 1 2 3 8
0 0 0 0 0 0 0 0 0
7 1 3 6 2 0 0 4 0
3 0 6 4 0 0 0 1 0
0 0 0 0 6 0 5 2 3
1 0 2 0 0 3 0 8 0
Output:
Not Solved
import java.util.*;
class Slot{
    int r,c;
}
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        int mat[][]=new int[9][9];
        
        for(int i=0;i<9;++i){
            for(int j=0;j<9;++j){
                mat[i][j]=scan.nextInt();
            }
        }
        if(solve(mat)){
            for(int i=0;i<9;++i){
                for(int j=0;j<9;++j){
                    System.out.printf("%d ",mat[i][j]);
                }
                System.out.println("");
            }
        }
        else{
            System.out.print("Not Solved");
        }
	}
	public static boolean solve(int mat[][]){
	    Slot slot=getnextslot(mat);
	    if(slot==null){
	        return true;
	    }
	    for(int digit=1;digit<=9;++digit){
	        if(rowpossible(mat,slot,digit) && colpossible(mat,slot,digit) &&
	            submatpossilbe(mat,slot,digit)){
	                mat[slot.r][slot.c]=digit;
	                if(solve(mat)){
	                    return true;
	                }
	                mat[slot.r][slot.c]=0;
	            }
	    }
	    return false;
	}
	public static Slot getnextslot(int mat[][]){
	    for(int i=0;i<9;++i){
	        for(int j=0;j<9;++j){
	            if(mat[i][j]==0){
	                Slot slot=new Slot();
	                slot.r=i;
	                slot.c=j;
	                return slot;
	            }
	        }
	    }
	    return null;
	}
	public static boolean rowpossible(int mat[][],Slot slot,int digit){
	    for(int i=0;i<9;++i)if(mat[slot.r][i]==digit)return false;
	    return true;
	}
	public static boolean colpossible(int mat[][],Slot slot,int digit){
	    for(int i=0;i<9;++i)if(mat[i][slot.c]==digit)return false;
	    return true;
	}
	public static boolean submatpossilbe(int mat[][],Slot slot,int digit){
	    int currentr=(slot.r/3) *3;
	    int currentc=(slot.c/3) *3;
	    for(int i=currentr;i<=currentr+2;++i){
	        for(int j=currentc;j<=currentc+2;++j){
	            if(mat[i][j]==digit){
	                return false;
	            }
	        }
	    }
	    return true;
	}
}
