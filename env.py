import random




# CARATTERISTICHE EROE
DANNO_CRITICO = 8
PIANO_ATTUALE = 0
ULTIMO_PIANO = 100
HP = 100
DANNO = 10
CRITICO = DANNO + DANNO_CRITICO
DIFESA = 0
SOLDI = 1000
INVENTARIO = ["pozione di cura","scettro degli inferi","corno del diavolo", "occhio degli inferi"]





# COLORI
ROSSO = "\033[91m"
VERDE = "\033[92m"
GIALLO = "\033[93m"
BLU = "\033[94m"
VIOLA = "\033[95m"
CIANO = "\033[96m"
RESET = "\033[0m"


#NEGOZIO
MARKETPLACE = [
  ("pozione di cura", 5),
  ("panacea abissale", 15),
  ("spada ancestrale", 35),
  ("patata cotta", 3),
  ("orecchio di pipistrello", 16),
  ("cristallo di ametista", 17),
  ("dente di vipera", 30)
]










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
    ("Cavaliere", cavaliere, 42, 1, 13),
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
    ("Satana", satana, 501, 40, 60, ["scettro degli inferi", "corno del diavolo", "occhio degli inferi"])

]

#promemoria signiore delli specchi(te stesso)

