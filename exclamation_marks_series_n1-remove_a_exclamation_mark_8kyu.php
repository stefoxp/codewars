<?php
function remove(string $s): string {
    $risultato = $s;
    
    if(strrpos($s, '!') == strlen($s) - 1) {
      $risultato = substr($s, 0, strlen($s) - 1);
    }
    
    return $risultato;
}
?>
