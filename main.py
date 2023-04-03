class Celula:

    def get_nume(self):
        raise NotImplementedError("Functie neimplementata!")

class FibraMusculara(Celula):

    def __init__(self,nume, masa):
        self.nume=nume
        self.masa_musculara=masa

    def get_nume(self):
        return self.nume

    def get_masa_musculara(self):
        return self.masa_musculara


class FibraNervoasa(Celula):

    def __init__(self, nume, lungime):
        self.nume = nume
        self.lungime = lungime

    def get_nume(self):
        return self.nume

    def get_lungime(self):
        return self.lungime

class MuschiGeneric:

    def __init__(self, fibre, nume, masa_musculara, scop):
        self.fibre=fibre
        self.nume=nume
        self.masa_musculara=masa_musculara
        self.scop=scop

    def get_nume(self):
        return self.nume

    def get_masa_musculara(self):
        return self.masa_musculara

    def get_scop(self):
        return self.scop


class TrunchiNervos:

    def __init__(self, nervi, nume, lungime, specializare):
        self.nervi=nervi
        self.nume=nume
        self.lungime=lungime
        self.specialziare=specializare

    def get_nume(self):
        return self.nume

    def get_lungime(self):
        return self.lungime

    def get_specializare(self):
        return self.specialziare

class Biceps(MuschiGeneric):

    def __init__(self, fibre, nume, masa_musculara, scop, brat):
        super().__init__(fibre, nume, masa_musculara, scop)
        self.brat=brat

    def get_brat(self):
        return self.brat

def masa_musculara_totala(list):
    sum=0
    for item in list:
        sum=sum+item.get_masa_musculara()
    return sum

def lungime_totala(list):
    sum=0
    for item in list:
        sum=sum+item.get_lungime()
    return sum

def functie_locomotorie(list):
    list2=[]
    for item in list:
        for scop in item.get_scop():
            if (scop=="locomotor"):
                list2.append(item)
    return list2
if __name__ == '__main__':
    fibram1 = FibraMusculara("nume_fibram1", 0.5)
    fibram2 = FibraMusculara("nume_fibram2", 0.6)
    fibram3 = FibraMusculara("nume_fibram3", 0.7)

    fibran1 = FibraNervoasa("nume_fibran1", 0.15)
    fibran2 = FibraNervoasa("nume_fibran2", 0.16)
    fibran3 = FibraNervoasa("nume_fibran3", 0.17)

    lista_fibrem = [fibram1, fibram2, fibram3]
    lista_fibren = [fibran1, fibran2, fibran3]

    triceps_stang = MuschiGeneric(lista_fibrem, "triceps stang", 0.44, ["locomotor", "relaxare"])
    triceps_drept = MuschiGeneric(lista_fibrem, "triceps drept", 0.45, ["locomotor", "relaxare"])
    gamba_stanga = MuschiGeneric(lista_fibrem, "gamba stanga", 0.6, ["locomotor", "incordare"])
    gamba_dreapta = MuschiGeneric(lista_fibrem, "gamba dreapta", 0.61, ["locomotor", "incordare"])
    stomac = MuschiGeneric(lista_fibrem, "stomac", 1, ["digestie"])

    emisfera_stanga = TrunchiNervos(lista_fibren, "emisfera stanga", 160, ["gandire"])
    emisfera_dreapta = TrunchiNervos(lista_fibren, "emisfera dreapta", 162, ["gandire"])
    maduva = TrunchiNervos(lista_fibren, "maduva", 200, ["celule stem"])

    biceps_stang = Biceps(lista_fibrem,"biceps stang", 2, ["locomotor", "incordare brat stang"], "stang")
    biceps_drept = Biceps(lista_fibrem, "biceps drept", 2, ["locomotor", "incordare brat drept"], "drept")

    sum=masa_musculara_totala([triceps_stang, triceps_drept, gamba_stanga, gamba_dreapta, stomac, biceps_stang, biceps_drept])
    print("Masa musculara totala: "+str(sum))

    sum=lungime_totala([emisfera_dreapta, emisfera_dreapta, maduva])
    print("Lungimea totala a axonilor: " + str(sum))

    list=functie_locomotorie([triceps_stang, triceps_drept, gamba_stanga, gamba_dreapta, stomac, biceps_stang, biceps_drept])
    print("Muschii care au ca scop functia locomotorie: ")
    for item in list:
        print(item.get_nume() + ": ")
        print(item.get_scop())