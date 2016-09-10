<!DOCTYPE html>
<html>
<script type=text/javascript>
  $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
  alert($SCRIPT_ROOT);
</script>
<script type="text/javascript" src= http://192.168.178.32/jquery.min.js></script>
<style>

#myProgress {
  position: relative;
  width: 100%;
  height: 30px;
  background-color: #ddd;
}

#myBar {
  position: absolute;
  width: 10%;
  height: 100%;
  background-color: #4CAF50;
}

#label {
  text-align: center;
  line-height: 30px;
  color: white;
}

#box {
  width: 110;
  border: 2px rgb(161, 161, 161) solid;
  padding: 0px;
  margin: 0px;
  border-radius: 7px;
}
</style>
<header>
  <title>Robot Remote</title>
</header>
<body onload="startTime(); checkonline(); getSensors();">
<center>
<table cellspacing=0 border=0>
<tr><td></td>
  <td><center><h3><u>Robot Remote</u></h3></center></td>
<td></td></tr>
<tr><td></td><td>
  <div style='
    width: 640px;
    border: 2px rgb(161, 161, 161) solid;
    padding: 0px;
    margin: 0px;
    border-radius: 10px;' >
      <font size="4"><p id="status"></p>
      </font>
    </div>
  </td></tr>
<tr><td valign="middle" align="center">
  <div id="box">
    Temperatur &uArr;:
    <div id="temp1">
    </div>
  </div>
<table cellspacing=0 border=0>
<tr><td></td>
  <td valign="middle" align="center"><img id="camera-up" width="30" height="30" ></img></td><td></td></tr><tr>
  <td valign="middle" align="center"><img id="camera-left" width="30" height="30" ></td>
  <td valign="middle" align="center"><img id="camera" width="30" height="30" onmousedown="resetCamera(); return false;" onmouseup="clearCamera(); return false;"></td>
  <td valign="middle" align="center"><img id="camera-right" width="30" height="30" ></td></tr>
<tr><td></td><td valign="middle" align="center"><img id="camera-down" width="30" height="30" ></td><td></td></tr>
</table></td>
<td valign="middle" align="center">
<div id="stream" onmousemove="mousemove(event)" oncontextmenu="context=true;return false" onmouseup="context=false; clearCamera(); return false">
  <img src="http://192.168.178.32/pictures/live.jpg"></td>
</div>
<td valign="middle" align="center">
  <div id="box">
    Temperatur &dArr;:
    <div id="temp2">
    </div>
  </div>
  <table cellspacing=0 border=0>
  <tr><td></td>
    <td valign="middle" align="center"><img id="bot-forward" width="30" height="30" ></img></td><td></td></tr><tr>
    <td valign="middle" align="center"><img id="bot-left" width="30" height="30" ></td>
    <td valign="middle" align="center"><img id="bot" width="30" height="30"></td>
    <td valign="middle" align="center"><img id="bot-right" width="30" height="30" ></td></tr>
  <tr><td></td><td valign="middle" align="center"><img id="bot-back" width="30" height="30" ></td><td></td></tr>
  </table>
</td>
</tr>
<tr><td><a href="#" onclick="help(); return false;">Hilfe</a>
</td>
  <td>
    <table cellspacing=0 border=0>
      <tr><td valign="middle" align="center">
        <div id="box">
        Zeit: <div id="clock"></div>
      </div>
      </td>
      <td valign="middle" align="center">
      <div id="box">
        Server IP: <div id="server-ip"></div>
      </div>
    </td>
  </td>
  <td valign="middle" align="center">
  <div id="box">
    Client IP: <div id="client-ip"></div>
  </div>
</td>
  </tr>
</table>
</td>
</tr>
</table>
</center>
<script>
function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('clock').innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}
</script>
<script type="text/javascript">

//IP des Roboters
var intip = location.host.split(":")[0];
httpip = "http://" + intip;
strg = false;

//Bilder laden
function loadImages(src) {
  if (document.images) {
    img1 = new Image();
    img1.src = src;
  }
}
loadImages( httpip + "/pictures/leer.png");
loadImages( httpip + "/pictures/up.png");
loadImages( httpip + "/pictures/down.png");
loadImages( httpip + "/pictures/left.png");
loadImages( httpip + "/pictures/right.png");
loadImages( httpip + "/pictures/camera.png");
loadImages( httpip + "/pictures/bot.png");

