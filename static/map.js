// Map Setup
var mylocation = [6.099216, -0.018239]
var source_map = L.map('source_map').setView(mylocation, 13);
var dest_map = L.map('dest_map').setView(mylocation, 13);

var default_public_token = "pk.eyJ1IjoibWFwbm9xIiwiYSI6ImNrZTc4aXdweTEwY2wycXJ6cTg5NTE3aGsifQ.6soHRBucYxXoipUTzwvX5Q"

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: default_public_token
}).addTo(source_map);


L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: default_public_token
}).addTo(dest_map);


//Default View
var default_source_marker = L.marker(mylocation).addTo(source_map);
var default_dest_marker = L.marker(mylocation).addTo(dest_map);
default_source_marker.bindPopup("<br>Click on your location</br>").openPopup();
default_dest_marker.bindPopup("<br>Click on your location</br>").openPopup();

// Event handlers
var source_hidden_field = document.querySelector("#source_latlon");
var new_source_marker;
function onSourceMapClick(e) {
    //    alert("You clicked the map at " + e.latlng);
    if(default_source_marker){default_source_marker.removeFrom(source_map);}
    if(new_source_marker){new_source_marker.removeFrom(source_map);}
    new_source_marker = L.marker(e.latlng).addTo(source_map);
    new_source_marker.bindPopup("<b>Source</b>").openPopup();
    source_hidden_field.setAttribute("value", e.latlng);
}

var new_dest_marker;
var dest_hidden_field = document.querySelector("#dest_latlon");
function onDestMapClick(e) {
    //    alert("You clicked the map at " + e.latlng);
    if(default_dest_marker){default_dest_marker.removeFrom(dest_map);}
    if(new_dest_marker){new_dest_marker.removeFrom(dest_map);}
    new_dest_marker = L.marker(e.latlng).addTo(dest_map);
    new_dest_marker.bindPopup("<b>Destination</b>").openPopup();
    dest_hidden_field.setAttribute("value", e.latlng);
}


source_map.on('click', onSourceMapClick);
dest_map.on('click', onDestMapClick);
