package eu.ase.japp_serialization;

import java.io.*;

public class BookMain {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
//        Book b1 = new Book(2004, "Rusu Micnea", "Tata bogat tata sarac");
//        b1.saveBookToFile("book.bin");
//
//        Book b2 = new Book();
//        b2 = b2.readBookFromFile("book.bin");

        Author a1 = new Author(2004, "Rusu Micnea"); // daca schimbam a1 se va schimba si in b1/b2 pentru ca este aceasi referinta
        Book b1 = new Book(2025, "Tata bogat tata sarac volumul 100", a1);
        Book b2 = new Book(2024, "Tata bogat tata sarac volumul 101", a1);

        FileOutputStream fos = new FileOutputStream("serializedBook.bin");
        ObjectOutputStream oos = new ObjectOutputStream(fos);

        oos.writeObject(b1);
        oos.writeObject(b2);
        oos.writeObject(a1);

        oos.close();

        FileInputStream fis = new FileInputStream("serializedBook.bin");
        ObjectInputStream ois = new ObjectInputStream(fis);

        Book b3 = (Book) ois.readObject();
        Book b4 = (Book) ois.readObject();
        Author a2 = (Author) ois.readObject();
    }
}
