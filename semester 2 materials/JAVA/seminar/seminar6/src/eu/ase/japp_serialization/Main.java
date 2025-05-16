package eu.ase.japp_serialization;

import java.io.*;

/*
 * R -> Read
 * FileInputStream
 * BufferedInputStream
 * DataInputStream
 * ----------------
 * W -> Write
 * FileOutputStream
 * BufferedOutputStream
 * DataOutputStream
 */
public class Main {
    public static void main(String[] args) throws IOException {
        try {
            FileOutputStream fos = new FileOutputStream("data");
            BufferedOutputStream bos = new BufferedOutputStream(fos);
            DataOutputStream dos = new DataOutputStream(bos);

            //write data to file
            dos.writeInt(5);
            dos.writeUTF("Bai nene pumnu meu beton armat!");
            dos.writeBoolean(true);
            dos.writeFloat(60.99f);

            dos.close();
            //fos.close() -> still valid

        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        DataInputStream dis = new DataInputStream(new BufferedInputStream((new FileInputStream("data"))));
        int data = dis.readInt();
        System.out.println(data);
        String utfData = dis.readUTF();
        System.out.println(utfData);
        boolean boolData = dis.readBoolean();
        System.out.println(boolData);
        float floatData = dis.readFloat();
        System.out.println(floatData);

        dis.close();
    }
}