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
car1 = Vehicle()
car1.kind = "cabrio"
car1.color = "rosso"
car1.name = "Fer"
car1.value = 60000

car2 = Vehicle()
car2.kind = "furgone"
car2.color = "blu"
car2.name = "Jump"
car2.value = 10000

# test code
print(car1.description())
print(car2.description())
