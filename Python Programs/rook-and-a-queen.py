Rook and a Queen
Given the position of a Rook and a queen in a chess board (8X8 board),  write an algorithm and the subsequent Python code to determine the common positions where both rook and queen can be placed in the next move. Rook can move through any number of cells,  either horizontally or vertically. Queens can move through any number of cells,  either horizontally, vertically or diagonally.  Each cell in the chess board may be represented as a 2-tuple (row,col). For example, if the current position of the rook is (3,1) then the next possible position of the rook may be either in the same column {(2,1),(1,1),(4,1),(5,1),(6,1),(7,1),(8,1)} or in the same row {(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8)}. If the queen is in the position (5,3) then it can be placed in the same row {(5,1),(5,2),(5,4),(5,5),(5,6),(5,7),(5,8)} or same column {(1,3),(2,3),(3,3),(4,3),(6,3),(7,3),(8,3)} or along the diagonal of the current position {(6,4),(7,5),(8,6),(4,2),(5,1),(6,2),(7,1),(4,4),(3,5),(2,6),(1,7)}. Then the common cells for next move are {(3,3), (5,1), (7,1)}.
The output is a set of common board positions where both queen and rook can be placed. The positions must be printed in sorted order, sort it by row. When rows are same,  sort it by column.

(Hint: Use built-in function to sort the values)
Input Format: 
Row position of rook
Column position of rook
Row position of queen
Column position of queen
Output Format:
Common position1
Common position2
...
#Reading the inputs
r_rook=int(input())
c_rook=int(input())
r_queen=int(input())
c_queen=int(input())

#Finding the next positions for Rook
positions_rook=[]
for i in range(1,9):
 positions_rook.append((r_rook,i)) #same row
 positions_rook.append((i,c_rook)) #same column
for rc in positions_rook:
 if(rc==(r_rook,c_rook) or rc==(r_queen,c_queen)):
  positions_rook.remove(rc)

#Finding the next positions for Queen
positions_queen=[]
for i in range(1,9):
 positions_queen.append((r_queen,i)) #same row
 positions_queen.append((i,c_queen)) #same column

#For diagonals_Queen
c=c_queen
r=r_queen
while(c!=1 and r!=8):
 positions_queen.append((r+1,c-1))
 r=r+1
 c=c-1
c=c_queen
r=r_queen
while(c!=1 and r!=1):
 positions_queen.append((r-1,c-1))
 r=r-1
 c=c-1
c=c_queen
r=r_queen
while(c!=8 and r!=8):
 positions_queen.append((r+1,c+1))
 r=r+1
 c=c+1
c=c_queen
r=r_queen
while(c!=8 and r!=1):
 positions_queen.append((r-1,c+1))
 r=r-1
 c=c+1

for rc in positions_queen:
 if(rc==(r_rook,c_rook) or rc==(r_queen,c_queen)):
  positions_queen.remove(rc)

final_list=[]
for i in positions_rook:
 if(i in positions_queen):
  final_list.append(i)

x=sorted(final_list)
for i in x:
 print(i)
