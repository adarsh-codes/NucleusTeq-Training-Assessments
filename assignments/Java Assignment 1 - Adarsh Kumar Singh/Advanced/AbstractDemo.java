// Abstract class example
abstract class Animal {
    abstract void makeSound(); 

    public void sleep() {
        System.out.println("Sleeping...");
    }
}

// Interface example
interface Pet {
    void play();
}

// Dog class demonstrating both Abstract Class and Interface
class Dog extends Animal implements Pet {
    @Override
    void makeSound() {
        System.out.println("Dog barks.");
    }

    @Override
    public void play() {
        System.out.println("Dog is playing.");
    }
}

// Main class
public class AbstractDemo {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.makeSound();
        myDog.play();
        myDog.sleep();
    }
}
