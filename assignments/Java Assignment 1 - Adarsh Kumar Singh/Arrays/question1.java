

import java.util.Scanner;

public class question1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();
        
        int[] arr = new int[n];
        int sum = 0;
        
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
            sum += arr[i];
        }
        scanner.close();
        
        double average = (double) sum / n;
        System.out.println("Average of the array elements: " + average);
    }
}
