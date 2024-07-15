// package hw1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;

public class factorServer {

  public static void main(String[] args)
    throws UnknownHostException, IOException {
    ServerSocket ss = new ServerSocket(9806);
    Socket soc = ss.accept();
    PrintWriter out = new PrintWriter(soc.getOutputStream(), true);
    System.err.println("client connected");
    BufferedReader read = new BufferedReader(
      new InputStreamReader(soc.getInputStream())
    );
    int data = Integer.parseInt(read.readLine());

    out.println(data);
    ss.close();
  }
}
