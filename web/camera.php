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
        <img src=http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/?action=stream />
      </td>
      <td>
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
