package eu.ase.lab3;

public class Main {
    public static void main(String[] args) {
        Aircraft ac1 = new Aircraft(7);
        Helicopter h1 = new Helicopter(5, 4);

        System.out.println(Aircraft.getAircraftNo());


        ac1.printAircraft();
        System.out.println();
        h1.printAircraft();

        h1.takeOff();
        h1.land();
        ac1.takeOff();
        ac1.land();

        Aircraft ac2 = ac1.clone();
        System.out.println(ac2.getWeight());
    }
}