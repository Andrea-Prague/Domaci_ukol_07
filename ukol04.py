def seznamy_zvirat(seznam_zvirat1, seznam_zvirat2):
    prunik_zvirat = []
    rozdil_zvirat1 = []
    rozdil_zvirat2 = []
    for zvire1 in seznam_zvirat1:
        if zvire1 in seznam_zvirat2:
            prunik_zvirat.append(zvire1)

    for zvire1 in seznam_zvirat1:
        if zvire1 not in seznam_zvirat2:
            rozdil_zvirat1.append(zvire1)

    for zvire2 in seznam_zvirat2:
        if zvire2 not in seznam_zvirat1:
            rozdil_zvirat2.append(zvire2)
    return prunik_zvirat, rozdil_zvirat1, rozdil_zvirat2

print (seznamy_zvirat(["pes","kocka"], ["had", "kocka"]))
