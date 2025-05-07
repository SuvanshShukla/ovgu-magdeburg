/* ToDo: import standard java libraries you need e.g. java.io, java.utils, ... */
//Author: Suvansh Shukla
//Matriculation Number: 256245

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
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

      for (int i=0; i<lines.size(); i++){
        if (!lines.get(i).isBlank() && lines.get(i).contains("Monster")) {
          Monster monster = new Monster(
                  lines.get(i+1).replaceFirst("name ",""),
                  (int) Float.parseFloat(lines.get(i+2).replaceFirst("maxHP ","")),
                  Float.parseFloat(lines.get(i+3).replaceFirst("attack ","")),
                  (int) Float.parseFloat(lines.get(i+4).replaceFirst("weight ","")),
                  Float.parseFloat(lines.get(i+5).replaceFirst("multi ",""))
          );
          monsters.add(monster);
        }
      }

    } catch (IOException e) {
      System.out.println("File Not Found.");
    }

      return monsters;
  }

  // --------------------------------------------------------------- //
  public static void main(String[] args) {

    List<Monster> loadedMonsters = loadMonsterFile("./monster_ok.txt");
    List<Monster> failedMonsters = loadMonsterFile("./monster_fail.txt");

    loadedMonsters.addAll(failedMonsters);

    for (Monster monster : loadedMonsters){
      System.out.println(monster.toString());
    }

  }
}
