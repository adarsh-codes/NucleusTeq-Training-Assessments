import java.io.*;

public class FileIODemo {
    public static void readFile(String filename) {
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            System.out.println("\nReading from file:");
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Error: File not found or cannot be read.");
        }
    }

    public static void main(String[] args) {
        String filename = "sample.txt";
        readFile(filename);
    }
}
