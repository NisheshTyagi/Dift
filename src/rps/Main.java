package rps;
import  java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        GameManager game = new GameManager("%s Won!!\n");
        Player player = new Player("Player");
        Player computer = new Player("Computer");

        Scanner scan = new Scanner(System.in);
        System.out.println("Welcome to Rock paper scissors");
        computer.chooseRandom();
        game.showChoices();
        player.choose((byte) (scan.nextByte()-1));
        String winner = game.checkVictory(player,computer);
        System.out.printf("Computer : %s\n",computer.choice);
        game.congratulate(winner);

        }
    }