//Tastatur Events registrieren
window.addEventListener("keydown", keysPressed, false);
window.addEventListener("keyup", keysReleased, false);


function help() {
  alert("Hilfe:\nSTRG + Mausbewegung: Kamera bewegen\nPfeiltasten: Kamera Positionen ansteuern\nW/A/S/D: Roboter bewegen")
}

function mousemove(event) {
  if(strg == true || context == true) {
    pos_x = event.offsetX?(event.offsetX):event.pageX-document.getElementById("stream").offsetLeft;
	   pos_y = event.offsetY?(event.offsetY):event.pageY-document.getElementById("stream").offsetTop;
     pos_x = (pos_x/640*10)+2.9;
     pos_y = (pos_y/480*10)+2.5;
     pos_x = pos_x.toFixed(1);
     pos_y = pos_y.toFixed(1);
     $.ajax({
       type: "GET",
       url: $SCRIPT_ROOT + "/cameramove/",
       data: { x: pos_x, y: pos_y },
     });
   }
}

//Verbindung da?
setInterval(checkonline, 3000)
verbindung = null;
function checkonline() {
  $(function() {
           $.ajax({
              type: "GET",
              url: $SCRIPT_ROOT + "/online/",
              contentType: "application/json; charset=utf-8",
              data: { aktion: "online" },
              success: function(data) {
                clientIP = data.value;
                $('#client-ip').text(clientIP);
                verbindung = true;
                document.body.style.backgroundColor = "#DEDEDE";
              },
              error: function(data) {
                  verbindung = false;
                  document.body.style.backgroundColor = "#ff7f50";
                  aktion = "Verbindung fehgeschlagen! (Neuversuch alle 3 Sekunden)"
                  document.getElementById("status").innerHTML = "Aktion: " + aktion;
              }
      });
    });
    getServerIP();
}
function getServerIP() {
  if(verbindung == true) {
    serverIP = location.host.split(":")[0];
    document.getElementById("server-ip").innerHTML = serverIP;
  }

  else{
    serverIP = "-";
    document.getElementById("server-ip").innerHTML = serverIP;
    clientIP = "-";
    document.getElementById("client-ip").innerHTML = clientIP;
  }
}
//Sensor Werte empfangen
setInterval(getSensors, 5000)
function getSensors() {
  if(verbindung == true) {
    $.ajax({
       type: "GET",
       url: $SCRIPT_ROOT + "/sensors/",
       data: { aktion: "all" },
       success: function(data) {
         temp1 = data.temp1;
         temp2 = data.temp2;
         document.getElementById("temp1").innerHTML = temp1 + " &deg;C";
         document.getElementById("temp2").innerHTML = temp2 + " &deg;C";
       }
     });
  }
  else {
    document.getElementById("temp1").innerHTML = "-";
    document.getElementById("temp2").innerHTML = "-";
  }

}

//Alles reseten
resetRobot();

function resetRobot() {
  document.getElementById("status").innerHTML = "Aktion: Warte auf Eingabe";

  document.getElementById("camera-up").src= httpip  + "/pictures/leer.png";
  document.getElementById("camera-left").src= httpip + "/pictures/leer.png";
  document.getElementById("camera-right").src= httpip + "/pictures/leer.png";
  document.getElementById("camera-down").src= httpip + "/pictures/leer.png";
  document.getElementById("camera").src= httpip + "/pictures/camera.png";
  document.getElementById("bot").src= httpip + "/pictures/bot.png";
  document.getElementById("bot-forward").src= httpip  + "/pictures/leer.png";
  document.getElementById("bot-left").src= httpip + "/pictures/leer.png";
  document.getElementById("bot-right").src= httpip + "/pictures/leer.png";
  document.getElementById("bot-back").src= httpip + "/pictures/leer.png";

  fehler = false;

  camera_up = false;
  camera_left = false;
  camera_right = false;
  camera_down = false;
  bot_forward = false;
  bot_left = false;
  bot_right = false;
  bot_back = false;

  clearCamera()

}
function stopRobot(direction) {

  document.getElementById("status").innerHTML = "Aktion: Roboter " + direction + " gestoppt - Warte auf Eingabe";
  document.getElementById(direction).src= httpip + "/pictures/leer.png";
  //Stoppe alle Fahrt Bewegungen
  $.ajax({
     type: "GET",
     url: $SCRIPT_ROOT + "/drive/",
     data: { aktion: "stop-" + direction },
   });

   bot_forward = false;

}

