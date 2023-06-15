#Aggiungi una funzione denominata list_benefits() che restituisca il seguente elenco di stringhe: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
#Aggiungere una funzione denominata build_sentence(info) che riceve un singolo argomento contenente una stringa e restituisce una frase che inizia con la stringa data e termina con la stringa " is a benefit of functions!"

def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()