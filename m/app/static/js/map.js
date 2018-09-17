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


    var map = L.map('map', {
      center: [49.84104, 24.03164],
      zoom: 13,
      zoomControl: false,
      layers: [osm]
    });

    L.control.layers(baseMapLayers).addTo(map);


    L.control.zoom({
      position: 'bottomright'
    }).addTo(map);
