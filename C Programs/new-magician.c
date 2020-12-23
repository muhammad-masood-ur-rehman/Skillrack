New Magician
You are a programming-savvy person and you never get involved in any extra-curricular activities. Your faculty mentor has ordered that you need to give one on-stage performance in the Induction Program for the first years to be held a week later. You were very tensed thinking about it and you could hardly sleep.Just to make you relax, one of your friends took you along with him for P.C.Sorcar Jr.'s magic show.You were very impressed by one of the tricks, so you decided to try to figure out the secret behind it!The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row. Each card has a different number from 1 to 16 written on the side that is showing. Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. Once again, he asks the volunteer which row her card is in. With only the answers to these two questions, the magician then correctly determines which card the volunteer chose. Amazing, right?You decide to write a program to help you understand the magician's technique so that you can also do a magic show during the first year induction program. The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. The rows are numbered 1 to n from top to bottom.Your program should determine which card the volunteer chose; or if there is more than one card the volunteer might have chosen (the magician did a bad job); or if there's no card consistent with the volunteer's answers (the volunteer cheated).
Input Format
Input starts with a line containing an integer: the size of the grid, N. The next line contains the answer to the first question. The next N lines represent the first arrangement of the cards: each line contains N integers, separated by a single space. The next line contains the answer to the second question, and the following N lines contain the second arrangement in the same format.
Output Format
If there is a single card the volunteer could have chosen, print the number on the card. If there are multiple cards the volunteer could have chosen, print "bad", without the quotes. If there are no cards consistent with the volunteer's answers, print "cheat", without the quotes.
Limits:
N is between 4 and 6.1 ≤ both answers ≤ N.
Each number from 1 to N2 will appear exactly once in each arrangement.
Sample Input 1:
4
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16


Sample Output 1:
7
Sample Input 2:
4
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16


Sample Output 2:
bad
Sample Input 3:
 5
2
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
3
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25


Sample Output 3:
cheat
#include<stdio.h>
int main()
{
            int n,i,j,r,r1,c=0,t=0;
            scanf("%d%d",&n,&r);
            int m[n][n],m1[n][n];
            for(i=0;i<n;i++)
            {
                for(j=0;j<n;j++)
                scanf("%d",&m[i][j]);
            }
            scanf("%d",&r1);
            for(i=0;i<n;i++)
            {
                for(j=0;j<n;j++)
                scanf("%d",&m1[i][j]);
            }
            for(i=0;i<n;i++)
            {
                for(j=0;j<n;j++)
                {
                    if(m[r-1][i]==m1[r1-1][j])
                    {c++;
                    t=m1[r1-1][j];}
                }
            }
           
            if(c==0)
            printf("cheat");
            else if(c==1)
            printf("%d",t);
    else
    printf("bad");

            return 0;
}
