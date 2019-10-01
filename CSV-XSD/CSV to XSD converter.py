#import necessary modules
import csv
import pandas as pd
from lxml import etree, objectify

# open file as pandas DataFrame
csv_file_name = input("Enter the CSV File Name : ")
csv_file=open(csv_file_name,'r')
df = pd.read_csv(csv_file)

# Get the Required Column
columnName = input("Enter the Column Name : ")
saved_column = df[columnName]
rootTags = input("Enter the Name of Root Tags : ")

print(saved_column)

# Create XSD file
xsd_file= open("output.xsd","w+")

xsd_file.write('''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">'''+'<xs:element name="' +rootTags+'">\n'+'''<xs:complexType><xs:sequence><xs:element minOccurs="0" maxOccurs="unbounded" name="'''+ rootTags + '">'+'''<xs:complexType>
                        <xs:sequence>''')
      
for col in range(saved_column.count()):
	xsd_file.write('''<xs:element nillable="false" minOccurs="0"  maxOccurs="unbounded" name="'''+saved_column[col]+'"></xs:element>')


xsd_file.write('''</xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>			
    </xs:element>
</xs:schema>''')


xsd_file= open("output.xsd","r")
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(xsd_file, parser)
tree.write('Output.xsd',
           pretty_print=True, xml_declaration=True, encoding='UTF-8')

