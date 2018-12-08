seznam_zvirat = ["pes", "kocka", "kralik", "had","pavouk", "papousek"]

seznam_zvirat.append("andulka")

bez_prvniho_p = []

for zvire in seznam_zvirat:
    bez_prvniho_p.append(zvire[1:])

seznam_dvojic = []
for pismeno, zvire in zip(bez_prvniho_p, seznam_zvirat):
    dvojice = [pismeno, zvire]
    seznam_dvojic.append(dvojice)

seznam_dvojic.sort()

konecny_seznam = []
for zvire in seznam_dvojic:
    konecny_seznam.append(zvire[1])

print (konecny_seznam)
