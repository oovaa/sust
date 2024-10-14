import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class factorClient {

  public static void main(String[] args) {
    try (
      Socket soc = new Socket("localhost", 9806);
      BufferedReader reader = new BufferedReader(
        new InputStreamReader(System.in)
      );
    ) {
      System.out.println("Client started");
      System.out.println("enter a number");
      int num = Integer.parseInt(reader.readLine());
      PrintWriter out = new PrintWriter(soc.getOutputStream(), true);
      out.println(num);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
