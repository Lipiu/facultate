public class Main {
    public static void main(String[] args) {
        ThreadNonSync t1 = new ThreadNonSync("T1");
        ThreadNonSync t2 = new ThreadNonSync("T2");

        t1.start(); // start creates the thread
        t2.start();
    }
}