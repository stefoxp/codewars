public class NthSeries {
  
  public static String seriesSum(int n) {
    double den = 1.0;
    double sum = den;
    
    for(int i = 1; i < n; i++)
    {
      den = (den + 3.0);
      sum += 1.0 / den;
    }
    return String.format("%.2f", sum);
  }
}
