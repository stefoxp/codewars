public class Accumul {
    
    public static String accum(String s) {
        String result = "";
        char[] characters = s.toLowerCase().toCharArray();
        int counter = 1;
        
        for(int indice = 0; indice < s.length(); indice++)
        {
          char character = characters[indice];
          
          if(indice != 0)
          {
            result += "-";
          }
          result += ("" + character).toUpperCase();
          
          for(int reps = 1; reps < counter; reps++)
          {
            result += character;
          }
          counter++;
        }
        return result;
    }
}
