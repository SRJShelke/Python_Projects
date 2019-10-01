from lxml import etree, objectify
f= open("test.xsd","r")
metadata = f
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(metadata, parser)
root = tree.getroot()

####    
for elem in root.getiterator():
    if not hasattr(elem.tag, 'find'): continue  # (1)
    i = elem.tag.find('}')
    if i >= 0:
        elem.tag = elem.tag[i+1:]
objectify.deannotate(root, cleanup_namespaces=True)
####

# tree.write('done.xml',
#            pretty_print=True, xml_declaration=True, encoding='UTF-8')

# temp = open("done.xml")
# parser = etree.XMLParser(remove_blank_text=False)
# tree = etree.parse(temp, parser)
# root = tree.getroot()
elements=tree.xpath('//element')
tagList=list()
for t in elements:
    xmlTagName =(t.attrib['name'])
    # print(type(xmlTagName))
    tagList.append(xmlTagName)
# print(tagList)

# =========================================================

xslt_file= open("Final.xslt","w+")
first_line = '''<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:multimap="http://sap.com/xi/XI/SplitAndMerge">
	<xsl:template match="/">'''
xslt_file.write(first_line)
second_line = '<' + tagList[0]+'>\n'
xslt_file.write(second_line)
xslt_file.write('<xsl:for-each select="//'+tagList[1]+'">\n')
xslt_file.write('<' + tagList[1]+'>\n')
for tag in tagList[2:]:
	xslt_file.write('<' + tag +'>'+'<xsl:value-of select="'+tag+'"/>'+'</' + tag+'>\n')
xslt_file.write('</' + tagList[1]+'>\n')
xslt_file.write('</xsl:for-each>\n')
xslt_file.write('</' + tagList[0]+'>\n')
xslt_file.write('</xsl:template>\n</xsl:stylesheet>')

xslt_file.close()
xslt= open("Final.xslt","r")
parser2 = etree.XMLParser(remove_blank_text=True)
tree2 = etree.parse(xslt, parser2)
tree2.write('FinallyDone.xslt',
           pretty_print=True, xml_declaration=True, encoding='UTF-8')

