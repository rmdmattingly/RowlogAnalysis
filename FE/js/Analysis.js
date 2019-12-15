function buildCell(data) {
    return "<td>" + data + "</td>";
}

function randomizeRGBColorInt(colorI) {
    if (colorI < 125) {
        colorI += Math.round(Math.random() * 125);
    } else {
        colorI -= Math.round(Math.random() * 125);
    }
    return colorI;
}

function handleInformal(data) {
    console.log('handling informally because frontend handling of this service is not yet established');
    html = "<pre style=\"text-align:left\">" + JSON.stringify(data, null, 2) + "</pre>";
    console.log(html);
    return html;
}

function handleServiceFormatting(service, data, username) {
    switch(service) {
        case 'ergMetersPerDay':
            return formatErgMetersPerDay(data);
        case 'individualContributions':
            return formatIndividualContributions(data, username);
        case 'workoutsPerPerson':
            return formatWorkoutsPerPerson(data);
        case 'typesOfWorkoutsPerPerson':
            return formatTypesOfWorkoutsPerPerson(data);
        case 'totalMetersPerSide':
            return formatTotalMetersPerSide(data);
        default:
            return handleInformal(data);
    }
}

async function formatData(username, service) {
    document.getElementById('dataContainerHeader').innerHTML = '<h3>' + service + '</h3>';
    document.getElementById('dataContainer').innerHTML = '<div class="loading loading-lg"></div>';
    let response = await fetch(`https://quikfo.com/rowlog/api/analysis?service=` + service);
    let data = await response.json();
    html = handleServiceFormatting(service, data, username);
    document.getElementById('dataContainer').innerHTML = html;
}
