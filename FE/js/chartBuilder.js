function buildLineChart(xs, data) {
    var ctx = document.getElementById('dataChart');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xs,
            datasets: data
        },
        options: {
            responsive: true,
            title:{
                display:true,
                text:'Select an Item in the Legend to Include it on the Chart'
            },
            tooltips: {
                mode: 'nearest',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}