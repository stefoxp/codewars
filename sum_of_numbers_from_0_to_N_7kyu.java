public class SequenceSum{

  public static String showSequence(int value){
    int sum_result = 0;
    String result = "";
    
    if (value > 0) {      
      for(int c=0; c<=value; c++){
        result += "+";
        result += Integer.toString(c);
        sum_result += c;
      }
      result += " = " + Integer.toString(sum_result);
      
      result = result.substring(1, result.length());
    } else if(value == 0) {
      result = "0=0";
    } else {
      result = Integer.toString(value) + "<0";
    }
    
    return result;
  }
}
