import xml.etree.ElementTree as ET 

with open("testfile.json", "a") as myfile:
	myfile.write('{')
	myfile.write('"Arkansas":') #CHANGE HERE
	myfile.write('{')
	myfile.write('"senators": [ ')

	myfile.write('{')
	myfile.write('"cand_name":"John Boozman",') #CHANGE HERE
	myfile.write('"party": "R",') #CHANGE HERE
	myfile.write('"contributor":[')
	tree = ET.parse('./xml files/ar john boozman.xml') #CHANGE HERE
	contributor = tree.getroot()[0]
	for child in contributor:
		org = str(child.attrib)
		myfile.write(org)
	myfile.write(']')
	myfile.write('},')

	myfile.write('{')
	myfile.write('"cand_name":"Tom Cotton",') #CHANGE HERE
	myfile.write('"party": "R",') #CHANGE HERE
	myfile.write('"contributor":[')
	tree = ET.parse('./xml files/ar tom cotton.xml') #CHANGE HERE
	contributor = tree.getroot()[0]
	for child in contributor:
		org = str(child.attrib)
		myfile.write(org)
	myfile.write(']')
	myfile.write('}')
	myfile.write(']')
	myfile.write('}')

	myfile.write('},') #REMOVE FROM LAST ONE