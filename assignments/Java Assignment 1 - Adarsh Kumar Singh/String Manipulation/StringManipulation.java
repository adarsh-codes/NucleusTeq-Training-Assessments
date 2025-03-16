import java.util.Arrays;
import java.util.Scanner;

public class StringManipulation {
    
    // Method to reverse a string
    public static String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }

    // Method to count the number of vowels in a string
    public static int countVowels(String str) {
        int count = 0;
        str = str.toLowerCase(); 
        for (char ch : str.toCharArray()) {
            if ("aeiou".indexOf(ch) != -1) {
                count++;
            }
        }
        return count;
    }

    // Method to check if two strings are anagrams
    public static boolean areAnagrams(String str1, String str2) {
        if (str1.length() != str2.length()) {
            return false;
        }
        char[] arr1 = str1.toLowerCase().toCharArray();
        char[] arr2 = str2.toLowerCase().toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        return Arrays.equals(arr1, arr2);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a string to reverse: ");
        String inputString = scanner.nextLine();
        System.out.println("Reversed String: " + reverseString(inputString));

        System.out.print("\nEnter a string to count vowels: ");
        String vowelString = scanner.nextLine();
        System.out.println("Number of Vowels: " + countVowels(vowelString));

        System.out.print("\nEnter first string for anagram check: ");
        String str1 = scanner.nextLine();
        System.out.print("Enter second string for anagram check: ");
        String str2 = scanner.nextLine();
        if (areAnagrams(str1, str2)) {
            System.out.println("The strings are anagrams.");
        } else {
            System.out.println("The strings are NOT anagrams.");
        }

        scanner.close();
    }
}
