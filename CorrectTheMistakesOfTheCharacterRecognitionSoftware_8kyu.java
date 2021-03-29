public class Correct {
  public static String correct(String string) {
    String[][] cases = {
                        {"5", "S"},
                        {"0", "O"},
                        {"1", "I"}
                        };
                        
    for(String[] single: cases)
      string = string.replace(single[0], single[1]);
    
    return string;
  }
}
