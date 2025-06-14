import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {
  public static void main(String[] args) {

    Scanner input = new Scanner(System.in);
    System.out.println("Rock-paper-scissors");
    System.out.println("===================");
    System.out.println("Choose your weapon!");
    System.out.println("(1) Scissors");
    System.out.println("(2) Rock");
    System.out.println("(3) Paper");

    int choice = 0;
    while (choice < 1 || choice > 3) {
      System.out.print("Input:");
      choice = input.nextInt();
    }
    input.close();

    System.out.print("You chose ");

    printChoice(choice);

    Random random = new Random();
    int enemy = random.nextInt(3) + 1;

    System.out.print("Your opponent chose ");

    printChoice(enemy);

    printOutcome(choice, enemy);

  }

  public static void printChoice(int choice) {
    switch (choice) {
      case 1: {
        System.out.print("scissors");
      }
      break;
      case 2: {
        System.out.print("rock");
      }
      break;
      case 3: {
        System.out.print("paper");
      }
      break;
    }

    System.out.println(" as wepaon.");
  }

  public static void printOutcome(int choice, int enemy) {

    if (choice == enemy) {
      System.out.println("Draw!");
      return;
    } else {
      if(choice == 1 && enemy == 2) {
        System.out.println("You Win!");
      } else if (choice == 2 && enemy == 3) {
      }
    }

    switch (choice) {
      case 1: {
        if (enemy == 1) {
          System.out.println("Draw!");
          return;
        }

        if (enemy == 2) {
          System.out.println("You lose!");
          return;
        }

        if (enemy == 3) {
          System.out.println("You win!");
          return;
        }
      }
      break;
      case 2: {

        if (enemy == 1) {
          System.out.println("You win!");
          return;
        }

        if (enemy == 2) {
          System.out.println("Draw!");
          return;
        }

        if (enemy == 3) {
          System.out.println("You lose!");
          return;
        }
      }
      break;
      case 3: {
        if (enemy == 1) {
          System.out.println("You lose!");
          return;
        }

        if (enemy == 2) {
          System.out.println("You win!");
          return;
        }

        if (enemy == 3) {
          System.out.println("Draw!");
          return;
        }
      }
      break;
    }
  }
}