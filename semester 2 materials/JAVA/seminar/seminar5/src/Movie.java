import java.util.Objects;

public class Movie {
    private int id;
    private int year;
    private String title;
    private float rating;

    public Movie(int id, int year, String title, float rating) {
        this.id = id;
        this.year = year;
        this.title = title;
        this.rating = rating;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Movie movie = (Movie) o;
        return id == movie.id && year == movie.year && Float.compare(rating, movie.rating) == 0 && Objects.equals(title, movie.title);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, year, title, rating);
        //return (int) (31*id + 31*31*year + 31*rating + 31*title.length());
    }

    @Override
    public String toString() {
        return String.format("[%d. %s from %d has %5.2f/10]", id, title, year, rating);
    }
}
