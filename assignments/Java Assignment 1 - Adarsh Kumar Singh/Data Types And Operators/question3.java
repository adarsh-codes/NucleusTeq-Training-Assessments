import java.util.Scanner;

public class question3 {


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter temperature: ");
        double temp = sc.nextDouble();
        
        System.out.println("Convert to (C/F)? ");
        char unit = sc.next().charAt(0);

        if (unit == 'C' || unit == 'c') {
            double celsius = (temp - 32) * 5 / 9;
            System.out.println("Temperature in Celsius: " + celsius);
        } else if (unit == 'F' || unit == 'f') {
            double fahrenheit = (temp * 9 / 5) + 32;
            System.out.println("Temperature in Fahrenheit: " + fahrenheit);
        } else {
            System.out.println("Invalid choice");
        }
        
        sc.close();
    
}

}
