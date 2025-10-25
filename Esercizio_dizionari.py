def add_dictValue(dizionario_che_riceve:dict, dizionario_da_inserire:dict, chiave:str):
    """
    Aggiunge i valori di un dizionario all'interno di un altro dizionario tramite la chiave fornita.
    """
    for id, valore in dizionario_da_inserire.items():
        dizionario_che_riceve[id][chiave] = valore


# Dizionari di partenza
nomi = {
    "100": "Maglietta",
    "2500": "TV Samsung",
    "342": "Zaino",
    "578": "Smartphone",
    "12": "Cuffie Wireless"
}

categorie = {
    "100": "Abbigliamento",
    "2500": "Elettronica",
    "342": "Accessori",
    "12": "Elettronica",
    "999": "Alimentari"  # ID non presente negli altri dizionari
}

prezzi = {
    "100": 19.99,
    "2500": 899.99,
    "342": 49.90,
    "578": 599.00,
    "777": 1.99  # ID non presente negli altri dizionari
}

quantita = {
    "100": 50,
    "2500": 15,
    "342": 30,
    "12": 25,
    "578": 40
}

fornitori = {
    "100": "Fornitore A",
    "342": "Fornitore B",
    "578": "Fornitore C",
    "999": "Fornitore D"  # ID presente solo in categorie e qui
}

{"__id__": {"__nome_dizionario__": "__valore_dizionario__" }  }

#lista_dizionari = [nomi, categorie, prezzi, quantita, fornitori]

prodotti = {}
ids = set(list(nomi.keys()) + list(categorie.keys()) + list(prezzi.keys()) + list(quantita.keys()) + list(fornitori.keys()))

prodotti = {}
for id in ids:
    prodotti[id] = {}

for k, v in {"Nome": nomi, "Categorie": categorie, "Prezzi": prezzi, "Quantita": quantita, "Fornitori": fornitori}.items():
    add_dictValue(prodotti, v, k)

print(prodotti)
