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
    System.out.print("You chose ");
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
    System.out.println(" as weapon.");
    Random random = new Random();
    int enemy = random.nextInt(3) + 1;
    System.out.print("Your opponent chose ");
    switch (enemy) {
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
    switch (choice) {
      case 1: {
        if (enemy == 1) {
          System.out.println("Draw!");
          input.close();
          return;
        }
        if (enemy == 2) {
          System.out.println("You lose!");
          input.close();
          return;
        }
        if (enemy == 3) {
          System.out.println("You win!");
          input.close();
          return;
        }
      }
        break;
      case 2: {
        if (enemy == 1) {
          System.out.println("You win!");
          input.close();
          return;
        }
        if (enemy == 2) {
          System.out.println("Draw!");
          input.close();
          return;
        }
        if (enemy == 3) {
          System.out.println("You lose!");
          input.close();
          return;
        }
      }
        break;
      case 3: {
        if (enemy == 1) {
          System.out.println("You lose!");
          input.close();
          return;
        }
        if (enemy == 2) {
          System.out.println("You win!");
          input.close();
          return;
        }
        if (enemy == 3) {
          System.out.println("Draw!");
          input.close();
          return;
        }
      }
        break;
    }
    System.out.println("ERROR: The program should never arrive here!");
    input.close();
  }
}