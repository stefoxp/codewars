using System;
using System.Linq;

namespace Solution {
  public class Kata
  {
    public static int FinalGrade(int exam, int projects)
    {
      int result = 0;
      
      if((exam > 90) || (projects > 10))
        result = 100;
      else if((exam > 75) && (projects > 4))
        result = 90;
      else if((exam > 50) && (projects > 1))
        result = 75;
        
        
      return result;
    }
  }
}
