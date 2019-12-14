function formatTypesOfWorkoutsPerPerson(data) {
    console.log('formatting data for typesOfWorkoutsPerPerson service');
    html = "<table id=\"dataTable\" class=\"table table-striped table-hover\">";
    html += "<th>Person</th><th>Erg</th><th>Bike</th><th>Run</th><th>Swim</th><th>Lift</th><th>Core</th>";
    for (i in data) {
        console.log(data[i]);
        html += "<tr>";
        html += buildCell(i);
        html += buildCell(data[i]['Erg']);
        html += buildCell(data[i]['Bike']);
        html += buildCell(data[i]['Run']);
        html += buildCell(data[i]['Swim']);
        html += buildCell(data[i]['Lift']);
        html += buildCell(data[i]['Core']);
        html += "</tr>";
    }
    html += "</table>"
    return html;
}