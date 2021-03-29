class Arge {
    
    public static int nbYear(int p0, double percent, int aug, int p) {
        int n = 0;
        
        while(p > p0)
        {
          n++;
          p0 += p0 * percent / 100 + aug;      
        }
        
        return n;
    }
}
