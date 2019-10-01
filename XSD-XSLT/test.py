import StringIO
import xml.etree.ElementTree as ET
# import xml.etree.ElementTree as ET
f= open("sample.xml","r")
# tree = ET.parse(f)
# root = tree.getroot()
# for x in f:
# #     print (x)
# tree = ET.parse(f)
# root = tree.getroot()
# for child in root.findall('.'):
#     print(child.tag)
#     for tags in child:
#         print(tags.text)
#         
# =============================================================================
# ns = {'xs': 'http://www.w3.org/2001/XMLSchema'}

# for nameSpace in root.findall('xs:complexType', ns):
    # name = nameSpace.find('xs:sequence', ns)
    # print (nameSpace) 
    # for char in actor.findall('role:character', ns):
    #     print (' |-->', char.text)
# ============================================================================
# root = f
# for actor in root.findall('{http://www.w3.org/2001/XMLSchema}complexType'):
#     name = actor.find('{http://www.w3.org/2001/XMLSchema}element')
#     print (name.tag)
#     # for char in actor.findall('{http://characters.example.com}character'):
#     #     print (' |-->', char.text)



# instead of ET.fromstring(xml)
it = ET.iterparse(StringIO(f))
for _, el in it:
    if '}' in el.tag:
        el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
root = it.root
print (root)