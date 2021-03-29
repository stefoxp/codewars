var SequenceSum = (function() {
    function SequenceSum() {}
  
    SequenceSum.showSequence = function(count) {
      var partial = 0;
       var index = 1;
       
      if(count < 0) {
        result = count + '<0';
      } else {
        if(count > 0) {
          result = '0';  
          while(index <= count) {
            result += '+' + index;
            partial += index;
            index++;
          };
          result += ' = ' + partial;
        } else {
          result = '0=0';
        };
      };
       
      return result;
    };
  
    return SequenceSum;
  
  })();
