import json

#Pasar el file de json a diccionario de python
#open the json file
with open("json_example.code-workspace") as data:
    json_data = data.read() # instanciate it like a string and sting object

json_dict = json.loads(json_data) # instanciate it as a dictionary object, se usa loads, porque json_data es un string


print(type(json_data))
print(type(json_dict))
print(json_dict)

#Now modify the description from the list
json_dict["interface"]["description"] = "Backup link"
print(json_dict)

#I want it to make it a json output again
with open("json_example.code-workspace", "w") as fh:
    json.dump(json_dict, fh, indent=4)

#Para ver que el file tiene el cambio que acabo de hacer por "Backup link"
with open("json_example.code-workspace", "r") as data:
    json_data = data.read()
    print(json_data)