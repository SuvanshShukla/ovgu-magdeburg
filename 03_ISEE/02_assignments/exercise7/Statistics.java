public class Statistics {
  public static void main(String[] args) {
    int[] d = {6, 21, 16, 11, 17, 26, 16, 7, 13, 22, 5, 9, 29, 14, 18, 10, 1, 5, 5, 23, 24, 4, 1, 12, 28, 3, 8, 30, 19, 24, 25, 7, 11, 1, 20, 9, 26, 7, 7, 7, 3, 6, 18, 5, 10, 22, 25, 13, 24, 12, 22, 26, 10, 22, 17, 1, 24, 18, 27, 18, 1, 29, 18, 12, 29, 17, 24, 26, 22, 15, 23, 25, 23, 28, 11, 4, 20, 14, 21, 17, 25, 2, 24, 16, 30, 1, 29, 13, 13, 30, 28, 25, 9, 23, 11, 1, 29, 29, 17, 4, 12, 25, 13, 8, 13, 19, 13, 25, 28, 22, 30, 20, 21, 13, 29, 24, 23, 3, 29, 5, 19, 11, 25, 4, 8, 7, 10, 17, 29, 21};

    // summieren
    double a = 0.0;

    for (int i = 0; i < d.length; i++) {
      a = a + d[i];
    }

    // divide by number:
    double o = a / d.length;

    System.out.println("Mean value: " + o);

    int sum1 = (int) a;
    System.out.println("Sum: " + sum1);

    // Calculate variance
    double v = 0;

    for (int i = 0; i < d.length; i++) {
      v += Math.pow((double) d[i] - o, 2);
    }

    // durch Anzahl teilen
    // double var = v / (d.length-1);
    double v2 = v / (d.length - 1);

    double stan = Math.sqrt(v2);
    System.out.println("Standard deviation: " + stan);
    System.out.println("Variance: " + v2);

    // Histogram darstellen
    System.out.println();
    System.out.println("Histogram: ");

    int[] q = new int[100]; // Problem if a number occurs more than 100 times

    for (int i = 0; i < d.length; i++) {
      int Zahl = d[i];
      q[Zahl]++; // q counts how often a number occurs
    }

    // display histogram with asterisks
    for (int i = 0; i < q.length; i++)
      if (q[i] > 0) {
        System.out.print(i + ": ");
        for (int j = 0; j < q[i]; j++)  System.out.print("*");
        System.out.println();
      }
 }
}
