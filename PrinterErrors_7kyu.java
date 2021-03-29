public class Printer {
    
    public static String printerError(String s) {
        int errors_count = 0;
        String errors = "/";
        String control = "abcdefghijklm";
        
        for(char ch: s.toCharArray())
        {
          if(!(control.contains(Character.toString(ch))))
            errors_count++;
        }
        
        errors = Integer.toString(errors_count) + errors;
        errors += s.length();
        
        return errors;
    }
}
