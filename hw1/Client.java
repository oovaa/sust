import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {

  public static void main(String[] args) {
    try (
      Socket soc = new Socket("localhost", 9806);
      PrintWriter out = new PrintWriter(soc.getOutputStream(), true);
      BufferedReader input = new BufferedReader(
        new InputStreamReader(System.in)
      );
      BufferedReader reader = new BufferedReader(
        new InputStreamReader(soc.getInputStream())
      )
    ) {
      System.out.println("Client started. Enter a string:");
      out.println(input.readLine());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
