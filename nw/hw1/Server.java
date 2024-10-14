// package hw1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;

public class Server {

  public static void main(String[] args)
    throws UnknownHostException, IOException {
    try (
      ServerSocket serverSocket = new ServerSocket(9806);
      Socket clientSocket = serverSocket.accept();
      BufferedReader in = new BufferedReader(
        new InputStreamReader(clientSocket.getInputStream())
      );
      PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)
    ) {
      System.err.println("Client connected");
      String received = in.readLine();

      int[] data = Minmax.getMinMax(received);
      int min = data[0], max = data[1];
      out.println("Min is: " + min + "  Max is: " + max);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
