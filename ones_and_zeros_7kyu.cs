namespace Solution
{
  class Kata
    {
      public static int binaryArrayToNumber(int[] BinaryArray)
        {
          string binaryString = "";
          
          foreach (int element in BinaryArray) {
            binaryString += element.ToString();
          }
          
          return System.Convert.ToInt32(binaryString, 2);
        }
    }
}
