/* ToDo: import standard java libraries you need e.g. java.io, java.utils, ... */

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MonsterLoader {
  // --------------------------------------------------------------- //
  /**
   * Load the monsters from the given file. If something is wrong with a monster, it is not loaded.
   * The loading process continues with the next monster.
   */
  public static List<Monster> loadMonsterFile(String file_path) {
    /* ToDo: implement this method */

    //initialize an empty list of Monster
    List<Monster> monsters = new ArrayList<>();

    //load file
    Path filePath = Paths.get(file_path);

    try {
      List<String> lines = Files.readAllLines(filePath);

      for (String i : lines){
        System.out.println(i);
      }
    } catch (IOException e) {
      System.out.println("File Not Found.");
    }

      return Collections.emptyList();
  }

  // --------------------------------------------------------------- //
  public static void main(String[] args) {
    /* ToDo: test your code */
    loadMonsterFile("./monster_ok.txt");
  }
}
