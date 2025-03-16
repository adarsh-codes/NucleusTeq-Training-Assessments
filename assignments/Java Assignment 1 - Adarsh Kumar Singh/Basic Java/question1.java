import java.util.*;
public class question1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Whose are you want to calculate - circle, rectangle, triangle? Type 1 for circle, 2 for rectangle and 3 for triangle.");

        double calc = sc.nextDouble();

        if(calc == 1){
            System.out.println("Give the radius of circle - ");
            double r = sc.nextDouble();

            System.out.println("Area is - "+3.14*r*r);
        }
        if(calc == 2){
            System.out.println("Give the length and breadth of rectangle - ");
            double l = sc.nextDouble();
            double b = sc.nextDouble();
            System.out.println("Area is - "+l*b);
        }
        if(calc == 3){
            System.out.println("Give the breadth and height of triangle - ");
            double b = sc.nextDouble();
            double h = sc.nextDouble();

            System.out.println("Area is - "+0.5*b*h);
        }
        else{
            System.out.println("Please choose among given options.");
        }

        sc.close();
        
    }
}