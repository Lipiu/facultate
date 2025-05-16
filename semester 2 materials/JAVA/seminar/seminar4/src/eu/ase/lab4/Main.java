package eu.ase.lab4;

import java.util.*;

public class Main {
    public static void main(String[] args){
        List<Integer> intList = new ArrayList<>();
        for(int i = 0; i < 5; i++){
            intList.add(i);
        }
        for(int e: intList){
            System.out.println(e);
        }

        System.out.println("Size of intList: " + intList.size());

        intList.addFirst(-1);
        for(int e: intList){
            System.out.println(e);
        }

        System.out.println("Element at index 3: " + intList.get(3));
        System.out.println("Element at index 4: " + intList.indexOf(4));

        Random rand = new Random();
        List<Integer> randList = new ArrayList<>();
        for(int i = 0; i < 10; i++){
            randList.add(rand.nextInt() % 100);
        }
        System.out.println("Unsorted:");
//        for(int e: randList){
//            System.out.println(e);
//        }
        System.out.println(randList);
        randList.sort(Comparator.naturalOrder());
        System.out.println("Sorted:");
//        for(int e: randList){
//            System.out.println(e);
//        }
        System.out.println(randList);

        randList.sort(Comparator.reverseOrder());
        System.out.println("Reverse:");
//        for(int e: randList){
//            System.out.println(e);
//        }
        System.out.println(randList);

        List<Movie> movieLibrary = new ArrayList<>();

        movieLibrary.add(new Movie (2024, "Moana 2", 9.7f));
        movieLibrary.add(new Movie (2003, "Anora", 7.7f));
        movieLibrary.add(new Movie (2025, "Wicked", 8.7f));

        for(Movie m: movieLibrary){
            System.out.println(m);
        }

        movieLibrary.sort(new TitleComparator());
        for(Movie m: movieLibrary){
            System.out.println(m);
        }
    }
}
