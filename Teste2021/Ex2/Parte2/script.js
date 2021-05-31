let axios = require('axios')

let prefixes = `

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    PREFIX owl: <http://www.w3.org/2002/07/owl#>

    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    PREFIX noInferences: <ontotext.com/explicit>

    PREFIX skos: <w3.org/2004/02/skos/core#>

    PREFIX : <http://prc.di.uminho.pt/2021/myfamily#>

`   
    let query = encodeURI(prefixes + `CONSTRUCT {
        ?s1 :irmao ?s2 .
        ?s2 :irmao ?s1 .
    } WHERE {
        ?s1 :temProgenitor ?p1.
        ?s2 :temProgenitor ?p1.
    }`)

    
    axios.get('http://localhost:7200/repositories/family/statements?query=' + query)
        .then(res => {
            console.log(res.data)
            /*let data = res.data.results.bindings.map( e => {
                return `:${e.subject.value.split('#')[1]} :${e.predicate.value.split('#')[1]} :${e.object.value.split('#')[1]} .`
            })*/

            let query2 = `INSERT DATA { ${res.data} }`


            axios.get('http://localhost:7200/repositories/family/statements?query=' + encodeURI(query2))
              .then(_ => console.log("Done!"))
        })