package ro.ase.acs.main;

import ro.ase.acs.classes.Car;

public class Main {
    public static void main(String[] args) {
        Car c1 = new Car("Tesla" , 40000);
        System.out.println(c1);
        System.out.println(c1.getProducer());

        Car c2 = c1;
        c1.setPrice(30000f);
        // 30000 deoarece se face shallow copy
        System.out.println(c2.getPrice());
    }
}