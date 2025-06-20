public class ComputeTax {

  public static double calculateTax(double income) {
    if (income <= 10000) {
      return 0;
    } else if (income <= 20000) {
      return (income - 10000) * 0.10;
    } else if (income <= 30000) {
      return (income - 20000) * 0.20 + 1000;
    } else {
      return (income - 30000) * 0.30 + 1000 + 2000;
    }
  }

  // --- Insert Code below 
  public static boolean testCalculation() {
		if (calculateTax(100) != 0.00){
			return false;
		} else if (calculateTax(15000) != 500) {
			return false;
		} else if (calculateTax(25000) != 2000) {
			return false;
		} else if (calculateTax(999999) != 293999.7) {
			return false;
		}
    return true;
  }

  // --- Insert Code above

  public static void main(String args[]) {
    if (testCalculation()) {
      System.out.println("Alle Tests bestanden.");
    } else {
      System.out.println("Die Berechnung ist fehlerhaft.");
    }
  }
}
