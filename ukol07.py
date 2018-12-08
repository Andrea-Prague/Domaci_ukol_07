rodne_cislo = input("Zadej rodne cislo")

def overeni_formatu(rodne_cislo):
    if int(rodne_cislo [0:5]) and "/" in rodne_cislo[6] and int(rodne_cislo[7:]):
        return True
    else:
        return False

def delitelne_jedenacti(rodne_cislo):
    seznam_rd = list(rodne_cislo)
    del seznam_rd[6]
    retezce_rd = ''.join(seznam_rd)
    if int(retezce_rd)%11==0:
        return True
    else:
        return False

def datum_narozeni(rodne_cislo):
    if rodne_cislo[2] =="0" or rodne_cislo[2]== "5":
        if rodne_cislo[0] == "0" or rodne_cislo[0]== "1":
            datum_narozeni = "{}{}.{}.20{}{}".format(rodne_cislo[4], rodne_cislo[5], rodne_cislo[3], rodne_cislo[0],rodne_cislo[1])
            return datum_narozeni
        else:
            datum_narozeni = "{}{}.{}.19{}{}".format(rodne_cislo[4], rodne_cislo[5], rodne_cislo[3], rodne_cislo[0],rodne_cislo[1])
            return datum_narozeni
    else:
        if rodne_cislo[0] == "0" or rodne_cislo[0]== "1":
            datum_narozeni = "{}{}.{}{}.20{}{}".format(rodne_cislo[4], rodne_cislo[5], rodne_cislo[2], rodne_cislo[3], rodne_cislo[0],rodne_cislo[1])
            return datum_narozeni
        else:
            datum_narozeni = "{}{}.{}{}.19{}{}".format(rodne_cislo[4], rodne_cislo[5], rodne_cislo[2], rodne_cislo[3], rodne_cislo[0],rodne_cislo[1])
            return datum_narozeni


def pohlavi(rodne_cislo):
        if rodne_cislo[2]=="0":
            return "muz"
        elif rodne_cislo[2]=="5":
            return "zena"
        else:
            return "nelze urcit"


print (overeni_formatu(rodne_cislo))
print (delitelne_jedenacti(rodne_cislo))
print (datum_narozeni(rodne_cislo))
print (pohlavi(rodne_cislo))

# Nedokazu najit lepsi zpusob, takze budu rada zpetnou vazbu :-)
