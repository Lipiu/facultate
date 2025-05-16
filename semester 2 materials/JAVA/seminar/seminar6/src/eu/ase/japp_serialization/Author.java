package eu.ase.japp_serialization;

import java.io.Serializable;

public class Author implements Serializable {
    private int birthYear;
    private String name;

    public Author(int birthYear, String name) {
        this.birthYear = birthYear;
        this.name = name;
    }

    public int getBirthYear() {
        return birthYear;
    }

    public void setBirthYear(int birthYear) {
        this.birthYear = birthYear;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
