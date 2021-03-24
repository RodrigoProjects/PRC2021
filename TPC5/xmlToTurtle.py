from xml.etree import cElementTree as ElementTree
from sys import argv

def main() -> ():

    if len(argv) != 2:
        print("This script takes a XML file argument.\nExample: xmlToTurtle.py data.xml.")
        return
    
    tree = ElementTree.parse(argv[1])
    resources = list(tree.getroot())

    file_header = open("bibliography.owl").read()

    resources_tags = set()
    resources_child_tags = set()
    authors = []
    editors = []
    total_resources = 0

    with open("output.owl", "w") as out:

        out.write(file_header) # Classes and Object properties definitions.

        out.write("#################################################################\n")
        out.write("#    Individuals\n")
        out.write("#################################################################\n\n")

        for el in resources:
            resources_tags.add(el.tag)
            total_resources += 1

            for aut in el.findall('author'):
                authors.append(aut)
                
                out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/tpc5#{aut.attrib["id"]}\n')
                out.write(f':{aut.attrib["id"]} rdf:type owl:NamedIndividual ,\n')
                out.write(f'\t\t\t\t:Author ;\n')
                out.write(f'\t\t:name "{aut.text}" .\n\n')
            
            for edit in el.findall('editor'):
                editors.append(edit)

                out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/tpc5#{edit.attrib["id"]}\n')
                out.write(f':{edit.attrib["id"]} rdf:type owl:NamedIndividual ,\n')
                out.write(f'\t\t\t\t:Editor ;\n')
                out.write(f'\t\t:name "{edit.text}" .\n\n')
        
        for el in resources:

            out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/tpc5#{el.attrib["id"]}\n')
            out.write(f':{el.attrib["id"]} rdf:type owl:NamedIndividual ,\n')
            out.write(f'\t\t\t\t:{el.tag.capitalize()} ')

            for tag in list(el):
                resources_child_tags.add(tag.tag)

                if tag.tag == "author":
                    out.write(f';\n\t\t:hasAuthor :{tag.attrib["id"]} ')
                
                elif tag.tag == "editor":
                    out.write(f';\n\t\t:hasEditor :{tag.attrib["id"]} ')
                
                elif tag.tag == 'author-ref':
                    out.write(f';\n\t\t:hasAuthor :{tag.attrib["authorid"]} ')
                
                elif tag.tag == 'editor-ref':
                    out.write(f';\n\t\t:hasEditor :{tag.attrib["authorid"]} ')

                elif tag.tag == 'deliverables':
                    out.write(f';\n\t\t:deliverables "{", ".join([deli.tag + " - " + deli.attrib["url"] for deli in list(tag)])}" ')

                else:
                    out.write(f';\n\t\t:{tag.tag} "{tag.text}" ')
            
            out.write('.\n\n')


    print(f'Resources found on the xml: {", ".join([e.capitalize() for e in resources_tags])}.\n')
    print(f'Possible tags inside a resource: {", ".join([e.capitalize() for e in resources_child_tags])}.\n')
    print(f'Total resources: {total_resources}\n')
    print(f'Total authors: {len(authors)}\n')
    print(f'Total editors: {len(editors)}\n')
    print("Output file generated!")

if __name__ == '__main__':
    main()