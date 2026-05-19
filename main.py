import env, random, time, os, func
from env import *
from func import *

gioco = True

print(" BENVENUTO NELL'ABISSO ")
print("VERSIONE 0.0.1")
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
                print(f"{VERDE}HP: {env.HP}{RESET} | {GIALLO} DIFESA: {env.DIFESA}{RESET} | {ROSSO} ATTACCO: {env.DANNO}{RESET} | {GIALLO} SOLDI: {env.SOLDI}{RESET} | {CIANO} PIANO: {PIANO_ATTUALE}/{ULTIMO_PIANO} {RESET}")
                azione = input(f"Cosa vuoi fare {nome}? Esplora | Inventario: ").lower()
                if azione not in ["esplora", "inventario"]:
                    print("Azione non valida. Riprova.")
                else:
                    if azione == "esplora":
                        if int(PIANO_ATTUALE)%11 == 0 and int(PIANO_ATTUALE)>0:
                            battaglia_boss()
                        else:
                            esplora()


                        PIANO_ATTUALE += 1
                    elif azione == "inventario":
                        inventario()



# COSE DA FARE 
# SHOP
# GENERAZIONE BOSS OGNI 11 o ogni 10 lvl 
# UTILIZZO OGGETTI
# UTILIZZO CURE DIVERSE