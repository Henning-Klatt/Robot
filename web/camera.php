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
      <td><iframe src="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8082/0/config/list/">
      </td>
    </tr>
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
    </script>
