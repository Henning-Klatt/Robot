<?php
session_start();
if(!$_SESSION['logged_in'])
  header("Location: login.php");
?>
  <div class="row">
    <!-- Page Header -->
    <div class="col-lg-12">
      <h1 class="page-header">Einstellungen</h1>
    </div>

    <table>
      <!--SERVER SCRIPT-->
      <tr><td>
        <h5>&nbsp;<i class="fa fa-play"></i>&nbsp;&nbsp;Server Script&nbsp;&nbsp;</h5>
      </td><td>
        <button type="button" id="Script_On" class="btn btn-success" onclick="startScript();" >Start</button>
        &nbsp;&nbsp;
      </td><td>
        <button type="button" id="Script_Off" class="btn btn-danger" onclick="stopScript();" >Stop</button>
        &nbsp;&nbsp;
      </td></tr>
      <!--HOSTAPD-->
      <tr><td>
        <h5>&nbsp;<i class="fa fa-signal"></i>&nbsp;&nbsp;HotSpot&nbsp;&nbsp;</h5>
      </td><td>
        <button type="button" id="HotSpot_On" class="btn btn-success" onclick="startHotSpot();" >Start</button>
        &nbsp;&nbsp;
      </td><td>
        <button type="button" id="HotSpot_Off" class="btn btn-danger" onclick="stopHotSpot();" >Stop</button>
        &nbsp;&nbsp;
      </td></tr>

      <script>

      checkonline();
      setInterval(checkonline, 5000)

      function checkonline() {
        var verbindung = false;
        $.ajax({
          url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/online/",
          type: 'get',
          dataType: 'jsonp',
          success: function(data) {
            var response = JSON.stringify(data);
            var obj = $.parseJSON(response);
            var verbindung = obj.online;
            Script_On();
          }
        });
        if(verbindung == false) {
          Script_Off();
        }
      }

      function stopScript() {
        $.ajax({
          url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/action/?action=stopScript",
          type: 'get',
          dataType: 'jsonp',
        });
        Script_Off();
      }

      function startScript() {
        $.ajax({
          url: 'startScript.php',
        });
        Script_On();
      }

      function Script_On() {
        document.getElementById('Script_On').className = "btn btn-success disabled";
        document.getElementById('Script_Off').className = "btn btn-danger enabled";
      }
      function Script_Off() {
        document.getElementById('Script_Off').className = "btn btn-danger disabled";
        document.getElementById('Script_On').className = "btn btn-success enabled";
      }
      </script>

      <!--End Page Header -->
    </div>
