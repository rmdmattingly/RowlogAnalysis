function formatTotalMetersPerSide(data) {
    console.log('formatting data for totalMetersPerSide service');
    html = "<table id=\"dataTable\" class=\"table table-striped table-hover\">";
    html += "<th>Ports</th><th>Starboards</th>";
    html += "<tr>";
    html += "<td>" + data['port'] + "</td>";
    html += "<td>" + data['starboard'] + "</td>";
    html += "</tr>";
    html += "</table>"
    return html;
}