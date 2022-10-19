<?php
//Salida siempre que sea inferior a 6.$i$i
$i = 1; 

while($i < 6){
    echo $i;
    $i++;
}


//Salida siempre que sea inferior a 6.$i$i
$i = 1; 

do{
    echo $i;
    $i++;

}while($i < 6);


//Cree un bucle que vaya de 0 a 9.
for($i = 0; $i < 10; $i++) {
    echo $i;
}

#recorra los elementos de la matriz.$colors
$colors = array("red", "green", "blue", "yellow"); 

foreach($colors as $x) {
    echo $x;
}
?>