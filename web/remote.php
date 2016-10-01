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
    <!-- PopUp -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h4 class="modal-title" id="myModalLabel">Hilfe:</h4>
          </div>
          <div class="modal-body">
          <li>Punkt 1</li>
          <li>Punkt 2</li>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" data-dismiss="modal">Schließen</button>
          </div>
          </div>
        </div>
      </div>
      <!-- End PopUp -->
    <table cellspacing=1 border=!>
      <tr><td>Bla
    </table>

    <button class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
      Hilfe
    </button>





                <!--End Page Header -->
  </div>
