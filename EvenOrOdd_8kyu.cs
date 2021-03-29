using System;

namespace Solution
{
  public class SolutionClass
  {
    public static string EvenOrOdd(int number)
    {
      string result = "Even";
      
      if(number % 2 != 0)
      {
       result = "Odd";
      }
      return result;
    }
  }
}
