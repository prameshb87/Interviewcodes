import java.util.*;
import java.lang.*;
class Main {
  public static void main(String[] args) {
    String s = " Ramesh Pra sad";
    ArrayList<Character> array_s = new ArrayList<Character>();
    StringBuilder string_s = new StringBuilder();
    int i = 0;
    while(i<s.length()) {
      if(s.charAt(i) != ' ') {
        array_s.add(s.charAt(i));
        i++;

      }
      else {
        array_s.add('%');
        array_s.add('2');
        array_s.add('0');
        i++;

      }
    }
    for (Character a: array_s) {
      string_s.append(a);
    }
    System.out.println(string_s.toString());
  }
}
