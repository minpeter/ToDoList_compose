const COORDS = 'coords';



function handleGeoSucces(position) {
    
}

function handleGeoError() {
    console.log("cant acc");
}

function askForCoords() {
    navigator.geolocation.getCurrentPosition(handleGeoSucces, handleGeoError);
}

function loadCoords() {
    const loadCoords = localStorage.getItem(COORDS);
    if(loadCoords === null) {
        askForCoords();
    } else {

    }
}

function init() {
    loadCoords();
}

init();