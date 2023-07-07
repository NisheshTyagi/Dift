package rps;

public class GameManager {
    public String wonDialog;

    private String[] choices = {"Rock","Paper","Scissors"};
    GameManager(String wonDia){
    wonDialog = wonDia;

    }
    public String checkVictory(Player Player1,Player Player2){

        if(Player1.choice == "Rock" && Player2.choice == "Scissors"){
            return Player1.name;
        }
        else if(Player1.choice == "Scissors" && Player2.choice == "Paper"){
            return Player1.name;
        }
        else if(Player1.choice == "Paper" && Player2.choice == "Rock"){
            return Player1.name;
        }
        else{
            return Player2.name;
        }


    }
    public void congratulate(String Winner){
        System.out.printf(wonDialog,Winner);
    }
    public void showChoices(){
        System.out.println("Choose : ");
        for(int i=1;i <= 3;i++){
            System.out.printf("%d ==> %s\n",i,choices[i-1]);
        }
    }

}
