package eu.ase.lab3;

public class Aircraft implements Flight, Cloneable{
    private int weight;
    private static int aircraftNo = 10;

    public Aircraft(int weight) {
        this.weight = weight;
    }

    public int getWeight() {
        return weight;
    }

    public static int getAircraftNo() {
        return aircraftNo;
    }

    public static void setAircraftNo(int aircraftNo) {
        Aircraft.aircraftNo = aircraftNo;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public void printAircraft(){
        System.out.println("Aircraft");
    }

    @Override
    public void takeOff() {
        System.out.println("Aircraft is taking off...");
    }

    @Override
    public void land() {
        System.out.println("Aircraft is landing...");
    }

    @Override
    public Helicopter clone() {
        return Helicopter(this.getWeight(), this.rotorBladeNo);
    }
}