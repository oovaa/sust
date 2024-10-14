import java.util.ArrayList;
import java.util.List;

public class Minmax {

  static int[] getMinMax(String strArr) {
    String[] splited = strArr.split(" ");
    List<Integer> validnums = new ArrayList<>();

    for (String s : splited) if (canParseToInt(s)) validnums.add(
      Integer.parseInt(s)
    );

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
