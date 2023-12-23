# MODULES

# import math
from math import pi

import sys
import random as rdm
from enum import Enum

# print(math.pi) => import math
print(pi)

# rdm.choice("123")

for item in dir(rdm):
  print(item)

print(__name__)

## PARA IMPORTAR O MODULO DE OUTRO ARQUIVO É NECESSÁRIO QUE OS DOIS ESTEJAM NA MESMA PASTA E O MODULO IMPORTADO NÃO PODE COMEÇAR COM NÚMERO OU CARAC ESPECIAIS. 
from rpsV7_18 import rock_paper_scissors

rock_paper_scissors()