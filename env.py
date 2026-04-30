import random


# VARIABILI UTILI
danno_critico_aumento = 5
danno_base = 4
danno = random.randint(danno_base, danno_critico_aumento)


# CARATTERISTICHE EROE
PIANI = 100
HP = 100
DANNO = 4
DIFESA = 0
DANNO = danno
SOLDI = 0


# COLORI
ROSSO = "\033[91m"
VERDE = "\033[92m"
GIALLO = "\033[93m"
BLU = "\033[94m"
VIOLA = "\033[95m"
CIANO = "\033[96m"
RESET = "\033[0m"

#NEMICI NORMALI
ragno =r"""                                  
          /---.'.__             ____//
               '--.\           /.---'
          _______  \\         //
        /.------.\  \|      .'/  ______
       //  ___  \ \ ||/|\  //  _/_----.\__
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
         //   \'. | \'.|.'/ /_/ /  \\
        //     \ \_\/" ' ~\-'.-'    \\
       //       '-._| :H: |'-.__     \\
      //           (/'==='\)'-._\     ||
      ||                        \\    \|
      ||                         \\    '
      |/                          \\
                                   ||
                                   ||
                                   \\
                                    '
"""

strega =r"""(       "     )
                ( _  * * (     /      \    ___
                      "     "        _/ /
                     (   * )    ___/   |
                       )   "     _ o)'-./__
                      * _ )    (_, . $$$
                      (  )   __ __ 7_ $$$$
                       ( :  { _)  '---  $\
                  ______'___//__\   ____, \
                   )           ( \_/ _____\_
                 .'             \   \------''.
                 |='           '=|  |         )
                 |               |  |  .    _/
                  \    (. ) ,   /  /__I_____\
                   '._/_)_(\__.'   (__,(__,_]
                  @---()_.'---@"""

cavaliere =r""" 
 /\
 ||
 ||
 ||
 ||           {}
 ||          .--.
 ||         /.--.\
 ||         |====|
 ||         |`::`|
_||_    .-;`\..../`;_.-^-._
 /\\   /  |...::..|`   :   `|
 |:'\ |   /'''::''|   .:.   |
  \ /\;-,/\   ::  |..:::::..|
   \ <` >  >._::_.| ':::::' |
    `""`  /   ^^  |   ':'   |
          |       \    :    /
          |        \   :   / 
          |___/\___|`-.:.-`
           \_ || _/    `
           <_ >< _>
           |  ||  |
           |  ||  |
          _\.:||:./_
         /____/\____\
"""




lista_mostri = [
    ("Ragno", ragno, 21, 1, 7),
    ("Strega", strega, 55, 5, 11),
    ("Cavaliere", cavaliere, 42, 1, 16),
    ("NULLA", "NULLA", "NULLA", "NULLA", "NULLA")
]






#BOSS

satana = r"""               ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      \
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  \
            /   /     ||--+--|--+-/-|     \   \
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
"""





lista_boss = [
    ("Satana", satana, 501, random.randint(40,60), random.choice(["Sciettro degli inferi", "Corno del diavolo", "Occhio degli inferi"]))

]


boss_scelto = random.choice(lista_boss)

nome_boss = boss_scelto[0]
ascii_boss = boss_scelto[1]
vita_boss = boss_scelto[2]
attacco_boss = boss_scelto[3]
loot_boss = boss_scelto[4]


#promemoria signiore delli specchi(te stesso)