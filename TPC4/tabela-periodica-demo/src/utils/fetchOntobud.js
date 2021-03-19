const axios = require('axios')

export function fetchOntobud(q){

    let prefixes = `

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    PREFIX owl: <http://www.w3.org/2002/07/owl#>

    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    PREFIX noInferences: <ontotext.com/explicit>

    PREFIX skos: <w3.org/2004/02/skos/core#>

    PREFIX : <http://www.daml.org/2003/01/periodictable/PeriodicTable#>

`

    const body = new URLSearchParams()

    body.append('query', prefixes + q)

    const config = {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    
      return axios.post('http://localhost:8080/ontobud/api/rdf4j/query/tabela-periodica', body, config)
}