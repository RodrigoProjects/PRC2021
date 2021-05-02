import json

def main() -> ():

    with open('dataset.json') as f:
        data = json.loads(f.read())

    with open('output.owl', 'w') as out:
        for cidade in data["cidades"]:
            out.write(f'''
                ###  http://www.semanticweb.org/rodrigop/ontologies/2021/Cidades#{cidade["id"]}
                :{cidade["id"]} rdf:type owl:NamedIndividual ,
                                      :Cidade ;
                             :nome    "{cidade["nome"]}";
                             :população "{cidade["população"]}";
                             :descrição "{cidade["descrição"]}";
                             :distrito "{cidade["distrito"]}".
            ''')

        for ligacao in data["ligações"]:
             out.write(f'''
                ###  http://www.semanticweb.org/rodrigop/ontologies/2021/Cidades#{ligacao["id"]}
                :{ligacao["id"]} rdf:type owl:NamedIndividual ,
                                      :Ligação ;
                             :origem    :{ligacao["origem"]};
                             :destino :{ligacao["origem"]};
                             :distância "{ligacao["distância"]}".
            ''')


if __name__ == "__main__":
    main()