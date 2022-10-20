<?php
//Salida "Hello World" si es mayor a que b.
$a = 50;
$b = 10;

if($a > $b){
  echo "Hello World";
}


#Salida "Hello World" si NO es igual $a y $b
$a = 50;
$b = 10;

if($a != $b){
  echo "Hello World";
}


//Salida "Sí" si es igual a y b, de lo contrario salida "No"
$a = 50;
$b = 10;

if($a == $b) {
  echo "Yes";
} 
else{
  echo "No";
}

//Salida "1" si es igual a , imprimir "2" si es mayor que , de lo contrario salida "3".$a$b$a$b
$a = 50;
$b = 10;

if($a == $b) {
  echo "1";
} 
elseif($a > $b) {
  echo "2";
} 
else{
  echo "3";
}
?>