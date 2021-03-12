var axios = require('axios')

export default function query(repo, q){
    var prefixes = `

    PREFIX rdf: <w3.org/1999/02/22-rdf-syntax-ns#>

    PREFIX owl: <w3.org/2002/07/owl#>

    PREFIX rdfs: <w3.org/2000/01/rdf-schema#>

    PREFIX noInferences: <ontotext.com/explicit>

    PREFIX skos: <w3.org/2004/02/skos/core#>

    PREFIX : <http://www.semanticweb.org/rodrigo/ontologies/prc2021/advocacias#>

`



    var getLink = `localhost:7200/repositories/${repo}" + "?query=`



    // var query = `SELECT ?s WHERE { ?s rdf:type owl:Class}`



    var encoded = encodeURIComponent(prefixes + q)



    return axios.get(getLink + encoded)

}

