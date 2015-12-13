import xml.etree.ElementTree as ET
from pip.commands.search import print_results
tree = ET.parse('country_data.xml')
root = tree.getroot()

# if __name__ == '__main__':
#    pass
print type (root)
print root.keys()

for child in root:
    print child.tag, child.attrib
    
print root.getchildren()

for neighbor in root.iter('neighbor'):
    print neighbor.attrib
    
print "------------"

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print name, rank
print "------------" 
# panId = root.getchildren().index(ET.SubElement(root, "Panama"))

for panId, child in enumerate(root):
    if child.attrib['name'] == "Panama":
        break
print panId


print panId
Pol = ET.Element('country')
rank = ET.SubElement(Pol, 'Rank')
# rank. = "1234"
ET.SubElement(Pol, 'year')
ET.SubElement(Pol, 'gdppc')
ET.SubElement(Pol, 'neighbor')
Pol.attrib['name'] = 'Polska'
root.insert(panId + 1, Pol)

for child in root:
    print child.tag, child.attrib
print "------------+++++++"

  
tree.write("country_data2.xml")
