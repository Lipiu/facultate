package eu.ase.threads;

public class Main {
    public static void main(String[] args) {
        ThreadNonSync thread1 = new ThreadNonSync("thread1");
        ThreadNonSync thread2 = new ThreadNonSync("thread2");

        System.out.println("Threads when not in sync:\n");
        try {
            thread1.start();
            thread2.start();
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        ThreadSync thread1s = new ThreadSync("thread1sync");
        ThreadSync thread2s = new ThreadSync("thread2sync");

        thread1s.start();
        thread2s.start();

        try {
            thread1s.join();
            thread2s.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        System.out.println("\nProgram finished executing successfully!");
    }
}
