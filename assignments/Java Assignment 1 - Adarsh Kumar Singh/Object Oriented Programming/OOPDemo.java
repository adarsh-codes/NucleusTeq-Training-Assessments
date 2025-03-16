// Base class - Student
class Student {
    private String name;
    private int rollNumber;
    private double marks;

    // Constructor
    public Student(String name, int rollNumber, double marks) {
        this.name = name;
        this.rollNumber = rollNumber;
        this.marks = marks;
    }

    // Getter methods (Encapsulation)
    public String getName() {
        return name;
    }

    public int getRollNumber() {
        return rollNumber;
    }

    public double getMarks() {
        return marks;
    }

    // Setter method with validation
    public void setMarks(double marks) {
        if (marks >= 0 && marks <= 100) {
            this.marks = marks;
        } else {
            System.out.println("Invalid marks! Enter a value between 0 and 100.");
        }
    }

    // Method Overloading
    public void displayInfo() {
        System.out.println("Student Name: " + name);
        System.out.println("Roll Number: " + rollNumber);
        System.out.println("Marks: " + marks);
    }

    public void displayInfo(String extraInfo) { // Overloaded method
        displayInfo();
        System.out.println("Extra Info: " + extraInfo);
    }
}

class GraduateStudent extends Student {
    private String specialization;

    public GraduateStudent(String name, int rollNumber, double marks, String specialization) {
        super(name, rollNumber, marks); // Calling parent class constructor
        this.specialization = specialization;
    }

    @Override
    public void displayInfo() {
        super.displayInfo(); // Call parent method
        System.out.println("Specialization: " + specialization);
    }
}

public class OOPDemo {
    public static void main(String[] args) {
        Student student = new Student("Alice", 101, 89.5);
        System.out.println("Student Details:");
        student.displayInfo();

        GraduateStudent gradStudent = new GraduateStudent("Bob", 201, 92.0, "Computer Science");
        System.out.println("\nGraduate Student Details:");
        gradStudent.displayInfo();

        // Demonstrating Encapsulation
        System.out.println("\nUpdating Student Marks using Encapsulation...");
        student.setMarks(95.0); 
        System.out.println("Updated Marks: " + student.getMarks());
    }
}
