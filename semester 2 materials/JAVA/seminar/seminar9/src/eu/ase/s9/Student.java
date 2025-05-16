package eu.ase.s9;

public class Student {
    private String name;
    private Sex sex;
    private int age;
    private float gpa;
    private String email;

    public Student(String name, Sex sex, int age, float gpa, String email) {
        this.name = name;
        this.sex = sex;
        this.age = age;
        this.gpa = gpa;
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Sex getSex() {
        return sex;
    }

    public void setSex(Sex sex) {
        this.sex = sex;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public float getGpa(){ return gpa; }

    public void setGpa(float gpa) { this.gpa = gpa; }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void printPerson(){
        System.out.printf("Name: %s\nSex: %s\nAge: %d\nGPA: %.1f\nEmail: %s\n", getName(), getSex(), getAge(), getGpa(), getEmail());
    }
}
