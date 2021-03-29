function mirror(code, alphabet="abcdefghijklmnopqrstuvwxyz") {
    var result = "";
    alphabet = alphabet.split('');
    code = code.toLowerCase().split('');

    for(var i in code) {
      var value = code[i];
      var index = alphabet.indexOf(value);

      if(index == -1)
        result += value;
      else
        result += alphabet[alphabet.length - 1 - index];
    }

    return result;
  }
