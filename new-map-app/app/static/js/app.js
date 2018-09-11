var App = React.createClass({
  render: function(){
    return(<div className="row">
             <Sidebar />
             <Map />
           </div>
          )
  }
})


var Sidebar = React.createClass({
  render: function(){
    return(
      <div className="col-xs-3" id="sidebar">
      <Title />
      <Search />
      </div>
    )
  }
})


var Title = React.createClass({
  render: function(){
    return(
      <h3>Map App</h3>
    )
  }
})


var origin, destination;


var Search = React.createClass({

  getInitialState: function(){
    return{
      origin: '',
      destination: ''
    }
  },

  componentDidMount: function(){
    var autocompleteFrom = new google.maps.places.Autocomplete(document.getElementById("origin"));
    var autocompleteTo = new google.maps.places.Autocomplete(document.getElementById("destination"));

    autocompleteFrom.addListener('place_changed', function(){
      origin = autocompleteFrom.getPlace();
      L.marker(origin.geometry.location.toJSON()).addTo(map).bindPopup(origin.formatted_address)
    })

    autocompleteTo.addListener('place_changed', function(){
      destination = autocompleteTo.getPlace();
      L.marker(destination.geometry.location.toJSON()).addTo(map).bindPopup(destination.formatted_address)
    })
  },

  showDirections: function(){
    var directionsService = new google.maps.DirectionsService();
    var originInput = new google.maps.places.Autocomplete(document.getElementById("origin"));
    var destinationInput = new google.maps.places.Autocomplete(document.getElementById("destination"));

    // var origin = originInput.getPlace().geometry.location.toJSON()
    // var destination = destinationInput.getPlace().geometry.location.toJSON()

    var request = {
      origin: origin.geometry.location.toJSON(),
      destination: destination.geometry.location.toJSON(),
      travelMode: 'WALKING'
    }

    directionsService.route(request, function(result, status) {
      if (status == 'OK') {
        console.log(result);

        var latLngs = []

        for(var el in result.routes[0].overview_path){
          latLngs.push(result.routes[0].overview_path[el].toJSON())
        }

        L.polyline(latLngs).addTo(map)

        for(var el in result.routes[0].overview_path){
          console.log(result.routes[0].overview_path[el].toJSON())
        }
      }
      else{
        console.log('Error')
      }
    });

  },

  render: function(){
    return(
      <form className="form-horizontal">
        <h4>Search route:</h4>

        <div className="form-group">
          <div className="col-xs-12">
            <input type="text" className="form-control" id="origin" placeholder="From" />
          </div>
        </div>

        <div className="form-group">
          <div className="col-xs-12">
            <input type="text" className="form-control" id="destination" placeholder="To" />
          </div>
        </div>

        <div className="form-group">
          <div className="col-xs-12">
            <button className="btn btn-success pull-right" type="button"
              onClick={this.showDirections}>Show</button>
          </div>
        </div>

      </form>
    )
  }
})


var Map = React.createClass({
  render: function(){
    return(<div className="col-xs-9 map-container" id="map-container"></div>)
  }
})










ReactDOM.render(
  <App />,
  document.getElementById('app')
)



// ======================   Maps part   =================================

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

