<?php
session_start();
if(!$_SESSION['logged_in'])
    header("Location: login.php");
?>
<!DOCTYPE html>
<html>

<head>
    <title>LexoBot</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script type="text/javascript" src=http://<?php echo $_SERVER['SERVER_ADDR']; ?>/jquery.min.js></script>
    <!-- Core CSS - Include with every page -->
    <link href="assets/plugins/bootstrap/bootstrap.css" rel="stylesheet" />
    <link href="assets/font-awesome/css/font-awesome.css" rel="stylesheet" />
    <link href="assets/plugins/pace/pace-theme-big-counter.css" rel="stylesheet" />
    <link href="assets/css/style.css" rel="stylesheet" />
    <link href="assets/css/main-style.css" rel="stylesheet" />

</head>

<body>
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
    <!--  wrapper -->
    <div id="wrapper">
        <!-- navbar top -->
        <nav class="navbar navbar-default navbar-fixed-top" role="navigation" id="navbar">
            <!-- navbar-header -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".sidebar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="index.html">
                    <img src="assets/img/logo.png" alt="" />
                </a>
            </div>
            <!-- end navbar-header -->
            <!-- navbar-top-links -->
            <ul class="nav navbar-top-links navbar-right">
                <!-- main dropdown -->
                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                        <span class="top-label label label-danger">0</span><i class="fa fa-envelope fa-3x"></i>
                    </a>
                    <!-- dropdown-messages -->
                    <ul class="dropdown-menu dropdown-messages">
                        <li>
                            <a href="#">
                                <div>
                                    <strong><span class=" label label-danger">Andrew Smith</span></strong>
                                    <span class="pull-right text-muted">
                                        <em>Yesterday</em>
                                    </span>
                                </div>
                                <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eleifend...</div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#">
                                <div>
                                    <strong><span class=" label label-info">Jonney Depp</span></strong>
                                    <span class="pull-right text-muted">
                                        <em>Yesterday</em>
                                    </span>
                                </div>
                                <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eleifend...</div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#">
                                <div>
                                    <strong><span class=" label label-success">Jonney Depp</span></strong>
                                    <span class="pull-right text-muted">
                                        <em>Yesterday</em>
                                    </span>
                                </div>
                                <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eleifend...</div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a class="text-center" href="#">
                                <strong>Read All Messages</strong>
                                <i class="fa fa-angle-right"></i>
                            </a>
                        </li>
                    </ul>
                    <!-- end dropdown-messages -->
                </li>

                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                        <span class="top-label label label-success">4</span>  <i class="fa fa-tasks fa-3x"></i>
                    </a>
                    <!-- dropdown tasks -->
                    <ul class="dropdown-menu dropdown-tasks">
                        <li>
                            <a href="#">
                                <div>
                                    <p>
                                        <strong>Task 1</strong>
                                        <span class="pull-right text-muted">40% Complete</span>
                                    </p>
                                    <div class="progress progress-striped active">
                                        <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: 40%">
                                            <span class="sr-only">40% Complete (success)</span>
                                        </div>
                                    </div>
                                </div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#">
                                <div>
                                    <p>
                                        <strong>Task 2</strong>
                                        <span class="pull-right text-muted">20% Complete</span>
                                    </p>
                                    <div class="progress progress-striped active">
                                        <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 20%">
                                            <span class="sr-only">20% Complete</span>
                                        </div>
                                    </div>
                                </div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#">
                                <div>
                                    <p>
                                        <strong>Task 3</strong>
                                        <span class="pull-right text-muted">60% Complete</span>
                                    </p>
                                    <div class="progress progress-striped active">
                                        <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                            <span class="sr-only">60% Complete (warning)</span>
                                        </div>
                                    </div>
                                </div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#">
                                <div>
                                    <p>
                                        <strong>Task 4</strong>
                                        <span class="pull-right text-muted">80% Complete</span>
                                    </p>
                                    <div class="progress progress-striped active">
                                        <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: 80%">
                                            <span class="sr-only">80% Complete (danger)</span>
                                        </div>
                                    </div>
                                </div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a class="text-center" href="#">
                                <strong>See All Tasks</strong>
                                <i class="fa fa-angle-right"></i>
                            </a>
                        </li>
                    </ul>
                    <!-- end dropdown-tasks -->
                </li>

                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                        <span class="top-label label label-warning">5</span>  <i class="fa fa-bell fa-3x"></i>
                    </a>
                    <!-- dropdown alerts-->
                    <ul class="dropdown-menu dropdown-alerts">
                        <li>
                            <a href="#">
                                <div>
                                    <i class="fa fa-comment fa-fw"></i>New Comment
                                    <span class="pull-right text-muted small">4 minutes ago</span>
                                </div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#">
                                <div>
                                    <i class="fa fa-twitter fa-fw"></i>3 New Followers
                                    <span class="pull-right text-muted small">12 minutes ago</span>
                                </div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#">
                                <div>
                                    <i class="fa fa-envelope fa-fw"></i>Message Sent
                                    <span class="pull-right text-muted small">4 minutes ago</span>
                                </div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#">
                                <div>
                                    <i class="fa fa-tasks fa-fw"></i>New Task
                                    <span class="pull-right text-muted small">4 minutes ago</span>
                                </div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#">
                                <div>
                                    <i class="fa fa-upload fa-fw"></i>Server Rebooted
                                    <span class="pull-right text-muted small">4 minutes ago</span>
                                </div>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a class="text-center" href="#">
                                <strong>See All Alerts</strong>
                                <i class="fa fa-angle-right"></i>
                            </a>
                        </li>
                    </ul>
                    <!-- end dropdown-alerts -->
                </li>

                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                        <i class="fa fa-user fa-3x"></i>
                    </a>
                    <!-- dropdown user-->
                    <ul class="dropdown-menu dropdown-user">
                        <li><a href="#"><i class="fa fa-user fa-fw"></i>(Benutzer Profil)</a>
                        </li>
                        <li><a href="#"><i class="fa fa-gear fa-fw"></i>(Einstellungen)</a>
                        </li>
                        <li class="divider"></li>
                        <li><a href="logout.php"><i class="fa fa-sign-out fa-fw"></i>Abmelden</a>
                        </li>
                    </ul>
                    <!-- end dropdown-user -->
                </li>
                <!-- end main dropdown -->
            </ul>
            <!-- end navbar-top-links -->

        </nav>
        <!-- end navbar top -->

        <!-- navbar side -->
        <nav class="navbar-default navbar-static-side" role="navigation">
            <!-- sidebar-collapse -->
            <div class="sidebar-collapse">
                <!-- side-menu -->
                <ul class="nav" id="side-menu">
                    <li>
                        <!-- user image section-->
                        <div class="user-section">
                            <div class="user-section-inner">
                                <img src="assets/img/<?php echo $_SESSION['usr']; ?>.jpg" alt="">
                            </div>
                            <div class="user-info">
                                <div><strong><?php echo $_SESSION['usr']; ?></strong></div>
                                <div class="user-text-online">
                                    <span class="user-circle-online btn btn-success btn-circle "></span>&nbsp;Online
                                </div>
                            </div>
                        </div>
                        <!--end user image section-->
                    </li>
                    <li id="dashboard_menu">
                        <a href="#" onclick="clearselection(); show_dashboard(); return false;"><i class="fa fa-dashboard fa-fw"></i>&nbsp;Dashboard</a>
                    </li>
                    <li id="remote_menu">
                        <a href="#" onclick="clearselection(); show_remote(); return false;"><i class="fa fa-gamepad fa-fw"></i>&nbsp;Fernsteuerung</a>
                    </li>
                    <li id="camera_menu">
                        <a href="#" onclick="clearselection(); show_camera(); return false;"><i class="fa fa-video-camera fa-fw"></i>&nbsp;Kamera</a>
                    </li>
                    <li id="wireless_menu">
                        <a href="#" onclick="clearselection(); show_wireless(); return false;"><i class="fa fa-signal fa-fw"></i>&nbsp;Funk</a>
                    </li>
                    <li id="settings_menu">
                        <a href="#" onclick="clearselection(); show_settings(); return false;"><i class="fa fa-wrench fa-fw"></i>&nbsp;Einstellungen</a>
                    </li>
                    <li id="debug_menu">
                        <a href="#" onclick="clearselection(); show_debug(); return false;"><i class="fa fa-code fa-fw"></i>&nbsp;Debug</a>
                    </li>
                </ul>
                <!-- end side-menu -->
            </div>
            <!-- end sidebar-collapse -->
        </nav>
        <!-- end navbar side -->
        <!--  page-wrapper -->
        <div id="page-wrapper">
          <script>

          //Wenn Startseite aufgerufen wird, zeige Dashboard
          show_dashboard();

          //Public JS Functionen
          function delay(ms) {
            ms += new Date().getTime();
            while (new Date() < ms){}
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
              success: function(data) {
                var response = JSON.stringify(data);
                var obj = $.parseJSON(response);
                var streamstatus = obj.streamstatus;
                setTimeout(show_camera, 200);
              }
            });
          }
          
          function moveServo() {
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
          }

          //Menü Funktionen
          function clearselection() {
            document.getElementById("dashboard_menu").className = "";
            document.getElementById("remote_menu").className = "";
            document.getElementById("camera_menu").className = "";
            document.getElementById("wireless_menu").className = "";
            document.getElementById("settings_menu").className = "";
            document.getElementById("debug_menu").className = "";
          }

          function show_dashboard() {
            $(function(){
              $("#Content").load("dashboard.php");
            });
            document.getElementById("dashboard_menu").className = "selected";
          }
          function show_remote() {
            $(function(){
              $("#Content").load("remote.php");
            });
            document.getElementById("remote_menu").className = "selected";
          }
          function show_camera() {
            $(function(){
              $("#Content").load("camera.php");
            });
            document.getElementById("camera_menu").className = "selected";
          }
          function show_wireless() {
            $(function(){
              $("#Content").load("wireless.php");
            });
            document.getElementById("wireless_menu").className = "selected";
          }
          function show_settings() {
            $(function(){
              $("#Content").load("settings.php");
            });
            document.getElementById("settings_menu").className = "selected";
          }
          function show_debug() {
            $(function(){
              $("#Content").load("debug.php");
            });
            document.getElementById("debug_menu").className = "selected";
          }
          </script>

          <div id="Content"></div>

        </div>
        <!-- end page-wrapper -->

    </div>
    <!-- end wrapper -->

    <!-- Core Scripts - Include with every page -->
    <script src="assets/plugins/jquery-1.10.2.js"></script>
    <script src="assets/plugins/bootstrap/bootstrap.min.js"></script>
    <script src="assets/plugins/metisMenu/jquery.metisMenu.js"></script>
    <script src="assets/plugins/pace/pace.js"></script>
    <script src="assets/scripts/siminta.js"></script>

</body>

</html>
