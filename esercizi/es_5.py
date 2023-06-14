#Abbiamo una classe definita per i veicoli.
#Creare due nuovi veicoli chiamati car1 e car2.
#Imposta car1 come una cabrio rossa del valore di 60000 con un nome Fer e car2 come un furgone blu chiamato Jump del valore di 10000

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s è un(a) %s %s del valore di $%.2f." % (self.name, self.kind, self.color, self.value)
        return desc_str

# your code goes here

# test code
print(car1.description())
print(car2.description())
