import env, random, time, os, func
from env import *
from func import *

gioco = True

print(" BENVENUTO NELL'ABISSO ")
print("caricamento")
time.sleep(1)
print("caricamento.")
time.sleep(1)
print("caricamento..")
time.sleep(1)
print("caricamento...")
time.sleep(0.5)
nome = input("Benvenuto guerriero nell'Abisso dicci come ti chiami: ")
os.system("cls")

while gioco:
    if gioco == True:
        while True:

            if int(PIANO_ATTUALE)%10 == 0 and int(PIANO_ATTUALE)>0:
                negozio()
                PIANO_ATTUALE+=1
            
            else:
                print(f"{VERDE}HP: {HP}{RESET} | {GIALLO} DIFESA: {DIFESA}{RESET} | {ROSSO} ATTACCO: {danno_base}{RESET} | {GIALLO} SOLDI: {SOLDI}{RESET} | {CIANO} PIANO: {PIANO_ATTUALE}/{ULTIMO_PIANO} {RESET}")
                azione = input(f"Cosa vuoi fare {nome}? Esplora | Inventario: ").lower()
                if azione not in ["esplora", "inventario"]:
                    print("Azione non valida. Riprova.")
                else:
                    if azione == "esplora":
                        PIANO_ATTUALE += 1
                        esplora()
                    elif azione == "inventario":
                        print(INVENTARIO)



# COSE DA FARE 
# SHOP
# GENERAZIONE BOSS OGNI 11 o ogni 10 lvl 
# UTILIZZO OGGETTI
# UTILIZZO CURE DIVERSE