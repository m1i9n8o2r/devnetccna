#importing classes(methods) from my custome device.py
from device import Router, Switch

#Create a new object instances
rtr1 = Router("iosV", "15.6.7", "10.10.10.1")
rtr2 = Router("isr4221", "16.9.5", "10.10.10.5")
sw1 = Switch("Cat9300", "16.9.5", "10.10.10.8")
#Can now access instances of the object
print(rtr1.model)

#Can create new attibutes that were not called in the Class
rtr1.desc = "virtual router"
print(rtr1.desc)

#Calling the getdesc method
print("Rtr1:\n", rtr1.getdesc(), "\n", sep="")
print("Rtr2:\n", rtr2.getdesc(), "\n", sep="")
print("Sw1:\n", sw1.getdesc(), "\n", sep="")