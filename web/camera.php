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
        <img src=http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/?action=stream />
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td><h5>&nbsp;<i class="fa fa-camera"></i>&nbsp;&nbsp;Stream&nbsp;&nbsp;</h5></td>
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
        success: function(data) {
          var response = JSON.stringify(data);
          var obj = $.parseJSON(response);
          var streamstatus = obj.online;
          alert(streamstatus)
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
