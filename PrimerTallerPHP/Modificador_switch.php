<?php
//Cree una instrucción que genere "Hola" si es "rojo" y "bienvenido" si es "verde".switch$color$color
$color = "Hello";
switch($color) {
  
case "red":
    echo "Hello";
    break;
  
case "green":
    echo "Welcome";
    break;
}


//Agregue una sección que genere "Ninguno" si no es ni "rojo" ni "verde".$color
$color = "Black";
switch ($color) {
    case "red":
      echo "Hello";
      break;
    case "green":
      echo "Welcome";
      break;
    
  default:
      echo "Neither";
  }
