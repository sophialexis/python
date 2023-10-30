from random import randrange
import pickle

try:
    with open('esko.pickle', 'rb') as fichye_db:
        esko = pickle.load(fichye_db)
except (FileNotFoundError, EOFError):
    esko = {}

while True:
    epsedo = input("Antre non w : ")
    epsedo = epsedo.lower()
    print(f"Bonjou, {epsedo} ")
    while ' ' in epsedo:
        epsedo = input("Antre non an anko pa dwe gen espas : ")
    with open('esko.pickle', 'wb') as fichye_db:
        pickle.dump(esko, fichye_db)

    if epsedo in esko:
        sko = esko[epsedo]
    else:
        sko = 0

    nonb_odinate = randrange(0, 4)
    chans = 5
    sko += chans * 30
    n_sko = sko
    print("Ou gen 5 chans pou jwe")

    esko[epsedo] = n_sko
    with open('esko.pickle', 'wb') as fichye_db:
        pickle.dump(esko, fichye_db)

    while chans > 0:
        try:
            Nonb_chwazi = int(input(f"Chans ou rete : {chans}. Chwazi yon nonb ant 0 ak 100 : "))

            if 0 <= Nonb_chwazi < 4:
                if Nonb_chwazi < nonb_odinate:
                    print("Nonb odinate a pi gwo.")
                elif Nonb_chwazi > nonb_odinate:
                    print("Nonb odinate a pi piti.")
                else:
                    print("Bravo")
                    break
            else:
                print("Chwazi yon nonb ant 0 ak 36.")
                continue

            chans -= 1
            sko -= 30
        except ValueError:
            print("nonb ou a pa bon.")

    if chans == 0:
        print(f"ou pedi Ou pa gen chans anko. nonb odinate a se : {nonb_odinate}")
    else:
        print("Félisitasyon ou genyen.")

    esko[epsedo] = sko
    j = input("jwe anko? (O/N)")
    if j.lower() != 'o':
        break

for jwe, j_sko in esko.items():
    print(f"{jwe}: {j_sko}")

    if input("Pese 'k' pou kanpe jwè a: ").lower() == 'k':
        break

for epsedo, sko in esko.items():
    print(f"Sko w se:  : {sko}")
print("Mèsi pou jwe!")
