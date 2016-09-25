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
    <iframe src="http://<?php echo $_SERVER['SERVER_ADDR']; ?>/pictures/live.jpg" height="480" width="640" style="border:none;">
      <!--End Page Header -->
    </div>
