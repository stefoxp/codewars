public class Kata 
{
    public static int FindSmallestInt(int[] args) 
    {
      int smallest = args[0];
      
      foreach(int i in args)
        if(i < smallest)
          smallest = i;
      
      return smallest;
    }
}
