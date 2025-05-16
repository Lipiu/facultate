package eu.ase.multithread;

public class MyMultiThreadArray {
    private int[] arr;
    private int startIndex;
    private int stopIndex;
    private Long sum;

    public MyMultiThreadArray(){};

    public MyMultiThreadArray(int[] arr, int startIndex, int stopIndex) {
        this.arr = arr;
        this.startIndex = startIndex;
        this.stopIndex = stopIndex;
    }

    public void run(){
        long s = 0;
        for(int i = startIndex; i < stopIndex; i++){
            s += arr[i];
        }
        this.sum = s;
    }

    public Long getSum() {
        return sum;
    }
}
