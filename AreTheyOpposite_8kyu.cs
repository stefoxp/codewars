using System;

public class Kata
{
  public static bool IsOpposite(string s1, string s2)
  {
    bool result = false;
    string s1_opposite = "";
    
    if (s1 != "" && s2 != "" && s1.Length == s2.Length)
    {
      result = true;
      
      char[] charS1 = s1.ToCharArray();  
      foreach (char ch in charS1)
      {
        if(Char.IsUpper(ch))
          s1_opposite += Char.ToLower(ch);
        else
          s1_opposite += Char.ToUpper(ch);
      }
      if(s1_opposite != s2)
          result = result && false;
    }
    return result;
  }
}
