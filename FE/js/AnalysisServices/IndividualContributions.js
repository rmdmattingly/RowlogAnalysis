function formatIndividualContributions(data, username) {
    console.log('formatting data for individual contributions');
    chartData = []
    // get universal data
    univData = data['universalAvg_metersPerDay'];
    univXs = []
    univYs = []
    for (i in univData) {
        univXs.push(i);
        univYs.push(univData[i]);
    }
    chartData.push({
        label: 'Team Average Meters',
        borderColor: 'rgba(92,10,10,0.8)',
        backgroundColor: 'rgba(92,10,10,0.1)',
        data: univYs
    });
    colorI = 150;
    colorI2 = 50;
    colorI3 = 150;
    boats = ["1v", "2v", "3v", "4v+"];
    colors = {
        "1v": "rgba(115,224,56,",
        "2v": "rgba(224,224,56,",
        "3v": "rgba(224,129,56,",
        "4v+": "rgba(224,56,56,"
    };
    for (i in boats) {
        boat = boats[i];
        boatData = data[boat + '_metersPerDayPerPerson'];
        name = boat + " - Average Meters Per Day";
        boatYs = [];
        for (i in boatData) {
            boatYs.push(boatData[i]);
        }
        color = colors[boat] + '0.8)';
        bgColor = colors[boat] + '0.1)';
        console.log(boat + ": " + color + " " + bgColor);
        chartData.push({
            label: name,
            borderColor: color,
            backgroundColor: bgColor,
            data: boatYs
        });
    }
    // get individual data
    indiData = data['byPerson_metersPerDay'];
    peopleToShow = [username];
    for (person in indiData) {
        indiLabel = person + ' - Meters';
        indiYs = [];
        for (dateI in univXs) {
            console.log(univXs[dateI]);
            console.log(indiData[person]);
            if (univXs[dateI] in indiData[person]) {
                indiYs.push(indiData[person][univXs[dateI]]);
            } else {
                indiYs.push(0);
            }
        }
        hide = true;
        console.log("is " + person + " in:");
        console.log(peopleToShow);
        if (peopleToShow.indexOf(person) > -1) {
            console.log('yes');
            hide = false;
        } else {
            console.log('no');
        }
        width = 3;
        if (person == username) {
            width = 6;
        }
        chartData.push({
            label: indiLabel,
            borderColor: 'rgba(' + colorI + ',' + colorI2 + ',' + colorI3 + ',0.8)',
            backgroundColor: 'rgba(' + colorI + ',' + colorI2 + ',' + colorI3 + ',0.0)',
            data: indiYs,
            hidden: hide,
            borderWidth: width
        });
        colorI = randomizeRGBColorInt(colorI);
        colorI2 = randomizeRGBColorInt(colorI2);
        colorI3 = randomizeRGBColorInt(colorI3);
    }
    buildLineChart(univXs, chartData);
    return ''; //empty string because there's no table html to return, only the chart
}