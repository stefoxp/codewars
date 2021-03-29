function cutFruits(fruits){
    var fruits_cut = [""];
    
    for(var i = 0; i < fruits.length; i++)
    {
      if(fruitsName.indexOf(fruits[i]) != -1)
      {
        var val_length = fruits[i].length;
        var half = val_length / 2;
        
        if((val_length % 2) > 0)
        {
          // odd
          half = (val_length + 1) / 2;
        }
        
        fruits_cut.push(fruits[i].substring(0, half));
        fruits_cut.push(fruits[i].substring(half, val_length));
      } else {
       fruits_cut.push(fruits[i]);
      }
    }
    
    return fruits_cut.slice(1, fruits_cut.length);
  }
