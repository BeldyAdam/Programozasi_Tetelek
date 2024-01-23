from Szamitogep import Szamitogep

peldany1 = Szamitogep("win", 32)
peldany2 = Szamitogep("mac", 16)
peldany3 = Szamitogep("win", 16)

szamitogepek = []

szamitogepek.append(peldany1)
szamitogepek.append(peldany2)
szamitogepek.append(peldany3)

for i in range(len(szamitogepek)):
    oprsz = szamitogepek[i].oprsz
    ram = szamitogepek[i].ram
    print(f"{oprsz} ({ram})")

print("Átlag: ", end="")

gyujto = 0

for i in range(len(szamitogepek)):
    gyujto += szamitogepek[i].ram

print(round(gyujto/len(szamitogepek), 3))

print("Legtöbb ramot tartalmazó oprendszer: ", end="")

max_index = 0

for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > szamitogepek[max_index].ram:
        max_index = i

print(szamitogepek[max_index].oprsz)



lista = len(szamitogepek)
ker = szamitogepek[0]
i = 0
van = True
while i < lista and szamitogepek[i] != ker:
    i = i + 1
if i < lista:
    print("Van ilyen: ", szamitogepek[i].oprsz,szamitogepek[i].ram)
else:
    van = False

#masik megoldas

van2 = False
vizsgaltRam = 16
for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > vizsgaltRam and szamitogepek[i].oprsz == "win":
        van2 = True
#        print("Van", szamitogepek[i].oprsz, szamitogepek[i].ram)

if van2 == True:
    print("Van")
else:
    print("nincs")

#megszamlalas tetele
print("Hány windowos gepunk van?")
db = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].oprsz == "win":
        db +=1
print(db)


