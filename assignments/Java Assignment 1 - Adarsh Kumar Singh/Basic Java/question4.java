import java.util.Scanner;

public class question4 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Write an integer to calculate fibonnaci series upto - ");
        int n = sc.nextInt(), a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            System.out.print(a + " ");
            int temp = a;
            a = b;
            b = temp + b;
        }
        sc.close();
    }
}
