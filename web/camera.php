<?php
session_start();
if(!$_SESSION['logged_in'])
    header("Location: login.php");
?>
  <div class="row">
    <!-- Page Header -->
    <div class="col-lg-12">
      <h1 class="page-header">Kamera</h1>
    </div>
    <table cellspacing=1 border=1>
      <tr><td>
        <div id="stream" onmousemove="delay(500); mousemove(event);" oncontextmenu="alert('Drücken sie STRG und bewegen sie gelichzeitig die Maus in dem Stream, um sich um zu schauen.');return false">
          <object data="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/?action=stream" width=640 height=480>
            <img src="pictures/offline.png" alt="Stream offline!">
          </object>
        </div>
      </td>
      <td>
      <h4>Kamera Einstellungen:</h4>
      <li><p id="show_stream_quality"></li>
      <input type="range" id="stream_quality" onchange="update_video_config();" value="20" min="0" max="100">
      <li>Helligkeit:</li>
      <input type="range" id="brightness" onchange="update_video_config();" value="20" min="0" max="100">
      <p id="servo_pos">
    </td>
  </tr>
  </table>
  <table cellspacing=1 border=1>
    <tr>
      <td><h5>&nbsp;<i class="fa fa-video-camera"></i>&nbsp;&nbsp;Stream&nbsp;&nbsp;</h5></td>
      <td><button type="button" id="Stream_On" class="btn btn-success" onclick="startStream();" >Start</button>
      &nbsp;&nbsp;</td>
      <td><button type="button" id="Stream_Off" class="btn btn-danger" onclick="stopStream();" >Stop</button>
      &nbsp;&nbsp;</td>
    </tr>
  </table>
      <!--End Page Header -->
    </div>
    <script>

    update_video_config();

    function update_video_config() {
      stream_quality = document.getElementById("stream_quality").value;
      $.ajax({
        url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8082/0/config/set?stream_quality=" + stream_quality,
      });
      document.getElementById("show_stream_quality").innerHTML = "Stream Qualität: " + stream_quality;
    }

    function get_video_config() {
      $.ajax({
        url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8082/0/config/get?query=stream_quality",
        success: function(data) {
          var response = data;
          alert(data);
          Script_On();
        }
      });
    }

    get_video_config();

    function mousemove(event) {
      strg = true;
      if(strg == true) {
        pos_x = event.offsetX?(event.offsetX):event.pageX-document.getElementById("stream").offsetLeft;
	      pos_y = event.offsetY?(event.offsetY):event.pageY-document.getElementById("stream").offsetTop;
        pos_x = (pos_x/640*180);
        pos_y = (pos_y/480*180);
        pos_x = pos_x.toFixed(0)
        pos_y = pos_y.toFixed(0)
        $.ajax({
          type: "GET",
          url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8081/cameramove/?x=" + pos_x + "&y=" + pos_y,
          dataType: 'jsonp',
          success: function(data) {
            var response = JSON.stringify(data);
            var obj = $.parseJSON(response);
            var mousemovestatus = obj.status;
            if(mousemovestatus != "success") {
              alert("Server reagiert nicht mehr!");
            }
          }
        });
        document.getElementById("servo_pos").innerHTML = "Servos: X: " + pos_x + " | Y: " + pos_y;
      }
    }
    function startStream() {
      $.ajax({
        url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8081/action/?action=startStream",
        type: 'get',
        dataType: 'jsonp',
        success: function(data) {
          var response = JSON.stringify(data);
          var obj = $.parseJSON(response);
          var streamstatus = obj.streamstatus;

          setTimeout(show_camera, 3000);
        }
      });
    }
    function stopStream() {
      $.ajax({
        url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8081/action/?action=stopStream",
        type: 'get',
        dataType: 'jsonp',
      });
    }
    </script>
