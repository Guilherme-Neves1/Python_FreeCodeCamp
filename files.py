# r = Read      Ler
# a = Append    Anexar
# w = Write     Escrever
# x = Create    Criar

# Read - error if it doesn't exist

# f = open("names.txt", "rt") => Caso precise especificar que irá ler 'r' um texto 't'.

f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
  print(line)
  
f.close()
