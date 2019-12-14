function formatErgMetersPerDay(data) {
    console.log('formatting data for ergMetersPerDay service');
    html = "<table id=\"dataTable\" class=\"table table-striped table-hover\">";
    html += "<th>Date</th><th>Meters</th>";
    xs = []
    ys = []
    for (i in data) {
        xs.push(i);
        ys.push(data[i]);
        html += "<tr>";
        html += buildCell(i);
        html += buildCell(data[i]);
        html += "</tr>";
    }
    html += "</table>";
    data = [{
        label: 'Erg Meters',
        borderColor: 'rgba(10,10,92,0.2)',
        backgroundColor: 'rgba(10,10,92,0.2)',
        data: ys
    }];
    buildLineChart(xs, data);
    return html;
}