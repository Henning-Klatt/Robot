<?php

/*** KONFIGURATION ***/

// Definiert Konstanten für das Script
define('MD5_ENCRYPT', false); // Aktiviert Verschlüsselung für Passwort. Wenn "true" gesetzt, müssen Passwörter von $usrdata md5-verschlüsselt vorliegen. Standard: false
define('SUCCESS_URL', 'index.php'); // URL, zu welcher nach erfolgreichen Login umgeleitet wird.
define('LOGIN_FORM_URL', 'login.php'); // URL mit Anmeldeformular
// Array mit Benutzerdaten: Besteht aus Array-Elementen mit paarweisen Benutzernamen und Passwörtern
$usrdata = array(

    array(
        "usr" => "admin",
        "pwd" => "passwort" // MD5-verschlüsselte Form: e22a63fb76874c99488435f26b117e37
    ),
    array(
        "usr" => "pi",
        "pwd" => "raspberry"
    ),
    array(
        "usr" => "Henning",
        "pwd" => "passwort"
    ),
    array(
	"usr" => "Florian",
	"pwd" => "passwort"
    )
    /* ... */
);

header("Content-Type: text/html; charset=utf-8"); // Melde Browser die verwendete Zeichenkodierung

// PHP-Session starten und aktuellen Stand abfragen
session_start();
$_SESSION['logged_in'] = (isset($_SESSION['logged_in']) && $_SESSION['logged_in'] === true) ? true : false;
$_SESSION['usr'] = (isset($_SESSION['usr'])) ? $_SESSION['usr'] : '';

$error = array();
if(!isset($_POST['login'])){
    header('Location: '.LOGIN_FORM_URL);
}else{
    $usr = (!empty($_POST['user']) && trim($_POST['user']) != '') ? $_POST['user'] : false;
    $pwd = (!empty($_POST['password']) && trim($_POST['password']) != '') ? $_POST['password'] : false;

    if(!$usr || !$pwd){
        if(count($error) == 0)
            $error[] = "Bitte geben Sie Benutzername und Passwort ein.";
    }else{
        $pwd = (MD5_ENCRYPT === true) ? md5($pwd) : $pwd; // Passwort eingabe MD5-encrypten, falls Option gesetzt ist
        foreach($usrdata as $ud){ // Benutzer-Liste durchlaufen und je mit Formular-Eingaben vergleichen
            if($usr != $ud['usr'] || $pwd != $ud['pwd']){
                if(count($error) == 0)
                    $error[] = "Benutzername und/oder Passwort nicht korrekt.";
            }else{
                $_SESSION['logged_in'] = true;
                $_SESSION['usr'] = $usr;
                header('Location: '.SUCCESS_URL);
            }
        }
    }
}

?>
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LexoBot | LogIn</title>
    <!-- Core CSS - Include with every page -->
    <link href="assets/plugins/bootstrap/bootstrap.css" rel="stylesheet" />
    <link href="assets/font-awesome/css/font-awesome.css" rel="stylesheet" />
    <link href="assets/plugins/pace/pace-theme-big-counter.css" rel="stylesheet" />
   <link href="assets/css/style.css" rel="stylesheet" />
      <link href="assets/css/main-style.css" rel="stylesheet" />

</head>

<body class="body-Login-back">

    <div class="container">

        <div class="row">
            <div class="col-md-4 col-md-offset-4 text-center logo-margin ">
              <img src="assets/img/logo.png" alt=""/>
                </div>
            <div class="col-md-4 col-md-offset-4">
                <div class="login-panel panel panel-default">
                    <div class="panel-heading">
                        <h3 class="panel-title"><font color="#ff6347">Fehler aufgetreten:</font></h3>
                    </div>
                    <div class="panel-body">
                        <form role="form" method="POST" action="login.php">
                          <ul>
                          <?php
                          foreach($error as $out){
                              ?>
                              <li><?php echo $out; ?></li>
                              <?php
                          }
                          ?>
                          </ul>
                                <input type=submit name=login value="Erneut versuchen" class="btn btn-lg btn-success btn-block">
                            </fieldset>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

     <!-- Core Scripts - Include with every page -->
    <script src="assets/plugins/jquery-1.10.2.js"></script>
    <script src="assets/plugins/bootstrap/bootstrap.min.js"></script>
    <script src="assets/plugins/metisMenu/jquery.metisMenu.js"></script>

</body>

</html>
