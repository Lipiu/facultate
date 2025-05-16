package eu.deic.oop;

public class ProgMainVehicle {
    public static void main(String[] args){
        Vehicle v1 = new Vehicle(3200);
        Vehicle v2 = new Vehicle(4100);

        System.out.println("v1 = " + v1.display());
        System.out.println("v2 = " + v2.display());

        //v2 = v1;

        v1.setWeight(1000);
        System.out.println("v1 = " + v1.display());
        System.out.println("v2 = " + v2.display());


    }
}
