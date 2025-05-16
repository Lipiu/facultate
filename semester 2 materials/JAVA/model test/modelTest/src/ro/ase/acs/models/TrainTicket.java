package ro.ase.acs.models;

import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class TrainTicket extends PublicTransportTicket{
    private TrainType trainType;


    public TrainTicket(String departure, String destination, int distance, TrainType trainType) {
        super(departure, destination, distance);
        this.trainType = trainType;
    }

    public void setTrainType(TrainType trainType) {
        this.trainType = trainType;
    }

    public TrainTicket deepCopy(){
        TrainTicket copy = new TrainTicket("", "", 0, null);
        copy.departure = departure;
        copy.destination = destination;
        copy.distance = distance;
        copy.trainType = trainType;
        return copy;
    }

    public TrainType getTrainType() {
        return trainType;
    }

    @Override
    public float getPrice(){
        //price = the price returned by the method from PublicTransportTicket x distance x discount
        float price = 5 * distance * getDiscount();
        return price;
    }

    @Override
    public float getDiscount() {
        if(trainType == TrainType.REGIO){
            return 0.5f;
        }
        else if(trainType == TrainType.INTERREGIO){
            return 0.25f;
        }
        else{
            return 0;
        }
    }

    @Override
    public String toString() {
        return "> Departure: " + departure + "\n> Destination: "+ destination + "\n> Distance: " + distance;
    }
}
