import java.util.Scanner;

public class question2 {


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("give values for a and b");
        int a = sc.nextInt(), b = sc.nextInt();
        System.out.println("Addition: " + (a + b));
        System.out.println("Logical AND: " + (a > 0 && b > 0));
        System.out.println("a Greater than b: " + (a > b));
        sc.close();
    
}
}
