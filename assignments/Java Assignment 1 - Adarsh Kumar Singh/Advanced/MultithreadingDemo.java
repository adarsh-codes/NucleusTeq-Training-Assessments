class MyThread extends Thread {
    private String threadName;

    public MyThread(String name) {
        this.threadName = name;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(threadName + " - Count: " + i);
            try {
                Thread.sleep(700); 
            } catch (InterruptedException e) {
                System.out.println(threadName + " interrupted.");
            }
        }
    }
}

public class MultithreadingDemo {
    public static void main(String[] args) {
        System.out.println("Starting Threads:");
        MyThread thread1 = new MyThread("Thread A");
        MyThread thread2 = new MyThread("Thread B");

        thread1.start();
        thread2.start();

        try {
            thread1.join(); 
            thread2.join(); 
        } catch (InterruptedException e) {
            System.out.println("Main thread interrupted.");
        }

        System.out.println("\nMain thread finished execution.");
    }
}
