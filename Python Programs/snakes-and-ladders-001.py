Snakes and Ladders - 001
In an R*C matrix, a snake is represented using the letter 'S' and the ladder is represented using the letter 'L'. A kid is playing the Snakes and Ladders game with this matrix and a die which can show from 1 to 6. The game always starts with the pawn in the lower left most cell in the matrix and the aim is to reach or cross the top left most cell by casting the die as many times as required. Based on the number cast in the die, if the pawn lands up in a cell containing a snake, the pawn must move to the immediate lower  row (if it is not in the lowermost row) in the same column. Based on the number cast in the die, if the pawn lands up in a cell containing a ladder, the pawn must move to the immediate upper row in the same column (It may so happen that the pawn is already in the top most row and if it encouters a ladder it is considered to have crossed the matrix). The number of rows R will always be even. Please note that the pawn must travel in a zig zag fashion if it does not encounter any snake or ladder. That is in the Rth row it traverses the matrix from left to right, in the (R-1)th row it traverses from right to left, in the (R-2)th row it traverses from left to right and so on. A cell which does not have any snake or ladder is represented using the character asterisk '*'.
The sequence of numbers cast on the die is given as the input. From this sequence of numbers the program must print only the numbers required for the pawn to reach or cross the top most cell (discarding the additional numbers present in the sequence). The program must print -1 if the numbers in the sequence are not enough for the pawn to reach or cross the top most cell.
Input Format:
The first line contains R and C separated by a space.
Next R lines contains C columns with one of these three values * S L
(R+2)th line containing the numbers cast in the die.
Output Format:
The first line contains -1 or the sequence of numbers sufficient for the pawn to reach or cross the top most cell separated by a space.
Boundary Conditions:
2 <= R <= 50 and is even
2 <= C <= 50
Example Input/Output 1:
Input:
6 6
* S * * * *
* * L S * *
* * * * * *
* * * * L *
* * S * * *
* * * L * *
4 1 1 3 5 4 2 3 6 1 4 2 1 5 3 6

Output:
4 1 1 3 5 4 2 3 6 1 4
Explanation:
The pawn starts from 6th row first column.
4 causes the pawn to move 4 positions right to 6th row 5th column.
1 causes the pawn to  move to 6th row 6th column.
Next 1 causes the pawn to move to 5th row 6th column.
Next 3 causes the pawn to land up in S bringing it to 6th row 3rd column.
5 causes the pawn to move to 5th row 5th column.
4 causes the pawn to land up in 5th row 1st column.
Next 2 causes the pawn to land up in 4th row second column.
Next 3 causes the pawn to land up in 4th row 5th column where ladder is there. Hence it moves to 3rd row 5th column.
Next 6 causes the pawn to land up in 2nd row 2nd column.
Next 1 causes the pawn to land up in L which moves it up to 1st row 3rd column.
Next 4 causes the pawn to reach or cross the top left most cell and hence the output sequence is 4 1 1 3 5 4 2 3 6 1 4
input1 = input().strip().split(" ")
R,C = int(input1[0]), int(input1[1])
Matrix = [input().strip().split(" ") for j in range(R)]
numbers = [int(i) for i in input().strip().split(" ")]
pos = [R-1,-1]
 
def Snake():
    pos[0] = R-1
def Ladder():
    pos[0] -= 1
    
flag = 0

def func():
    if(pos[1] >= C):
        pos[0] -= 1
        pos[1] = pos[1] - C
 
    if(pos[1] < 0):
        pos[0] -= 1
        pos[1] = -pos[1] - 1
    
 
 
for i in numbers:
    flag += 1
    if(pos[0]%2 != 0):
        pos[1] += i
    else:
        pos[1] -= i
    
    func();
    if(Matrix[pos[0]][pos[1]] == "S"):
        Snake()
        func()
        func()
    if(Matrix[pos[0]][pos[1]] == "L"):
        Ladder()
        func()
        func()
    if(Matrix[pos[0]][pos[1]] == "S"):
        Snake()
        func()
        func()
    if(Matrix[pos[0]][pos[1]] == "L"):
        Ladder()
        func()
        func()
        
    if(pos[0] <= 0 and pos[1] <= 0):
        break
 
for i in numbers[:flag]:
    print(i,end = " ")
