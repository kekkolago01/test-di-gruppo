# ==========================================
# STRUTTURA DATI CONDIVISA
# ==========================================
# Usiamo una lista di liste per salvare i contatti [nome, cognome, numero]
rubrica = []

# ==========================================
# PARTE 1: Persona 1 (Aggiunta e gestione)
# ==========================================
def aggiungi_contatto():
    print("\n--- AGGIUNGI CONTATTO ---")
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    numero = input("Inserisci il numero di telefono: ")
    
    # Controllo validità dell'input
    if nome == "" or cognome == "" or numero == "":
        print("Errore: tutti i campi sono obbligatori!")
        return

    # Controllo duplicati del numero di telefono usando un ciclo for
    for contatto in rubrica:
        if contatto[2] == numero:
            print("Errore: Questo numero di telefono è già salvato!")
            return

    # Inserimento del contatto come sotto-lista [nome, cognome, numero]
    nuovo_contatto = [nome, cognome, numero]
    rubrica.append(nuovo_contatto)
    print(f"Contatto {nome} {cognome} aggiunto con successo!")


# ==========================================
# PARTE 2: Persona 2 (Visualizzazione e ricerca)
# ==========================================
def visualizza_contatti():
    print("\n--- LISTA CONTATTI ---")
    if len(rubrica) == 0:
        print("La rubrica è vuota.")
    else:
        for i in range(len(rubrica)):
            contatto = rubrica[i]
            print(f"{i + 1}. Nome: {contatto[0]} | Cognome: {contatto[1]} | Tel: {contatto[2]}")

def cerca_contatto():
    print("\n--- CERCA CONTATTO ---")
    if len(rubrica) == 0:
        print("La rubrica è vuota.")
        return

    chiave = input("Inserisci il nome o il cognome da cercare: ").lower()
    trovato = False

    for contatto in rubrica:
        # Confronto convertendo in minuscolo per evitare errori di maiuscole/minuscole
        if contatto[0].lower() == chiave or contatto[1].lower() == chiave:
            print(f"Trovato -> Nome: {contatto[0]} | Cognome: {contatto[1]} | Tel: {contatto[2]}")
            trovato = True

    if not trovato:
        print("Nessun contatto trovato con questo nome o cognome.")


# ==========================================
# PARTE 3: Persona 3 (Menu ed Eliminazione)
# ==========================================
def elimina_contatto():
    print("\n--- ELIMINA CONTATTO ---")
    if len(rubrica) == 0:
        print("La rubrica è vuota, non ci sono contatti da eliminare.")
        return

    # Visualizza i contatti con un indice per rendere facile la scelta
    visualizza_contatti()
    
    scelta = input("\nInserisci il numero del contatto da eliminare (o '0' per annullare): ")
    
    if scelta == "0":
        print("Operazione annullata.")
        return

    # Verifichiamo che l'utente abbia inserito un numero intero valido
    if scelta.isdigit():
        indice = int(scelta) - 1  # Convertiamo in indice partendo da 0
        
        if 0 <= indice < len(rubrica):
            contatto_rimosso = rubrica.pop(indice)
            print(f"Contatto {contatto_rimosso[0]} {contatto_rimosso[1]} eliminato con successo!")
        else:
            print("Numero non valido: il contatto non esiste.")
    else:
        print("Inserisci un numero intero valido.")


def menu_principale():
    while True:
        print("\n==============================")
        print("      RUBRICA TELEFONICA      ")
        print("==============================")
        print("1. Aggiungi contatto")
        print("2. Visualizza tutti i contatti")
        print("3. Cerca contatto")
        print("4. Elimina contatto")
        print("5. Esci")
        print("==============================")
        
        scelta = input("Scegli un'opzione (1-5): ")

        if scelta == "1":
            aggiungi_contatto()
        elif scelta == "2":
            visualizza_contatti()
        elif scelta == "3":
            cerca_contatto()
        elif scelta == "4":
            elimina_contatto()
        elif scelta == "5":
            print("\nGrazie per aver usato la Rubrica Telefonic. Arrivederci!")
            break
        else:
            print("\nOpzione non valida! Inserisci un numero da 1 a 5.")

# Avvio del programma
menu_principale()