package eu.ase.net;

import javax.xml.crypto.Data;
import java.io.IOException;
import java.net.*;

public class UDPServer {
    public static void main(String[] args){
        //equivalent to char
        byte[] bufferResponse = null;
        byte[] bufferReceive = null;

        try(DatagramSocket socket = new DatagramSocket(12345)){
            System.out.println("UDP Server bind on 12345 port");

            while(true){
                bufferReceive = new byte[256]; //only to store information
                DatagramPacket packet = new DatagramPacket(bufferReceive, bufferReceive.length);
                socket.receive(packet);
                System.out.println("Client: " + new String(packet.getData(), 0, packet.getLength()));

                String responseString = "All good fram!";
                bufferResponse = responseString.getBytes();

                InetAddress address = packet.getAddress();
                int port = packet.getPort();

                DatagramPacket packetResponse = new DatagramPacket(bufferResponse, bufferResponse.length, address, port);
                socket.send(packetResponse);
            }
        }
        catch (SocketException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