function stopCamera(direction) {
  document.getElementById("status").innerHTML = "Aktion: Kamera gestoppt - Warte auf Eingabe";
  document.getElementById(direction).src= httpip + "/pictures/leer.png";

  //Wird eine Taste gerade gedrückt? -Nein
  camera_up = false;
  camera_left = false;
  camera_right = false;
  camera_down = false;

  //Stoppe alle Kamera Bewegungen
  $.ajax({
     type: "GET",
     url: $SCRIPT_ROOT + "/camera/",
     data: { aktion: "stop-" + direction },
   });
}

var keys = [];

function clearCamera() {
  $.ajax({
    type: "GET",
    url: $SCRIPT_ROOT + "/camera/",
    data: { aktion: "clear" },
    });
}
function resetCamera() {
  $.ajax({
    type: "GET",
    url: $SCRIPT_ROOT + "/camera/",
    data: { aktion: "reset" },
    });
}


function keysPressed(e) {

    e.preventDefault();

    key = e.keyCode;
    keys[key] = true;
    aktion = false

    switch(key) {

      case 18: //alt
        aktion = "Servos 0 stellen"
        resetRobot();
        break;

      case 17: //STRG
        strg = true;
        aktion = "Kamera mit Maus bewegen"
        break;

      case 87: //W
        aktion = "Vorwärts";
        document.getElementById("bot-forward").src= httpip + "/pictures/up.png";
        if(bot_forward == false) { //Taste wird aktuell noch nicht gedrückt
          $.ajax({
            type: "GET",
            url: $SCRIPT_ROOT + "/drive/",
            data: { aktion: "forward" },
            });
          bot_forward = true; //Taste aktuell gedrückt
        }
        break;

      case 37: //Pfeil links
          aktion = "camera-left";
          document.getElementById("camera-left").src= httpip + "/pictures/left.png";
          if(camera_left == false) { //Taste wird aktuell noch nicht gedrückt
            $.ajax({
              type: "GET",
              url: $SCRIPT_ROOT + "/camera/",
              data: { aktion: "left" },
              });
            camera_left = true; //Taste aktuell gedrückt
          }
          break;

      case 38: //Pfeil hoch
          aktion = "camera-up";
          document.getElementById("camera-up").src= httpip + "/pictures/up.png";
          if(camera_up == false) { //Taste wird aktuell noch nicht gedrückt
            $.ajax({
               type: "GET",
               url: $SCRIPT_ROOT + "/camera/",
               data: { aktion: "up" },
             });
            camera_up = true; //Taste aktuell gedrückt
          }
          break;

      case 39: //Pfeil rechts
          aktion = "camera-right";
          document.getElementById("camera-right").src= httpip + "/pictures/right.png";
          if(camera_right == false) { //Taste wird aktuell noch nicht gedrückt
            $.ajax({
               type: "GET",
               url: $SCRIPT_ROOT + "/camera/",
               data: { aktion: "right" },
            });
            camera_right = true; //Taste aktuell gedrückt
          }
          break;

      case 40: //Pfeil runter
          aktion = "camera-down";
          document.getElementById("camera-down").src= httpip + "/pictures/down.png";
          if(camera_down == false) { //Taste wird aktuell noch nicht gedrückt
            $.ajax({
               type: "GET",
               url: $SCRIPT_ROOT + "/camera/",
               data: { aktion: "down" },
             });
            camera_down = true; //Taste aktuell gedrückt
          }
          break;
    }
    if(aktion == false) {
      aktion = "Unbekannte Taste " + key;
      fehler = true;
    }

    document.getElementById("status").innerHTML = "Aktion: " + aktion;

    // Ctrl + f
    if (keys[17] && keys[70]) {
        // irgendwas

    }
}

function keysReleased(e) {
  e.preventDefault();
  key = e.keyCode;
  switch(key) {

    case 17: //STRG
      strg = false;
      aktion = "Warte auf Eingabe";
      document.getElementById("status").innerHTML = "Aktion: " + aktion;
      break;

    case 87:
      stopRobot("bot-forward");
      break;

    case 37:
      stopCamera("camera-left");
      break;

    case 38:
      stopCamera("camera-up");
      break;

    case 39:
      stopCamera("camera-right");
      break;

    case 40:
      stopCamera("camera-down");
      break;
  }
  if(!(fehler==true)) {
    keys[e.keyCode] = false;
    //stopRobot();
  }
  else{
    resetRobot();
  }
}

</script>
</body>
</html>
