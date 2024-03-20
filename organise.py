import os
import shutil

path="C:/Users/jo__a/Downloads/joana.jpeg"

root, extension = os.path.splitext("joana.jpeg")
print("Raiz do caminho: ", root) 
print("Extensão do caminho: " , extension) 

path2="C:/Users/jo__a/Downloads"
print("Antes de copiar o arquivo:") 
print(os.listdir(path2))

source="C:/Users/jo__a/Downloads/kakashi.jpeg"
dest=shutil.copy(source,"C:/Users/jo__a/Documents/aulas em grupo/python/c111 grupo/aula_111")

print("Após copiar o arquivo:")
print(os.listdir(path2))








