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
    danno_critico_aumento = mostro_scelto[4]
    return nome_mostro, ascii_mostro, vita_mostro, danno_base, danno_critico_aumento


def calcolo_danno_mostro(danno_base, critico_mostro):
    danno_finale = random.randint(danno_base, critico_mostro)
    return danno_finale


def esplora():
    global INVENTARIO
    nome_mostro, ascii_mostro, vita_mostro, danno_mostro, danno_critico_aumento = genera_mostro()
    print("Esplorando la torre...")
    time.sleep(1)
    OGGETTO = random.choice(["pozione di cura", "spada di legno", "spada di pietra", "5 monete" ,"nulla"])
    
    if nome_mostro == "NULLA" and OGGETTO == "nulla":
        print("Non hai incontrato nessun mostro e non hai trovato nulla.")
    elif nome_mostro == "NULLA":
        print(f"Non hai incontrato nessun mostro ma hai trovato {OGGETTO}.")
        if OGGETTO == "5 monete":
            SOLDI+5
        else:
            INVENTARIO.append(OGGETTO)
    elif OGGETTO == "nulla":
        print(f"Hai incontrato un {nome_mostro} ma non hai trovato nulla.")
        battaglia_mostro(nome_mostro, ascii_mostro, vita_mostro, danno_mostro, danno_critico_aumento)
    else:
        print(f"Hai incontrato un {nome_mostro} e hai trovato {OGGETTO}.")
        INVENTARIO.append(OGGETTO)
        battaglia_mostro(nome_mostro, ascii_mostro, vita_mostro, danno_mostro, danno_critico_aumento)
    
    return HP, DANNO, INVENTARIO 


def battaglia_mostro(nome_mostro, ascii_mostro, vita_mostro, danno_mostro, danno_critico_aumento):
    global HP, DANNO
    print(ascii_mostro)
    print(f"Il {nome_mostro} ha HP: {vita_mostro}.")

    while vita_mostro > 0:
        azione = input("Cosa vuoi fare? Attacca | Inventario | Cura: ").lower()
        
        if azione not in ["attacca", "inventario", "cura"]:
            print("Azione non valida. Riprova.")
            
        elif azione == "attacca":
            danno_subito = calcolo_danno_mostro(danno_mostro, danno_critico_aumento)
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
            
        elif azione == "cura":
            cura()
            
        
    return HP, DANNO, INVENTARIO 


def inventario():
    global INVENTARIO
    
    
    


def cura():
    global HP
    if "pozione di cura" in INVENTARIO:
        HP += 50
        INVENTARIO.remove("pozione di cura")
        print(f"Hai usato una pozione di cura hai recuperato 50HP, HP: {HP}")
    else:
        print("Non hai pozioni di cura nel tuo inventario.")





def negozio():
    global MARKETPLACE
    STOCK = random.choice(MARKETPLACE)
    oggetto = STOCK[0]
    prezzo = STOCK[1]
    print(f"gli oggetti momentanemente presenti nel negozio sono:")
    n = 0
    for i in STOCK:
        print(f"{n}){i}")
        n+=1
    
    scielta = input("Cosa vuoi comprare: ")

