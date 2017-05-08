import random
vrednost = {
"Kamen" : 0,
"Skarje" : 1,
"List" : 2
}

matrika_igre = [
    [0,2,1],
    [1,0,2],
    [2,1,0]
  ]

def igra():
    
    x = input("Izberi! ")
    računalnik_izbira = random.random()
    if računalnik_izbira < 0.34:
        računalnik_izbira = vrednost["Skarje"]
    elif računalnik_izbira <= 0.67:
        računalnik_izbira = vrednost["Kamen"]
    else:
        računalnik_izbira = vrednost["List"]


    i = računalnik_izbira
    j = vrednost[x]

    if matrika_igre[i][j] == 0:
        return "Izenačeli ste, poskusite ponovno"
    if matrika_igre[i][j] ==  1:
        return "Čestitam, premagali ste računalnik, prosim nadaljujte"
    if matrika_igre[i][j] == 2:
        return "Izgubili ste, igre je konec"

#NEDELA
def Tocke_v_igri():
    vsota = 0
    for i in igra():
        vsota += 1
    return vsota
#NEDELA
def igra_v_neskoncnost():
    if igra() == "Izgubili ste, igre je konec":
        return Tocke_v_igri()
    else:
        igra()
