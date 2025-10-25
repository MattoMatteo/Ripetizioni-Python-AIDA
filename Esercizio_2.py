# Impostiamo i dati "costanti" del software: Dati utenti registrati
user1 = "Giovanna"
psw1 = "Master!"
bilancio1 = 2000

user2 = "Lorenzo"
psw2 = "AIDA2025"
bilancio2 = 120

#Chiediamo username e password all'utente
user_input = input('nome utente:')
psw_input = input('password:')

# In base all'utente selezionato ci segnamo in una nuova variabile "bilancio_corrente"
# il suo bilancio.
# In caso di errore durante il login usiamo impostiamo bilancio_corrente a "None" per segnalarci
# che l'operazione non è andata a buon fine e gestiamo i 3 casi:

if user_input == user1 and psw_input == psw1: # Login come user1
    bilancio_corrente = bilancio1
elif user_input == user2 and psw_input == psw2: # Login come user2
    bilancio_corrente = bilancio2
else:                                           # Credenziali errate
    print("Nome utente e/o password errati.")
    bilancio_corrente = None

# Controlliamo che le credenziali siano stato inserite correttamente e procediamo con il programma
if bilancio_corrente is not None: #Oppure: if bilancio_corrente != None:
    print("Benvenuto/a " + user_input + "!")
    user_choice = input("Deposito o Prelievo? (P/D)")

    # Richiesto prelievo
    if user_choice == "P":
        prelievo = int(input("Quanto vuoi prelevare?"))
        # Controlliamo che ci siano abbastanza soldi sul conto.
        if bilancio_corrente >= prelievo:
            # Facciamo il calcolo del nuovo bilancio e segnamo che dovrà essere effettuato
            # l'aggiornamento del saldo
            bilancio_corrente =bilancio_corrente - prelievo
            update_bilancio = True
        # Se non ci sono, segnaliamo e impostiamo la variabile di controllo finale a False
        # in questo modo non verrà aggiornato il saldo dell'utente e il programma terminerà
        else:
            print("Disponibilità non sufficiente.")
            update_bilancio = False

    # Richiesto Deposito
    elif user_choice == "D":
        deposito = int(input("Quanto vuoi depositare? "))
        # Il deposito non richiede particolari controlli.
        # Effettuiamo le operazioni in modo simile al prelievo.
        bilancio_corrente = bilancio_corrente + deposito
        update_bilancio = True
    
    # Bisogna aggiornare la variabile corretta di bilancio dell'utente.
    # Bisogna farlo solo se l'operazione effettuata è andata a buon fine.
    # Usiamo la variabile booleana "update_bilancio" per verificarlo
    if update_bilancio == True:
        print("Operazione completata!")
        print("Il tuo nuovo saldo è: ", bilancio_corrente)
        if user_input == user1:
            bilancio1 = bilancio_corrente
        else:
            bilancio2 = bilancio_corrente
    else:
        print("Operazione non riconosciuta. Chiusura programma.")

else: # Caso in cui le credenziali sono errate
    print("Nome utente e/o password errati.")

    

