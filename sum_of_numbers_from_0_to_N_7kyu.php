<?php
class SequenceSum {
  public function showSequence($count) {
    $partial = 0;
    $index = 1;
     
    if($count < 0) {
      $result = $count . '<0';
    } else {
      if($count > 0) {
        $result = '0';  
        while($index <= $count) {
          $result .= '+' . $index;
          $partial += $index;
          $index++;
        };
        $result .= ' = ' . $partial;
      } else {
        $result = '0=0';
      };
    };
     
    return $result;
  }
}
?>
