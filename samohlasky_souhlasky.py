veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
samohlasky = "aeiouáéíóú"
souhlasky = "bcčdďfghjklmnňprřsštťvzžcdž"
vysledek = {"souhlasky": 0, "samohlasky": 0}

# v reseni je sice podminka if not pismeno.isalpha() a nasleduje continue, ale tady je to zbytecne
for znak in veta:
    if znak.lower() in souhlasky:
        vysledek["souhlasky"] += 1
    elif znak.lower() in samohlasky:
        vysledek["samohlasky"] +=1
    
print(f"Počet souhlásek: {vysledek["souhlasky"]} | Počet samohlásek: {vysledek["samohlasky"]}")
