package eu.ase.threads;

public class ThreadSync extends Thread{
    private static final Object myLock = new Object();
    private static int a = 0;
    private static int b = 0;

    public ThreadSync(String name){
        super(name);
    }

    public void printMethod(){
        synchronized(myLock) {
            System.out.println("Thread = " + this.getName() + "; a = " + a + ", b = " + b);
            a++;
            try {
                sleep((int) Math.random() * 1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            b++;
        }
    }

    @Override
    public void run() {
        for(int i = 0; i < 5; i++){
            this.printMethod();
        }
    }
}
