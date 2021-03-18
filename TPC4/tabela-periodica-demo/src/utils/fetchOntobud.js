const axios = require('axios')

export function fetchOntobud(q){

    const body = new URLSearchParams()

    body.append('query', q)

    const config = {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    
      return axios.post('ontobud/api/rdf4j/query/tabela-periodica', body, config)
}