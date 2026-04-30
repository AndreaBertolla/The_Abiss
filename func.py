import time , random , env , os
from env import *

def mostro_scielto_func():
    mostro_scelto = random.choice(lista_mostri)
    return mostro_scelto


def genera_mostro():
    mostro_scelto = mostro_scielto_func()
    nome_mostro = mostro_scelto[0]
    ascii_mostro = mostro_scelto[1]
    vita_mostro = mostro_scelto[2]
    danno_base = mostro_scelto[3]
    return nome_mostro, ascii_mostro, vita_mostro, danno_base


def calcolo_danno_mostro():
    mostro_scelto = mostro_scielto_func()
    danno_base = mostro_scelto[3]
    critico_mostro = mostro_scelto[4]
    danno_finale = random.randint(danno_base, critico_mostro)
    return danno_finale


def esplora():
    nome_mostro, ascii_mostro, vita_mostro, danno_mostro = genera_mostro()
    print("Esplorando la torre...")
    time.sleep(1)
    OGGETTO = random.choice(["pozione di cura", "spada di legno", "spada di pietra", "5 monete" ,"nulla"])
    
    if nome_mostro == "NULLA" and OGGETTO == "nulla":
        print("Non hai incontrato nessun mostro e non hai trovato nulla.")
    elif nome_mostro == "NULLA":
        print(f"Non hai incontrato nessun mostro ma hai trovato {OGGETTO}.")
    elif OGGETTO == "nulla":
        print(f"Hai incontrato un {nome_mostro} ma non hai trovato nulla.")
        battaglia_mostro(nome_mostro, ascii_mostro, vita_mostro, danno_mostro)
    else:
        print(f"Hai incontrato un {nome_mostro} e hai trovato {OGGETTO}.")
        battaglia_mostro(nome_mostro, ascii_mostro, vita_mostro, danno_mostro)


def battaglia_mostro(nome_mostro, ascii_mostro, vita_mostro, danno_mostro):
    global HP, DANNO
    print(ascii_mostro)
    print(f"Il {nome_mostro} ha HP: {vita_mostro}.")

    while vita_mostro > 0:
        azione = input("Cosa vuoi fare? Attacca | Inventario: ").lower()
        
        if azione not in ["attacca", "inventario"]:
            print("Azione non valida. Riprova.")
            
        elif azione == "attacca":
            danno_subito = calcolo_danno_mostro()
            vita_mostro -= DANNO
            print(f"Hai inflitto {DANNO} di danno al {nome_mostro}, ora ha {vita_mostro} HP.")
            
            HP -= danno_subito
            print(f"Il {nome_mostro} ti ha inflitto {danno_subito} di danno, ora hai {HP} HP.")
            
            if vita_mostro <= 0:
                print(f"Hai sconfitto il {nome_mostro}!")
                break
            elif HP <= 0:
                print(f"{ROSSO}Sei stato sconfitto. Game Over.{RESET}")
                exit()
                
        elif azione == "inventario":
            inventario()