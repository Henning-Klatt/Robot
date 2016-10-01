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
    <table cellspacing=1 border=!>
      <tr><td>Blab
    </table>

    <button class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
      Hilfe
    </button>





                <!--End Page Header -->
  </div>
