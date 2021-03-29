<?php
function remove(string $s): string {
    $lunghezza = strlen($s);
    $conta_exc = 0;
    
    for($i = $lunghezza - 1; $i > 0; $i--) {
      if($s[$i] == '!') 
        $conta_exc++;
      else
        $i = 0;
    };
    
    $s_mod = substr($s, 0, $lunghezza - $conta_exc);
    
    return $s_mod;
  }
?>
