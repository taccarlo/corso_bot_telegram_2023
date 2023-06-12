print("dire amici ed entrate")

parola = input(" inserisci una parola ")
tentativi = 0

if parola != ("amici"):
    print("non sento nulla ma una presenza si avvicina")
    parola = input(" inserisci una parola ")
    tentativi = tentativi + 1

if parola != ("amici") and tentativi == 1:
    print("non succede nulla, ma la creatura è ancora piu vicina")
    parola = input(" inserisci una parola ")
    tentativi = tentativi + 1

if parola != ("amici") and tentativi == 2:
    print("attento la bestia è QUI")
elif parola == ("amici"):
    print("benvenuti a moira")


