<?php
function positive_sum($arr) {
    $result = 0;
    if(count($arr) > 0) 
      foreach($arr as $value)
        if($value > 0)
          $result += $value;
          
    return $result;
  }
?>
