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
    <table cellspacing=0 border=0 >
      <tr><td>
        <div id="stream" onmousemove="mousemove(event)" oncontextmenu="alert('Drücken sie STRG und bewegen sie gelichzeitig die Maus in dem Stream, um sich um zu schauen.');return false">
        <object data="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/?action=stream" width=640 height=480>
          <img src="http://<?php echo $_SERVER['SERVER_ADDR']; ?>/pictures/offline.png" alt="Just testing.">
        </object>
      </div>
        <!--<img src=http://<?php //echo $_SERVER['SERVER_ADDR']; ?>:8080/?action=stream />-->
      </td>
      <td>
        <h5>Kamera Einstellungen:</h5>
        <input type="range" min="0" max="100" step="1" value="50" data-orientation="horizontal">
        <script>
        $('input[type="range"]').rangeslider();
        $('input[type="range"]').rangeslider('destroy');
        $('input[type="range"]').rangeslider('update', true);
</script>
      </td>
    </tr>
  </table>
  <table cellspacing=0 border=0 >
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
          url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8081/cameramove/",
          data: { x: pos_x, y: pos_y },
        });
      }
    }

    function startStream() {
      $.ajax({
        url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8081/action/?action=startStream",
        type: 'get',
        dataType: 'jsonp',
      });
    }
    function stopStream() {
      $.ajax({
        url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8081/action/?action=stopStream",
        type: 'get',
        dataType: 'jsonp',
      });
    }
    function getStreamStatus() {
      $.ajax({
        url: "http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8081/status/?from=stream",
        success: function(data) {
          var response = JSON.stringify(data);
          var obj = $.parseJSON(response);
          var streamstatus = obj.online;
        }
          if(streamstatus == "online") {
            document.getElementById('Stream_On').className = "btn btn-success enabled";
            document.getElementById('Stream_Off').className = "btn btn-danger disabled";
          }
          else{
            document.getElementById('Stream_On').className = "btn btn-success disabled";
            document.getElementById('Stream_Off').className = "btn btn-danger enabled";
          }
        }
      });
    }
    getStreamStatus();
    </script>
