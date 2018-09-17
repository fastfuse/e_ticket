
var osm = L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png"),

    mapboxLight = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZmFzdGZ1c2UiLCJhIjoiY2l1ZnN3cm0yMDAyczJ2dXZyYWZnaWVjciJ9.411LJ8YHIUYLmTGrfvfkLg"),

    mapboxStreets = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/streets-v10/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZmFzdGZ1c2UiLCJhIjoiY2l1ZnN3cm0yMDAyczJ2dXZyYWZnaWVjciJ9.411LJ8YHIUYLmTGrfvfkLg"),

    mapboxDark = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZmFzdGZ1c2UiLCJhIjoiY2l1ZnN3cm0yMDAyczJ2dXZyYWZnaWVjciJ9.411LJ8YHIUYLmTGrfvfkLg");


var baseMapLayers = {
    "Open Street Maps": osm,
    "Mapbox Streets": mapboxStreets,
    "Mapbox Light": mapboxLight,
    "Mapbox Dark": mapboxDark
};


var map = L.map('map-container', {
  center: [49.84104, 24.03164],
  zoom: 13,
  zoomControl: false,
  layers: [osm]
});


L.control.layers(baseMapLayers).addTo(map);


L.control.zoom({
  position: 'bottomright'
}).addTo(map);

// ============================================

// $.ajax({
//     type: "GET",
//     url: "static/data/city_stops.geojson",
//     dataType: "json",
//     success: function (response) {
//       stops_layer = L.geoJSON(response,{
//         onEachFeature: function(feature, layer){
//           layer.bindPopup(feature.properties.code);
//           layer.bindPopup('<a href="/info/'+feature.properties.code+'">'+feature.properties.name+'</a>');
//         }
//       })

//       stops_clustered = L.markerClusterGroup();
//       stops_clustered.addLayer(stops_layer);
//       map.addLayer(stops_clustered);
//     }
// });

// var locateControl = L.control.locate({
//   position: "bottomright",
//   flyTo: true,
//   drawCircle: true,
//   follow: true,
//   setView: true,
//   keepCurrentZoomLevel: true,
//   markerStyle: {
//     weight: 1,
//     opacity: 0.8,
//     fillOpacity: 0.8
//   },
//   circleStyle: {
//     weight: 1,
//     clickable: false
//   },
//   metric: true,
//   strings: {
//     title: "My location (where am I?)",
//     popup: "You are within {distance} {unit} from this point",
//     outsideMapBoundsMsg: "You seem located outside the boundaries of the map"
//   },
//   locateOptions: {
//     maxZoom: 18,
//     watch: true,
//     enableHighAccuracy: true,
//     maximumAge: 10000,
//     timeout: 10000
//   }
// }).addTo(map);

