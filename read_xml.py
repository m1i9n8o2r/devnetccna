import xmltodict

#open the reader
with open("xml_sample.xml") as data:
    xml_example = data.read()

#From xml to dict
xml_dict = xmltodict.parse(xml_example)

print(xml_dict)

#Making a change
xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.55.3"

#Seeing the change in xml format
print(xmltodict.unparse(xml_dict, pretty=True))

#To write the changes to the actual file
with open ("xml_sample.xml", "w") as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))

#Para leer el file despues del cambio anterior
with open("xml_sample.xml") as data:
    xml_example = data.read()

print(xml_example)
