from xml.etree import cElementTree as ElementTree

def main() -> ():
    tree = ElementTree.parse('data.xml')
    resources = list(tree.getroot())

    resources_tags = set()
    authors = []

    for el in resources:
        resources_tags.add(el.tag)
        for aut in el.findall('author'):
            authors.append(aut)
    

    print(f'Resources found on the xml: {", ".join([e.capitalize() for e in resources_tags])}')
    print(f'Total authors: {len(authors)}')
    

if __name__ == '__main__':
    main()