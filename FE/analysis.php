<?php 
    session_start();
    header('Access-Control-Allow-Origin: *');
    require('func/EnableDebugSettings.php');
    require('func/RestrictToUsers.php');
    require('func/SqlConnector.php');
?>
<html>
<head>
    <link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre.min.css">
	<link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre-exp.min.css">
    <link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre-icons.min.css">
    <link rel="stylesheet" href="css/Analysis.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.bundle.js"></script>
    <!-- Service specific js file imports -->
        <script src="js/AnalysisServices/ErgMetersPerDay.js"></script>
        <script src="js/AnalysisServices/IndividualContributions.js"></script>
        <script src="js/AnalysisServices/TotalMetersPerSide.js"></script>
        <script src="js/AnalysisServices/TypesOfWorkoutsPerPerson.js"></script>
        <script src="js/AnalysisServices/WorkoutsPerPerson.js"></script>
    <!-- End of service specific js files -->
    <script src="js/Analysis.js"></script>
    <script src="js/chartBuilder.js"></script>
</head>
<body>
    <h1><a href='https://quikfo.com/rowlog'>Rowlog 4: A New [B]ope</a></h1>
	<div id="nav">
        <a href='index.php'>Home</a> |
        <a href='profile.php'>Profile</a> | 
        <a href='logout.php'>Logout</a>
    </div>
    <hr />
    <div id="container">
        <div class="formContainer">
            <form method="GET" action="analysis.php">
                <div class="form-group">
                    <label>
                        <select name="service" class="form-select">
                            <option>Choose an Analysis</option>
                            <option>averageMetersPerSide</option>
                            <option>ergMetersPerDay</option>
                            <option>individualContributions</option>
                            <option>longestWorkoutPerDay</option>
                            <option>totalMetersPerSide</option>
                            <option>typesOfWorkoutsPerPerson</option>
                            <option>workoutsPerPerson</option>
                        </select>
                    </label>
                    <br /><br />
                    <input type="submit" class="btn" value="Load Analysis" />
                </div>
            </form>
        </div>
        <hr />
        <div id="dataContainerHeader"></div>
        <div id="dataContainer"></div>
        <canvas id="dataChart" width="100%" height="50px"></canvas>
    </div>
    <hr />
    <h5>Created by Raymond Mattingly, Tadd Bindas, Tommy Burda, Chris Crawley, Logan Farmer, Jordan Irving. | Rowlog v2 2016-2020</h5> 
    <h6>If you want to contribute by writing services in Python which analyze Rowlog's data, then please reach out to one of the aforementioned people -- no prior knowledge necessary.</h6>
</body>
</html>
<?php 
    if (isset($_GET['service'])) {
        echo "<script>formatData('" . $_SESSION['user'] . "', '" . $_GET['service'] . "')</script>";
    }
?>
