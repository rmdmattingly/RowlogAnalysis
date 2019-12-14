function formatWorkoutsPerPerson(data) {
    console.log('formatting data for workoutsPerPerson service');
    html = "<table id=\"dataTable\" class=\"table table-striped table-hover\">";
    html += "<th>Person</th><th>Number of Workouts</th>";
    for (i in data) {
        console.log(data[i]);
        html += "<tr>";
        html += buildCell(data[i][0]);
        html += buildCell(data[i][1]);
        html += "</tr>";
    }
    html += "</table>"
    return html;
}