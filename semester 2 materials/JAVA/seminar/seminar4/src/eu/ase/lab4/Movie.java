package eu.ase.lab4;

public class Movie implements Cloneable{
    private int year;
    private String title;
    private float rating;

    public Movie(int year, String title, float rating) {
        this.year = year;
        this.title = title;
        this.rating = rating;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public float getRating() {
        return rating;
    }

    public void setRating(float rating) {
        this.rating = rating;
    }

    @Override
    protected Object clone() throws  CloneNotSupportedException{
        Movie clone = (Movie) super.clone();
        clone.year = this.year;
        clone.title = this.title;
        clone.rating = this.rating;

        return clone;
    }

    @Override
    public String toString() {
        String s = String.format("%s from %d has a rating of %5.2f", this.title, this.year, this.rating);
        return s;
    }

//
//    @Override
//    public int compareTo(Movie o) {
//        if(this.year == o.getYear()){
//            return 0;
//        }
//        if(this.year < o.getYear()){
//            return -1;
//        }
//        else{
//            return 1;
//        }
}
