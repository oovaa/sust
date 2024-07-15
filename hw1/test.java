import java.util.ArrayList;
import java.util.List;

public class test {

  public static void main(String[] args) {
    String str = "23 1 45 a 7 -3 as -8";
    int[] minmax = getMinMax(str);
    int min = minmax[0];
    int max = minmax[1];
    System.out.println(min + " - " + max);
  }

  static int[] getMinMax(String strArr) {
    String[] splited = strArr.split(" ");
    List<Integer> validnums = new ArrayList<>();

    for (String s : splited) {
      if (canParseToInt(s)) {
        validnums.add(Integer.parseInt(s));
      }
    }

    int min = getMin(validnums);
    int max = getmax(validnums);

    return new int[] { min, max };
  }

  public static boolean canParseToInt(String str) {
    try {
      Integer.parseInt(str);
      return true;
    } catch (NumberFormatException e) {
      return false;
    }
  }

  public static int getMin(List<Integer> validList) {
    int hold = validList.get(0);
    for (int i = 0; i < validList.size(); i++) {
      if (hold > validList.get(i)) {
        hold = validList.get(i);
      }
    }
    return hold;
  }

  public static int getmax(List<Integer> validList) {
    int hold = validList.get(0);
    for (int i = 0; i < validList.size(); i++) {
      if (hold < validList.get(i)) {
        hold = validList.get(i);
      }
    }
    return hold;
  }
}
