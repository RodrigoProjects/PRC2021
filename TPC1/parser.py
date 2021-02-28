import json
import codecs

OUTPUT_FILE = "data.ttl"
INPUT_FILE = "data.json"

def stringify(string):
    return '"' + string + '"'

def main():
    with open(INPUT_FILE) as json_file:
        data = json.load(json_file)
    
    with codecs.open(OUTPUT_FILE, 'w', 'utf-8') as output:
        output.write("###############################\n")
        output.write("# INDIVIDUALS\n")
        output.write("###############################\n\n")

        for key in data:
            output.write(f'### {key} Individuals\n\n')
            for ind in data[key]:
                output.write(f':{ind["id"]} rdf:type owl:NameIndividual ,\n\t\t\t{key}')

                for attr in ind:
                    if attr != "id":
                        if isinstance(ind[attr], list):
                            for idx, el in enumerate(ind[attr]):
                                if idx == 0:
                                    output.write(f' ;\n\t\t\t:{attr} {stringify(ind[attr][0]) if ind[attr][0][0] != ":" else ind[attr][0]}')
                                
                                else:
                                    output.write(f' ,\n\t\t\t\t{stringify(el) if el[0] != ":" else el}')              
                                
                        else: 
                            output.write(f' ;\n\t\t\t:{attr} {stringify(ind[attr]) if ind[attr][0] != ":" else ind[attr]}')
         
                output.write(' .\n\n')



if __name__ == "__main__":
    main()