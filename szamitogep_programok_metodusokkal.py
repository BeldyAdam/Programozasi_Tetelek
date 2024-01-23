from Szamitogep import Szamitogep

def szamitogepekListabaRendezes():
    peldany1 = Szamitogep("win", 32)
    peldany2 = Szamitogep("mac", 16)
    peldany3 = Szamitogep("win", 16)

    szamitogepek = []

    szamitogepek.append(peldany1)
    szamitogepek.append(peldany2)
    szamitogepek.append(peldany3)

    return szamitogepek

def szamitogepekListaKiirasa(lista):
    for i in range(len(lista)):
        oprsz = lista[i].oprsz
        ram = lista[i].ram
        print(f"{oprsz} ({ram})")

# szamitogepekLista = szamitogepekListabaRendezes()
# szamitogepekListaKiirasa(szamitogepekLista)

def osszegzesTetel(lista):
    print("Átlag: ", end="")
    ossz = 0
    for i in range(len(lista)):
        ossz += lista[i].ram
    print((round(ossz) / len(lista), 3))

osszegzesTetel(szamitogepekListabaRendezes())

def maximumKivalasztasTetel(lista):
    print()
    index = 0
    for i in range (len(lista)):
        if lista[i].ram > index:
            index = i

def megszamlalasTetel(lista):
    print("Hány windowos gepunk van?")
    db = 0
    for i in range(len(lista)):
        if lista[i].oprsz == "win":
            db += 1
    print(db)

def eldontesTetel(lista):
    van2 = False
    vizsgaltRam = 16
    for i in range(len(lista)):
        if lista[i].ram > vizsgaltRam and lista[i].oprsz == "win":
            van2 = True

    if van2 == True:
        print("Van")
    else:
        print("nincs")

