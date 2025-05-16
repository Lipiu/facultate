import com.sun.source.tree.Tree;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Map<Integer, Movie> movieLibrary = new HashMap<>();

        Movie m1 = new Movie(1, 2024, "Anora", 8.6f);
        Movie m2 = new Movie(2, 2023, "Oppenheimer", 9.2f);
        Movie m3 = new Movie(3, 2022, "Everything Everywhere all at Once", 7.6f);

        movieLibrary.put(67, m1);
        movieLibrary.put(7, m2);
        movieLibrary.put(200, m3);

        //movieLibrary.put(-1235019247, new Movie(0,0, "ERROR", 0f));

        Set<Integer> keySet = movieLibrary.keySet();
        Iterator<Integer> it = keySet.iterator();

        for(;it.hasNext();){
            Integer key = it.next();
            System.out.println("Key " + key + ": " + movieLibrary.get(key));
        }

        SortedMap<Integer, Movie> treeMap = new TreeMap<>();

        System.out.println();
        treeMap.put(m1.hashCode(), m1);
        treeMap.put(m2.hashCode(), m2);
        treeMap.put(m3.hashCode(), m3);

        keySet = treeMap.keySet();
        it = keySet.iterator();

        for(;it.hasNext();){
            Integer key = it.next();
            System.out.println("Key " + key + ": " + movieLibrary.get(key));
        }
    }
}