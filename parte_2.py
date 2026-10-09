
def visualizza_contatti(lista_nomi, lista_num_telefono):
    
    if(len(lista_nomi) == 0):
        print("La rubrica è vuota!")
    else:
        
        print("I contatti presenti in rubrica sono i seguenti: ")
    
        for i in range(len(lista_nomi)):
        
            print("Nome: ", lista_nomi[i], "Numero di telefono: ", lista_num_telefono[i] )
    

def cerca_contatto(lista_nomi, lista_num_telefono):
    
    nome = input("Inserisci il nome della persona da cercare: ")
    
    if(len(lista_nomi == 0)):
        print("La rubrica è vuota")
    else: 
        for i in range(len(lista_nomi)):
            if(lista_nomi[i] == nome):
                print("Nome trovato in rubrica! ")
                print("Il numero di telefono della persona cercata è: ", lista_num_telefono[i])
                break
            print("Nome non trovato!")
            
    
    