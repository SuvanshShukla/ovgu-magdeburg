import java.util.Iterator;

class Game {
  // --------------------------------------------------------------- //
  public static void printWelcomScreen() {
    System.out.println("Welcome to Monster World!");
  }

  // --------------------------------------------------------------- //
  public static MonsterDatabase initDatabase() {
    MonsterDatabase db = new MonsterDatabase();
    if (db.initDatabase("monsters.txt")) {
      System.out.println("database loaded \n");
      return db;
    }
    System.out.println("database initialization failed \n");
    return null;
  }

  // --------------------------------------------------------------- //
  public static void showAllMonsters(MonsterDatabase db) {
    ConsoleVisualizer visualizer = new ConsoleVisualizer();
    Iterator<Monster> iter = db.iterator();
    while (iter.hasNext()) {
      visualizer.visualize(iter.next());
    }
  }

  // --------------------------------------------------------------- //
  public static void main(String[] args) {
    printWelcomScreen();
    MonsterDatabase db = initDatabase();
    if (db != null) {
      showAllMonsters(db);
    } else {
      System.out.println("Something went wrong.");
    }
  }
}