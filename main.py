import env, random, time, os, func
from env import *
from func import *

gioco = True

print(" BENVENUTO SU NOME ")
print("caricamento")
time.sleep(1)
print("caricamento.")
time.sleep(1)
print("caricamento..")
time.sleep(1)
print("caricamento...")
time.sleep(0.5)
nome = input("Benvenuto guerriero nella torre dicci come ti chiami: ")
os.system("cls")

while gioco:
    if gioco == True:
        print(f"{VERDE}HP: {HP}{RESET} | {GIALLO} DIFESA: {DIFESA}{RESET} | {ROSSO} ATTACCO: {danno_base}{RESET} | {GIALLO} SOLDI: {SOLDI}{RESET}")
        while True:
            azione = input("Cosa vuoi fare? Esplora | Inventario: ").lower()
            if azione not in ["esplora", "inventario"]:
                print("Azione non valida. Riprova.")
            else:
                if azione == "esplora":
                    esplora()
                elif azione == "inventario":
                    inventario()
