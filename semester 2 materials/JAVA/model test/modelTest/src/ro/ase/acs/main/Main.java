package ro.ase.acs.main;

import ro.ase.acs.models.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws CloneNotSupportedException {
        // Step 4: Create TrainType enum values
        TrainTicket ticket1 = new TrainTicket("Bucuresti", "Iasi", 500, TrainType.REGIO);
        TrainTicket ticket2 = new TrainTicket("Cluj", "Oradea", 150, TrainType.INTERREGIO);
        TrainTicket ticket3 = new TrainTicket("Timisoara", "Arad", 80, TrainType.INTERCITY);

        System.out.println(ticket1);
        System.out.println();
        System.out.println(ticket2);
        System.out.println();
        System.out.println(ticket3);
        System.out.println();

        // Step 6: Test getPrice() with discount logic
        System.out.printf("Ticket1 Price: %.2f\n", ticket1.getPrice());  // 5 * 500 * 0.5
        System.out.printf("Ticket2 Price: %.2f\n", ticket2.getPrice());  // 5 * 150 * 0.25
        System.out.printf("Ticket3 Price: %.2f\n", ticket3.getPrice());  // 5 * 80 * 0
        System.out.println();

        // Step 5: Test getDiscount()
        System.out.println("Ticket1 Discount: " + ticket1.getDiscount());  // 0.5
        System.out.println("Ticket2 Discount: " + ticket2.getDiscount());  // 0.25
        System.out.println("Ticket3 Discount: " + ticket3.getDiscount());  // 0
        System.out.println();

        // Step 6: Test getters
        System.out.println("Departure of Ticket1: " + ticket1.getDeparture());
        System.out.println("Destination of Ticket1: " + ticket1.getDestination());
        System.out.println("Distance of Ticket1: " + ticket1.getDistance());
        System.out.println("TrainType of Ticket1: " + ticket1.getTrainType());
        System.out.println();

        // Step 6: Test deep cloning
        TrainTicket clonedTicket = ticket1.deepCopy();
        System.out.println("Cloned Ticket:\n" + clonedTicket);
        System.out.println("\nCloned equals original? " + clonedTicket.equals(ticket1));
        System.out.println("Same reference? " + (clonedTicket == ticket1));
    }
}
