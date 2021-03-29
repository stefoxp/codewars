public class GpsSpeed {
    public static int gps(int s, double[] x) {
        int max = 0;
        int current = 0;
        
        for(int counter = 1; counter < x.length; counter++)
        {
          current = (int)(3600 * (x[counter] - x[counter - 1])) / s;
          
          if(current > max)
            max = current;
         }
          
        
        return max;
    }
}
