#Come al solito chiediamo i dati input
#Usiamo il cast a int per i numeri
numero_1 = int(input("Inserire numero_1: "))
numero_2 = int(input("Inserire numero_2: "))
Messaggio = input("Inserire Messaggio: ")

# Usiamo gli operatori matematici con le parentesi per costruire la stringa
# (Messaggio + ", ") crea il messaggio con la virgola e lo spazio e poi usiamo
# la moltiplicazione per concatenare il numero di stringhe corrette
# calcoliamo anche il numero da moltiplicare usando l'operatore matematico + per sommare i numeri
risposta = (Messaggio + ", ") * (numero_1 + numero_2)
# per capirci, questo è il "passaggio intermedio":
# risposta = "Ciao, " * 5

print(risposta)