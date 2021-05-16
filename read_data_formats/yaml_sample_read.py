import yaml

#Open the file as a string
with open("yaml_sample.yml") as data:
    yaml_sample = data.read()

#From yaml to dict
yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)

print(type(yaml_dict))
print(yaml_dict)

#Make a change in the name of the interface
yaml_dict["interface"]["name"] = "GigabitEthernet1"

#Show the change made in the interface
print(yaml.dump(yaml_dict, default_flow_style=False))

#To save the change to the file
with open("yaml_sample.xml", "w") as data:
    data.write(yaml.dump(yaml_dict, default_flow_style=False))

with open("yaml_sample.xml", "r") as data:
    data_last = data.read()


print("*"*20, "This is the actual file", "*"*20)
print(data_last)