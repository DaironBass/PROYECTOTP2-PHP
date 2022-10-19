<?php
//Cree una función denominada .myFunction
function myFunction1(){
  echo "Hello World!";
}

//Llamar (ejecutar) a una función denominada .myFunction
function myFunction2() {
  echo "Hello World!";
}
myFunction2();

//Dentro de una función con dos parámetros, imprima el primer parámetro.  
function myFunction3($fname, $lname) {
    echo $fname;
}

//Deje que la función devuelva el segundo valor.
function myFunction4($fname, $lname) {
    return $lname;
}
?>{{}}