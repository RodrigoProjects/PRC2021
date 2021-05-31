import json

def main() -> ():

    with open('emd.json') as f:
        data = json.loads(f.read())

    with open('output.owl', 'w') as out:
        for emd in data:

            out.write(f'''
                ###  http://www.semanticweb.org/rodrigop/ontologies/2021/teste#teste_emd
                :clube_{emd["index"]} rdf:type owl:NamedIndividual ,
                                    :Clube ;
                            :nome "{emd["clube"]}" .
                            
            ''')

            out.write(f'''
                ###  http://www.semanticweb.org/rodrigop/ontologies/2021/teste#teste_emd
                :modal_{emd["index"]} rdf:type owl:NamedIndividual ,
                                    :Modalidade ;
                            :nome "{emd["modalidade"]}" .
                            
            ''')

            out.write(f'''
                ###  http://www.semanticweb.org/rodrigop/ontologies/2021/teste#teste_emd
                :atleta_{emd["index"]} rdf:type owl:NamedIndividual ,
                                    :Atleta ;
                            :nome "{emd["nome"]["primeiro"]} {emd["nome"]["último"]}" ;
                            :idade "{emd["idade"]}" ;
                            :genero "{emd["género"]}" ;
                            :morada "{emd["morada"]}" ;
                            :email "{emd["email"]}" ;
                            :federado "{emd["federado"]}" .

            ''')

            out.write(f'''
                ###  http://www.semanticweb.org/rodrigop/ontologies/2021/teste#teste_emd
                :{emd["_id"]} rdf:type owl:NamedIndividual ,
                                    :EMD ;
                            :data "{emd["dataEMD"]}" ;
                            :resultado "{emd["resultado"]}" ;
                            :temModalidade :modal_{emd["index"]} ;
                            :temAtleta :atleta_{emd["index"]} ;
                            :temClube :clube_{emd["index"]} .

            ''')


if __name__ == "__main__":
    main()