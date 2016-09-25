<?php
session_start();
if(!$_SESSION['logged_in'])
    header("Location: login.php");
?>
<div class="row">
  <!-- Page Header -->
    <div class="col-lg-12">
      <h1 class="page-header">Fernsteuerung</h1>
    </div>
    <iframe src="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080" height="1000" width="1000" style="border:none;">
      <h3>Dein Browser unterstützt keine iFrames.</h3>
    </iframe>
                <!--End Page Header -->
  </div>
