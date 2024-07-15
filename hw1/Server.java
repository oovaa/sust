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
    ServerSocket ss = new ServerSocket(9806);
    Socket soc = ss.accept();
    System.err.println("client connected");
    BufferedReader read = new BufferedReader(
      new InputStreamReader(soc.getInputStream())
    );
    String str = read.readLine();
    PrintWriter out = new PrintWriter(soc.getOutputStream(), true);
    System.out.println("server says " + str);
    ss.close();
  }
}
