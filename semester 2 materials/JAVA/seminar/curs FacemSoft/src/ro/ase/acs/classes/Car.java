package ro.ase.acs.classes;

public class Car {
    private String producer;
    private float price;
    private FuelType fuelType;

    //constructor implicit
    public Car(){
        producer = "";
        price = 4000f;
        fuelType = FuelType.gas;
    }

    //constructor cu parametrii
    public Car(String producer, float price){
        this.producer = producer;
        this.price = price;
    }

    //getteri si setteri
    public String getProducer() {
        return producer;
    }

    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public FuelType getFuelType() {
        return fuelType;
    }

    public void setFuelType(FuelType fuelType) {
        this.fuelType = fuelType;
    }

    @Override
    public Object clone() {

    }
}
