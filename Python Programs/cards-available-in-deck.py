Cards Available in Deck
There are 52 cards in a standard deck of cards. There are four suits Clubs(C), Diamonds(D), Hearts(H) and Spades(S) each containing 13 cards. The 13 cards in each suit are A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q and K. The program must accept the names of N cards as the input. The name of each card contains the rank followed by its suit. The program must print the output based on the following conditions.
- The program must print "C - " and the cards available in the suit Clubs.
- The program must print "D - " and the cards available in the suit Diamonds.
- The program must print "H - " and the cards available in the suit Hearts.
- The program must print "S - " and the cards available in the suit Spades.
- If there are no cards for a suit, then the program must print an asterisk (*).
- The names of the cards must be printed in sorted order based on their rank.
Boundary Condition(s):
1 <= N <= 52
Input Format:
The first line contains N.
The second line contains the names of N cards separated by a space.
Output Format:
The first four lines, each contains the name of a suit and the cards available in the suit based on the given conditions.
Example Input/Output 1:
Input:
10
AD 2D 3D 4S 5C 6C JH QH KH AH
Output:
C - 5 6
D - A 2 3
H - A J Q K
S - 4
Explanation:
Here N=10.
The given 10 cards are AD, 2D, 3D, 4S, 5C, 6C, JH, QH, KH and AH.
Suit C contains 2 cards - 5C 6C.
Suit D contains 3 cards - AD 2D 3D.
Suit H contains 4 cards - AH JH QH KH.
Suit S contains 1 card - 4S.
Hence the output is
C - 5 6
D - A 2 3
H - A J Q K
S - 4
Example Input/Output 2:
Input:
7
JS 5H 8C 2S 6H KC KH
Output:
C - 8 K
D - *
H - 5 6 K
S - 2 J
n=int(input())
c=input().split()
for s in 'CDHS':
    print(s,end=" - ")
    h=0 
    for r in 'A 2 3 4 5 6 7 8 9 10 J Q K'.split():
        if r+s in c:
            print(r,end=" ")
            h=1 
    if h==0:
        print('*',end=" ")
    print()
