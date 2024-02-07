print("Organizador de arquivos e diretorios.")
#Passo 1: Blibiotecas necessárias, para manipulação e automação.
import os 
import shutil

#Passo 2: Definindo as Variaveis e criando as pastas.
#directory é o diretorio onde vc vai colocar todas as pastas que vão ser criadas
#Após isso é só definir as variaveis de pastas que vão ser criadas.
#Em seguida coloque tudo em uma lista e faça percorrer pela lista.
#Pra cada elemento dentro dela será criado uma pasta.

directory = "/Organizador/"
directorysearcher = "\Users\emanu\OneDrive\Documentos/"
#Coloque aqui o diretorio que quer analisar 

pdf_folder = "pdfs"
spreadsheet_folder = "planilhas"
image_folder = "imagens"
document_folder = "documentos"

directory_folders = [image_folder, document_folder, spreadsheet_folder, pdf_folder]

'''for dir in directory_folders:
    os.mkdir(directory+dir)
    print(directory+dir)'''

#Passo 3: Listar os arquivos no diretorio.
files = os.listdir(directorysearcher)
files

for file in files:
    if file.lower().endswith((".jpg",".jpeg",".png",".gif")):
        shutil.move(os.path.join(directorysearcher, file), os.path.join(directory, image_folder, file))
    elif file.lower().endswith((".doc", ".docx", ".txt")):
        shutil.move(os.path.join(directorysearcher, file), os.path.join(directory, document_folder, file))
    elif file.lower().endswith(".xlsx"):
        shutil.move(os.path.join(directorysearcher, file), os.path.join(directory, spreadsheet_folder, file))
    elif file.lower().endswith(".pdf"):
        shutil.move(os.path.join(directorysearcher,file), os.path.join(directory, pdf_folder, file))
#Aqui fizemos com que se o arquivo do diretorio analisado tiver a terminação em alguma dessas, ele irá mudar do diretorio em que está para o respectivo.

#Agora para renomear os arquivos de mesmo tipo, basta percorrer pelo diretorio que quer.
for file in os.listdir(os.path.join(directory, image_folder)):
    new_name = "imagem_" + file
#Coloque aqui o nome que quer dar para os arquivos de mesmo tipo.
    os.rename(os.path.join(directory, image_folder, file), os.path.join(directory, image_folder, new_name))
#Aqui o arquivo será renomeado.
