seznam_zvirat = ["pes", "kocka", "kralik", "had"]

def slovo_v_seznamu(slovo):
    return slovo in seznam_zvirat

print (slovo_v_seznamu(input("Zadej slovo, ktere si myslis, ze je v seznamu")))
