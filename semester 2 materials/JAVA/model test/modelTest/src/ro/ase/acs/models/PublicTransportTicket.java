package ro.ase.acs.models;

import ro.ase.acs.contracts.Buyable;

public abstract class PublicTransportTicket implements Buyable {
    protected String departure;
    protected String destination;
    protected int distance;

    PublicTransportTicket(String departure, String destination, int distance){
        this.departure = departure;
        this.destination = destination;
        this.distance = distance;
    }

    public String getDeparture() {
        return departure;
    }

    public void setDeparture(String departure) {
        this.departure = departure;
    }

    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }

    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }

    @Override
    public float getPrice() {
        return 5;
    }

    public abstract float getDiscount();
}

