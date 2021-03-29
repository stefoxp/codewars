function skiJump(mountain) {
    var height = mountain.length;
    var result = (height * height * 1.5 * 9 / 10).toFixed(2);

    if(result < 10)
      result += " metres: He's crap!"
    else if(result < 25)
      result += " metres: He's ok!"
    else if(result < 50)
      result += " metres: He's flying!"
    else
      result += " metres: Gold!!"
    
    return result;
  }
