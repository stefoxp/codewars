function points(games) {
    var result = 0;
    
    for(i in games) {
      x = games[i][0];
      y = games[i][2];
      
      if(x > y)
        result += 3;
      else if(x == y)
        result += 1;
    }
    return result;
  }
