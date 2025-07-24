import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

public class SortStudents {

    public static class Student {
        int id;
        String name;
        double grade;

        public Student(String id, String name, String grade) {
            this.id = Integer.parseInt(id);
            this.name = name;
            this.grade = Double.parseDouble(grade);
        }

        @Override
        public String toString(){
            return id + "," + name + "," + grade+ "\n";
        }

        public int getId() {
            return id;
        }
    }

    public static List<List<String>> readCSV(String csvFile) {
        try {
             return Files.readAllLines(Paths.get(csvFile))
                    .stream().map(line -> Arrays.asList(line.split(",")))
                    .toList();

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static List<Student> returnSortedStudents(List<List<String>> data) {
        List<Student> sortedStudents = new ArrayList<>();

        for (List<String> line : data) {
            Student student = new Student(
                    line.get(0),
                    line.get(1),
                    line.get(2)
            );
            sortedStudents.add(student);
        }

        sortedStudents.sort(Comparator.comparing(Student::getId));

        return sortedStudents;
    }

    public static void writeToCSV(String sortedCSVFile, List<Student> sortedStudentsList){
        try {
            Path path = Paths.get(sortedCSVFile);
            if (!Files.exists(path)) {
                Files.createFile(path);
            }
            FileWriter fileWriter = new FileWriter(sortedCSVFile);
            for (Student student : sortedStudentsList) {
                fileWriter.write(student.toString());
            }
            fileWriter.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        List<List<String>> readData = readCSV("studentGrades.csv");
        List<Student> studentList = returnSortedStudents(readData);
        writeToCSV("studentGradesSorted.csv", studentList);
    }

}
