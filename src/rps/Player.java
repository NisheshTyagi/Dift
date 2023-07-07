
package rps;
import java.util.Random;
public class Player {
    public String choice;
    public String name;
    Player(String PlayerName){
        name = PlayerName;
    }

    private String[] choices = {"Rock","Paper","Scissors"};
    public void chooseRandom() {
        Random rand = new Random();
        choice = choices[rand.nextInt(3)];
    }
    public void choose(Byte number){
        choice = choices[number];
    }

}
