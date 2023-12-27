import os
# r = Read      Ler
# a = Append    Anexar
# w = Write     Escrever
# x = Create    Criar

###################################################
# Read(Ler) - error if it doesn't exist

# f = open("names.txt", "rt") => Caso precise especificar que irá ler 'r' um texto 't'.
f = open("names.txt") # => por padrão vem como read "r"
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
  print(line)
  
f.close()

# try:
  # f = open("name_list.txt")
  # print(f.read())
# except:
  # print("The file you want to read doesn't exist")
# finally:
  # f.close()

###################################################
# Append(Anexar) - creates the file if it doesn't exist

f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt") # => por padrão vem read "r".
print(f.read())
f.close()

###################################################
# Write/overwrite (Escrever/sobrescrever)

f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new dile => Duas maneiras de criar um novo arquivo

# Opens a file for writing, creates the file if it does not exist.
# Abrir um arquivo para escrever, isso também cria o arquivo se ele não existir.
f = open("name_list.txt", "w")
f.close()

# Creates the specifed file, but returns an error if the file exists.
# Criar um arquivo especificado, mas retorna um erro se o arquivo existir.
if not os.path.exists("dave.txt"):
  f = open("dave.txt", "x")
  f.close()

# Delete a file
## avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
  os.remove("dave.txt")
else:
  print("The file you wish to delete does not exist")

with open("more_names.txt") as f:
  content = f.read()

with open("names.txt", "w") as f:
  f.write(content)