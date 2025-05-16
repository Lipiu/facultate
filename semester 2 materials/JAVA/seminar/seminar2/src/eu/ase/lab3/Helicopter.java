package eu.ase.lab3;

public class Helicopter  extends Aircraft {
    private int rotorBladesNo;

    public Helicopter(int weight, int rotorBladesNo){
        super(weight);
        this.rotorBladesNo = rotorBladesNo;
    }

    public int getRotorBladesNo() {
        return rotorBladesNo;
    }

    public void setRotorBladesNo(int rotorBladesNo) {
        this.rotorBladesNo = rotorBladesNo;
    }

    @Override
    public void takeOff() {
        System.out.println("Helicopter is landing....");
    }

    @Override
    public void land() {
        System.out.println("Helicopter is landing...");
    }
}