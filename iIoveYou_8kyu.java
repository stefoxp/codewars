public class Sid {
    public static String howMuchILoveYou(int nb_petals) {
      String result = "";
      int rest = 0;
      String[] ph = {
                    "I love you",
                    "a little",
                    "a lot",
                    "passionately",
                    "madly",
                    "not at all"
                    };
      int int_ph_length = 6;
    
   
      if(nb_petals <= int_ph_length)
      {
        result = ph[nb_petals - 1];
      }
      else
      {
        rest = nb_petals % int_ph_length;
        
        if(rest == 0)
          result = ph[int_ph_length - 1];
        else        
          result = ph[rest - 1];
      }
    
    return result;
    }
}
