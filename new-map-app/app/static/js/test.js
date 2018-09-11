


var Item = React.createClass({
  render: function(){
    return(
      <div className="panel panel-primary">
        <div className="panel-heading">
          <h3 className="panel-title">{this.props.artist}</h3>
        </div>
        <div className="panel-body">
          {this.props.song}
        </div>
      </div>
    )
  }
})




var App = React.createClass({

  getInitialState: function(){
    return{
      result: []
    }
  },

  fetchData: function(){
    var rootUrl = 'http://api.genius.com'
    var searchUrl = rootUrl + '/search?q=Arctic%20Monkeys'

    // fetch('http://127.0.0.1:5000/ping?k=v%20ss&k2=v2&q=arctic', {
    //   method: 'GET',
    //   headers: {
    //     'Authorization': 'Bearer g3I0_dpr-oZRNdnLowg1uT7VznFugwXEZpFsBVExX6f-K7V2QUMiKBOxqoIVtxNs',
    //   },
    // }).then(function(response){
    //   console.log(response.json())
    //   var result = response.json()
    //   this.setState({
    //     result: result.response.hits
    //   })
    // }.bind(this))


    $.ajax({
      url: 'http://127.0.0.1:5000/ping?q=aya%20Black%20rebel',
      headers: {
        'Authorization': 'Bearer g3I0_dpr-oZRNdnLowg1uT7VznFugwXEZpFsBVExX6f-K7V2QUMiKBOxqoIVtxNs',
      },
      cache: false,
      success: function(data){
        console.log(data)
        this.setState({
          result: data.response.hits
        })
      }.bind(this),

      error: function(xhr, status, err) {
        console.error(status, err.toString());
      }
    })
  },


  componentDidMount: function(){
    this.fetchData()
  },


  render: function(){
    console.log(this.state)

    var hits = []

    this.state.result.forEach(function(item){
      // hits.push(item.result.full_title)
      hits.push(<Item artist={item.result.primary_artist.name}
                      song={item.result.title} />)
    })

    console.log(hits)

    return(
      <div className="row">
        <h3>test</h3>
        {hits}
      </div>
          )
  }
})











ReactDOM.render(
  <App />,
  document.getElementById('app')
)