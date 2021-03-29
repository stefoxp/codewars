public class SequenceSum
{
  public static string ShowSequence(int n)
  {    
    int sum_result = 0;
    string result = "";
    
    if (n > 0) {      
      for(int c=0; c<=n; c++){
        result += "+";
        result += c.ToString();
        sum_result += c;
      }
      result += " = " + sum_result.ToString();
      
      result = result.Substring(1);
    } else if(n == 0) {
      result = "0=0";
    } else {
      result = n.ToString() + "<0";
    }
    
    return result;
  }
}
