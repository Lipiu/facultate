package eu.ase.net;

import java.io.IOException;
import java.net.*;

public class UDPClient {
    public static void main(String[] args){
        try {

            DatagramSocket clientSocket = new DatagramSocket();
            String message = "Hello from Sandu Leonard <3!";
            byte[] buffer = message.getBytes();

            int port = 12345;
            InetAddress address = InetAddress.getByName("10.2.65.66");

            DatagramPacket packet = new DatagramPacket(buffer, buffer.length, address, port);
            clientSocket.send(packet);

            byte[] bufferReceive = new byte[256];
            packet = new DatagramPacket(bufferReceive, bufferReceive.length);
            clientSocket.receive(packet);

            String received = new String(packet.getData());
            System.out.println("Client received from the server: " + received);
            clientSocket.close();
        }
        catch (SocketException e) {
            throw new RuntimeException(e);
        } catch (UnknownHostException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
