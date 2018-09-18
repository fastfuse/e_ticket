class App extends React.Component{
  render(){
    return(<div className="row">
             <Sidebar />
             <Map />
           </div>
          )
  }
}


class Sidebar extends React.Component{
  render(){
    return(
      <div className="col-xs-12 col-md-4" id="sidebar">
        <Search />
      </div>
    )
  }
}


class Search extends React.Component{

  render(){
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
            <button className="btn btn-success btn-block" type="button"
              onClick={this.showDirections}>Show</button>
          </div>
        </div>

      </form>
    )
  }
}


class Map extends React.Component{
  componentDidMount() {

      console.log('didddddd')

      this.initMap()
    }

  initMap() {
        // var map = new google.maps.Map(document.getElementById('map'), {
        //   zoom: 13,
        //   center: {lat: 49.84104, lng: 24.03164}
        // });
const map = new window.google.maps.Map(document.getElementById('map'), {
      center: { lat: 41.0082, lng: 28.9784 },
      zoom: 8
    });

      }

  render(){
    return(<div className="col-xs-8" id="map"></div>)
  }
}



ReactDOM.render(
  <App />,
  document.getElementById('app')
)


// ======================   Maps part   =================================

  // function initMap() {
  //     var map = new google.maps.Map(document.getElementById('map'), {
  //       zoom: 13,
  //       center: {lat: 49.84104, lng: 24.03164}
  //     });
  //   }
