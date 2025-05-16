package eu.ase.s9;

import javax.xml.crypto.dsig.spec.HMACParameterSpec;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;

//working with our interface
class checkStudentsThatPassed implements checkStudent{
    @Override
    public boolean test(Student s) {
        if(s.getGpa() >= 4.5f){
            System.out.println(s.getName() + " passed, having GPA: " + s.getGpa());
            return true;
        }
        else{
            System.out.println(s.getName() + " failed, having GPA: " + s.getGpa());
            return false;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        List<Student> students = new ArrayList<>();
        //String name, Sex sex, int age, float gpa, String email
        students.add(new Student("Rosu Liviu", Sex.MALE, 20, 4.5f, "rosuliviu@gmail.com"));
        students.add(new Student("Rusu Mihnea", Sex.MALE, 20, 4.7f, "rusumihnea@gmail.com"));
        students.add(new Student("Sandu Leonard", Sex.MALE, 21, 4.5f, "sanduleonard@gmail.com"));
        students.add(new Student("Raevschi Ana", Sex.FEMALE, 20, 5f, "raevschiana@gmail.com"));
        students.add(new Student("Suto Mara", Sex.FEMALE, 20, 4.4f, "sutomara@gmail.com"));

        System.out.println("\nI. Students older than a certain age (this case 18): ");
        printPersonsOlderThan(students, 18);

        System.out.println("\nII. Students in a certain age range (this case 18-20):");
        printStudentsInAgeRange(students, 18, 21);

        System.out.println("\nIII. Checking which student passed (must have GPA >= 4.5):");
        printStudent(students, new checkStudentsThatPassed());

    }

    //methods

    // I. print students older than a certain given age
    public static void printPersonsOlderThan(List<Student> myList, int age){
        for(Student s: myList){
            if(s.getAge() > age){
                System.out.println(s.getName() + " is " + s.getAge() + " years old and is older than given age: " + age);
            }
            else{
                System.out.println(s.getName() + " is " + s.getAge() + " years old and is not older than given age: " + age);
            }
        }
    }

    // II. use checkStudent
    public static void printStudent(List<Student> myList, checkStudent tester){
        for(Student s: myList){
            if(tester.test(s)){
                s.getName();
            }
        }
    }

    // III. print students in a certain age range
    public static void printStudentsInAgeRange(List<Student> myList, int low, int high){
        for(Student s: myList){
            if(low <= s.getAge() && s.getAge() < high){
                System.out.println(s.getName() + " is " + s.getAge() + " years old and fits the interval " + low + "-" + high);
            }
            else{
                System.out.println(s.getName() + " is " + s.getAge() + " years old and does not fit the interval " + low + "-" + high);
            }
        }
    }
}