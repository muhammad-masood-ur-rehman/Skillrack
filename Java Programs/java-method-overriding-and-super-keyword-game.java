JAVA - Method Overriding and Super Keyword - Game
The main method class Hello.java is given below.
import java.util.Scanner;
public class Hello {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int round1Score = scan.nextInt();
        int round2Score = scan.nextInt();
        Round1 game = new Round2(round1Score, round2Score);
        System.out.println(game.getTotalScore());
    }
}
Please write the code for the classes Round1.java and Round2.java so that the program prints the output as mentioned below.
Example Input/Output:
Input:
5 4
Output:
9
Round2null
public class Round2 extends Round1{
    int score;
    Round2(int Round1Score, int Round2Score){
        super(Round2Score);
        this.score = Round1Score;
    }
    public int getTotalScore(){  
        return score+super.getTotalScore();
    }
}
Round1.java
public class Round1 {
    int score;
    Round1(int score){
        this.score = score;
    }
    public int getTotalScore(){     
        return score;
    }
}
