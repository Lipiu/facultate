package eu.ase.japp_serialization;

import java.io.*;

public class Book implements Serializable{
    private int publishingYear;
    private String title;
    private Author author;

    public Book(int publishingYear, String title, Author author) {
        this.publishingYear = publishingYear;
        this.title = title;
        this.author = author;
    }

    public Book(){
        this.publishingYear = 0;
        this.author = null;
        this.title = "";
    }

    public int getPublishingYear() {
        return publishingYear;
    }

    public void setPublishingYear(int publishingYear) {
        this.publishingYear = publishingYear;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Author getAuthor() {
        return author;
    }

    public void setAuthor(Author author) {
        this.author = author;
    }

//    public void saveBookToFile(String filename) throws IOException {
//        DataOutputStream dos = new DataOutputStream(new BufferedOutputStream(new FileOutputStream(filename)));
//        dos.writeInt(getPublishingYear());
//        dos.writeUTF(getTitle());
//        dos.writeUTF(getAuthor());
//        dos.close();
//    }
//
//    public Book readBookFromFile(String filename) throws IOException {
//        DataInputStream dis = new DataInputStream(new BufferedInputStream(new FileInputStream(filename)));
//        return new Book(dis.readInt(), dis.readUTF(), dis.readUTF());
//    }
}
