
import java.util.Scanner;

public class question3 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Give an integer to calculate factorial.");
        int n = sc.nextInt(), fact = 1;
        for (int i = 1; i <= n; i++)
            fact *= i;
        System.out.println(fact);
        sc.close();
    }
}
