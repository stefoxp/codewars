function makePassword(phrase) {
    var a = phrase.split(" ");
    var result = "";
    var substitutes = [
      ["o", "0"],
      ["O", "0"],
      ["i", "1"],
      ["I", "1"],
      ["s", "5"],
      ["S", "5"]
    ];
    
    for(i in a) {
      result += a[i].slice(0, 1);
    }
    
    for(s in substitutes) {
      result = result.split(substitutes[s][0]).join(substitutes[s][1]);
    }
    
    return result;
  }
