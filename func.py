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


def boss_scielto_func():
    boss_scelto = random.choice(lista_boss)
    return boss_scelto


def genera_boss():
    boss_scelto = boss_scielto_func()
    nome_boss = boss_scelto[0]
    ascii_boss = boss_scelto[1]
    vita_boss = boss_scelto[2]
    danno_base = boss_scelto[3]
    danno_critico_aumento = boss_scelto[4]
    loot_boss = random.choice(boss_scelto[5])
    return nome_boss, ascii_boss, vita_boss, danno_base, danno_critico_aumento, loot_boss


def calcolo_danno_boss(danno_base, critico_boss):
    danno_finale = random.randint(danno_base, critico_boss)
    return danno_finale

def calcolo_danno_avventuriero(danno_base, critico_avventuriero):
    danno_finale = random.randint(danno_base, critico_avventuriero)
    return danno_finale

def esplora():
    global INVENTARIO, SOLDI
    nome_mostro, ascii_mostro, vita_mostro, danno_mostro, danno_critico_aumento = genera_mostro()
    print("Esplorando la torre...")
    time.sleep(1)
    OGGETTO = random.choice(["pozione di cura", "spada di legno", "spada di pietra", "5 monete" ,"nulla"])
    
    if nome_mostro == "NULLA" and OGGETTO == "nulla":
        print("Non hai incontrato nessun mostro e non hai trovato nulla.")
    elif nome_mostro == "NULLA":
        print(f"Non hai incontrato nessun mostro ma hai trovato {OGGETTO}.")
        if OGGETTO == "5 monete":
            env.SOLDI += 5
        else:
            INVENTARIO.append(OGGETTO)
    elif OGGETTO == "nulla":
        print(f"Hai incontrato un {nome_mostro} ma non hai trovato nulla.")
        battaglia_mostro(nome_mostro, ascii_mostro, vita_mostro, danno_mostro, danno_critico_aumento)
    else:
        print(f"Hai incontrato un {nome_mostro} e hai trovato {OGGETTO}.")
        if OGGETTO == "5 monete":
            SOLDI += 5
        else:
            INVENTARIO.append(OGGETTO)
        battaglia_mostro(nome_mostro, ascii_mostro, vita_mostro, danno_mostro, danno_critico_aumento)
    
    return env.HP, env.DANNO, env.INVENTARIO


def battaglia_mostro(nome_mostro, ascii_mostro, vita_mostro, danno_mostro, danno_critico_aumento):
    global HP, DANNO
    print(ascii_mostro)
    print(f"Il {nome_mostro} ha env.HP: {vita_mostro}.")

    while vita_mostro > 0:
        azione = input("Cosa vuoi fare? Attacca | Inventario: ").lower()
        
        if azione not in ["attacca", "inventario"]:
            print("Azione non valida. Riprova.")
            
        elif azione == "attacca":
            danno_subito = calcolo_danno_mostro(danno_mostro, danno_critico_aumento)
            danno_finale = calcolo_danno_avventuriero(DANNO, CRITICO)
            vita_mostro -= danno_finale
            print(f"Hai inflitto {danno_finale} di danno al {nome_mostro}, ora ha {vita_mostro} {ROSSO}HP{RESET}.")
            
            env.HP -= danno_subito
            print(f"Il {nome_mostro} ti ha inflitto {danno_subito} di danno, ora hai {env.HP} {VERDE}HP{RESET}.")
            
            if vita_mostro <= 0:
                print(f"Hai sconfitto il {nome_mostro}!")
                break
            elif env.HP <= 0:
                print(f"{ROSSO}Sei stato sconfitto. Game Over.{RESET}")
                exit()
                
        elif azione == "inventario":
            inventario()
            

            
        
    return env.HP, env.DANNO, env.INVENTARIO 



def battaglia_boss():
    global HP, DANNO
    nome_boss, ascii_boss, vita_boss, danno_boss, danno_critico_aumento, loot_boss = genera_boss()
    print(ascii_boss)
    print(f"Il {nome_boss} ha HP: {vita_boss}.")

    while vita_boss > 0:
        azione = input("Cosa vuoi fare? Attacca | Inventario: ").lower()
        
        if azione not in ["attacca", "inventario"]:
            print("Azione non valida. Riprova.")
            
        elif azione == "attacca":
            danno_subito = calcolo_danno_boss(danno_boss, danno_critico_aumento)
            danno_finale = calcolo_danno_avventuriero(DANNO, CRITICO)
            vita_boss -= danno_finale
            print(f"Hai inflitto {danno_finale} di danno al {nome_boss}, ora ha {vita_boss} {ROSSO}HP{RESET}.")
            
            env.HP -= danno_subito
            print(f"Il {nome_boss} ti ha inflitto {danno_subito} di danno, ora hai {env.HP} {VERDE}HP{RESET}.")
            
            if vita_boss <= 0:
                print(f"Hai sconfitto il {nome_boss}!")
                INVENTARIO.append(loot_boss)
                print(f"Hai ottenuto {loot_boss}!!")
                break
            elif env.HP <= 0:
                print(f"{ROSSO}Sei stato sconfitto. Game Over.{RESET}")
                exit()
                
        elif azione == "inventario":
            inventario()
            

            
        
    return env.HP, DANNO, INVENTARIO 



