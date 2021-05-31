var express = require('express');
var router = express.Router();
var graphDB = require('../utils/fetchGraph')

/* GET home page. */
router.get('/emd', function(req, res, next) {

  if(req.query.res == "0K"){
    graphDB.fetch('select ?s where { ?s rdf:type :EMD ; :resultado "True" .}')
   .then(resp => {
     res.jsonp(resp.data)
   })
  }
  else {
    graphDB.fetch('select ?s ?r ?da ?nome where { ?s rdf:type :EMD ; :temAtleta ?a ; :resultado ?r ; :data ?da . ?a :nome ?nome}')
    .then(resp => {
      res.jsonp(resp.data)
    })
  }

});

router.get('/emd/:id ', (req, res) => {
  graphDB.fetch(`select ?p ?val where { :${req.params.id} rdf:type :EMD ; ?p ?val .}`)
  .then(resp => {
    res.jsonp(resp.data)
  })
})

router.get('/modalidades', (req, res) => {
  graphDB.fetch(`select distinct ?m where { ?s rdf:type :EMD ; :temModalidade ?m .}`)
  .then(resp => {
    res.jsonp(resp.data)
  })
})

router.get('/modalidades/:id', (req, res) => {
  graphDB.fetch(`select ?s where { ?s rdf:type :EMD ; :temModalidade ?m . ?m :nome "${req.params.id}"}`)
  .then(resp => {
    res.jsonp(resp.data)
  })
})

router.get('/atletas', (req, res) => {
  if(req.query.gen){
    graphDB.fetch(`select ?nome where { ?a rdf:type :Atleta ; :genero "${req.query.gen}" ; :nome ?nome .} order by ?nome`)
    .then(resp => {
      res.jsonp(resp.data)
    })
  }
  else if (req.query.clube) {
    graphDB.fetch(`select ?nome where { ?em rdf:type :EMD; :temAtleta ?a; :temClube ?c . ?a :nome ?nome . ?c :nome "${req.query.clube}" .} order by ?nome`)
    .then(resp => {
      res.jsonp(resp.data)
    })
  } else {
    res.sendStatus(400)
  }
})

module.exports = router;
