<?php
//Escriba una sintaxis correcta para incluir un archivo denominado "footer.php"
include 'footer.php';

//Supongamos que tenemos un archivo llamado "webdict.txt", escriba la sintaxis correcta para abrir y leer el contenido del archivo
echo readfile("webdict.txt");

//Abra un archivo y escriba la sintaxis correcta para generar un carácter a la vez, hasta el final del archivo.
$myfile = fopen("webdict.txt", "r");
while(!feof($myfile)) {
  echo fgetc($myfile);
}

//Cree una cookie llamada "nombre de usuario".
setcookie("username", "John", time() + (86400 * 30), "/");

//Cree una variable de sesión denominada "favcolor".
session_start();
$_SESSION["favcolor"] = "green";

//Genere el valor de la variable de sesión "favcolor".
echo $_SESSION["favcolor"];
?>