def inventario():
    global INVENTARIO, HP, DIFESA, DANNO, CRITICO
    print("Il tuo inventario contiene:")
    n = 0
    for oggetto in INVENTARIO:
        print(f"{n} - {oggetto}")
        n += 1
    
    while True:
        chiusura = input("Digita 'esci' per chiudere l'inventario o un numero per usare un oggetto: ").lower()
        if chiusura == "esci":
            return
        elif chiusura.isdigit() and int(chiusura) < len(INVENTARIO):
            oggetto_scelto = INVENTARIO[int(chiusura)].lower()
            if oggetto_scelto == "pozione di cura":
                env.HP += 50
                print(f"Hai usato una pozione di cura hai recuperato 50HP, {VERDE}HP: {env.HP}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "panacea abissale":
                env.HP += 150
                print(f"Hai usato una panacea abissale hai recuperato 150HP, {VERDE}HP: {env.HP}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "spada ancestrale":
                env.DANNO += 15
                print(f"Hai usato la spada ancestrale, il tuo attacco è aumentato di 15, {ROSSO}DANNO: {env.DANNO}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "patata cotta":
                env.HP += 20
                print(f"Hai usato la patata cotta, hai recuperato 20HP, {VERDE}HP: {env.HP}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "orecchio di pipistrello":
                env.DIFESA += 3
                print(f"Hai usato l'orecchio di pipistrello, e la tua difesa è aumentata di 3, {GIALLO}DIFESA: {env.DIFESA}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "cristallo di ametista":
                env.DANNO_CRITICO += 5
                print(f"Hai usato il cristallo di ametista, il tuo danno critico è aumentato di 5, {VIOLA}danno critico: {env.CRITICO}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "dente di vipera":
                env.DANNO_CRITICO += 10
                print(f"Hai usato il dente di vipera, il tuo danno critico è aumentato di 10, {VIOLA}danno critico: {env.CRITICO}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "spada di legno":
                env.DANNO += 2
                print(f"Hai usato la spada di legno, il tuo attacco è aumentato di 2, {ROSSO}DANNO: {env.DANNO}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "spada di pietra":
                env.DANNO += 3
                print(f"Hai usato la spada di pietra, il tuo attacco è aumentato di 3, {ROSSO}DANNO: {env.DANNO}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "occhio degli inferi":
                env.HP += 100
                env.DANNO += 20
                env.DIFESA += 5
                print(f"Hai usato l'occhio degli inferi {VERDE}+100 HP: {env.HP}{RESET} | {ROSSO}+20 DANNO: {env.DANNO}{RESET} | {GIALLO}+5 DIFESA: {env.DIFESA}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "corno del diavolo":
                env.HP += 50
                env.DANNO += 10
                env.DIFESA += 3
                print(f"Hai usato il corno del diavolo {VERDE}+50 HP: {env.HP}{RESET} | {ROSSO}+10 DANNO: {env.DANNO}{RESET} | {GIALLO}+3 DIFESA: {env.DIFESA}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
            elif oggetto_scelto == "scettro degli inferi":
                env.DANNO += 30
                print(f"Hai usato lo scettro degli inferi {ROSSO}+30 DANNO: {env.DANNO}{RESET}")
                INVENTARIO.remove(oggetto_scelto)
                break
        else:
            print("Scelta non valida. Riprova.")

    return env.HP, INVENTARIO, env.DIFESA, env.DANNO, env.CRITICO, env.DANNO_CRITICO

        








def negozio():
    global MARKETPLACE,SOLDI, INVENTARIO
    print(f"gli oggetti momentanemente presenti nel negozio sono:")
    n1 = random.choice(MARKETPLACE)
    n2 = random.choice(MARKETPLACE)
    n3 = random.choice(MARKETPLACE)
    n4 = random.choice(MARKETPLACE)
    n5 = random.choice(MARKETPLACE)
    print(f"1 {n1[0]}: {n1[1]} soldi")
    print(f"2 {n2[0]}: {n2[1]} soldi")
    print(f"3 {n3[0]}: {n3[1]} soldi")
    print(f"4 {n4[0]}: {n4[1]} soldi")
    print(f"5 {n5[0]}: {n5[1]} soldi")
    scielta = input("Cosa vuoi comprare: ")
    if scielta not in ["1", "2", "3", "4", "5"]:
        print("Scelta non valida. Riprova.")
    else:
        scielta = int(scielta)
        if scielta == 1:
            if SOLDI < n1[1]:
                print("Non hai abbastanza soldi per comprare questo oggetto.")
            else:
                INVENTARIO.append(n1[0])
                env.SOLDI -= n1[1]
                print(f"Hai comprato {n1[0]}")
        elif scielta == 2:
            if SOLDI < n2[1]:
                print("Non hai abbastanza soldi per comprare questo oggetto.")
            else:
                INVENTARIO.append(n2[0])
                env.SOLDI -= n2[1]
                print(f"Hai comprato {n2[0]}")
        elif scielta == 3:
            if SOLDI < n3[1]:
                print("Non hai abbastanza soldi per comprare questo oggetto.")
            else:
                INVENTARIO .append(n3[0])
                env.SOLDI -= n3[1]
                print(f"Hai comprato {n3[0]}")
        elif scielta == 4:
            if SOLDI < n4[1]:
                print("Non hai abbastanza soldi per comprare questo oggetto.")
            else:
                INVENTARIO.append(n4[0])
                env.SOLDI -= n4[1]
                print(f"Hai comprato {n4[0]}")
        elif scielta == 5:
            if SOLDI < n5[1]:
                print("Non hai abbastanza soldi per comprare questo oggetto.")
            else:
                INVENTARIO.append(n5[0])
                env.SOLDI -= n5[1]
                print(f"Hai comprato {n5[0]}")
