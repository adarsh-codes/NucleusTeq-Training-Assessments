import java.util.Scanner;

public class ExceptionHandlingDemo {
    public static void divideNumbers(int a, int b) {
        try {
            int result = a / b;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Cannot divide by zero!");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter two numbers to divide: ");
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();

        divideNumbers(num1, num2);
        scanner.close();
    }
}
