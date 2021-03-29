public class Kata
{
  public static string GetMiddle(string s)
  {
    string result = "";
    int len = s.Length;
    int car = 1;
    
    if(len % 2 == 0) {
      car = 2;
    }
    result = s.Substring((len - 1) / 2, car);
    
    return result;
  }
}
