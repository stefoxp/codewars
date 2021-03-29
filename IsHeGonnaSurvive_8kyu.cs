class Kata
{
    public static bool Hero(int bullets, int dragons)
    {
        bool result = false;
        
        if(bullets >= dragons * 2)
          result = true;
        
        return result;
    }
}
