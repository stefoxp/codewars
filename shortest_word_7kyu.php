<?php
function findShort($str){
  $lunghezza = 100000;
  $a = preg_split('/\s+/', $str);
  foreach($a as $parola) {
    $parola_len = strlen($parola);
    if($parola_len < $lunghezza) {
      $lunghezza = $parola_len;
    };
  };
  
  return $lunghezza;
}
?>
