<?php
function makeYoutubeLink(string $str): string {
    $base = 'https://www.youtube.com/embed/';
    $risultato = $str;
    
    if($posizione = strpos($str, '=')) {
      $risultato = $base . substr($str, $posizione + 1);
    } else {
      if($posizione = strrpos($str, '/')) {
        $risultato = $base . substr($str, $posizione + 1);
      };
    };
    
    return $risultato;
}
?>
