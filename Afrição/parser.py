
with open("fractions.txt") as f:
    fractions = [line.split(',') for line in f.readlines()[1:]]

with open("fractions_payments.txt") as f:
    fractions_pay = [line.split(',') for line in f.readlines()[1:]]

with open("transactions.txt") as f:
    transactions = [line.split(',') for line in f.readlines()[1:]]
 

with open("output.ttl", 'w') as f:


    for pay in fractions_pay:
        f.write(f'''
            ###  http://www.semanticweb.org/rodrigop/ontologies/2021/3/untitled-ontology-9#MapaPagamento
            :mapa_{pay[0]} rdf:type owl:NamedIndividual ,
                                    :MapaPagamento ;
                          :jan "{pay[1] if pay[1].strip() != "" else 0}" ;
                          :fev "{pay[1] if pay[2].strip() != "" else 0}" ;
                          :mar "{pay[1] if pay[3].strip() != "" else 0}" ;
                          :abr "{pay[1] if pay[4].strip() != "" else 0}" ;
                          :mai "{pay[1] if pay[5].strip() != "" else 0}" ;
                          :jun "{pay[1] if pay[6].strip() != "" else 0}" ;
                          :jul "{pay[1] if pay[7].strip() != "" else 0}" ;
                          :ago "{pay[1] if pay[8].strip() != "" else 0}" ;
                          :set "{pay[1] if pay[9].strip() != "" else 0}" ;
                          :out "{pay[1] if pay[10].strip() != "" else 0}" ;
                          :nov "{pay[1] if pay[11].strip() != "" else 0}" ;
                          :dez "{pay[1] if pay[12].strip() != "" else 0}" .
        ''')

    for fraction in fractions:

        f.write(f'''
        ###  http://www.semanticweb.org/rodrigop/ontologies/2021/3/untitled-ontology-9#Fracao
        :{fraction[0][0] + fraction[0][3:] if "º" in fraction[0] else fraction[0]} rdf:type owl:NamedIndividual ,
                         :Fracao ;
                :fracao  "{fraction[1]}";
                :permilhagem "{fraction[2]}";
                :mensalidade "{fraction[3].strip()}";
                :temMapaPagamento :mapa{fraction[0][0] + fraction[0][3:] if "º" in fraction[0] else fraction[0]} .
        
        ''')

    remove_aspas = "\""

    for transaction in transactions:
        f.write(f'''
        ###  http://www.semanticweb.org/rodrigop/ontologies/2021/3/untitled-ontology-9#transacao
        :{transaction[0].replace('/', '_')} rdf:type owl:NamedIndividual ,
                            :Transacao ;
                   :tipo "{transaction[1]}" ;
                   :data "{transaction[2]}" ;
                   :valor "{transaction[3]}" ;
                   :entidade "{transaction[4]}" ;
                   :descricao "{transaction[5].strip().replace(remove_aspas, "")}" .
        ''')