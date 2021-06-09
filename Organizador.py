import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os

path = "C:/Users/Flavio/Downloads"
Arq_Text = "C:/Users/Flavio/Downloads/Texto"
Arq_Music = "C:/Users/Flavio/Downloads/Musica"
Arq_foto = "C:/Users/Flavio/Downloads/Imagem"
Arq_zip = "C:/Users/Flavio/Downloads/Zip"

try:
    os.mkdir(Arq_Text)
    os.mkdir(Arq_Music)
    os.mkdir(Arq_foto)
    os.mkdir(Arq_zip)

except FileExistsError as e:
    print(f'Pasta {Arq_Text} já existe')
    print(f'Pasta {Arq_Music} já existe')    
    print(f'Pasta {Arq_foto} já existe')   
    print(f'Pasta {Arq_zip} já existe') 
                

def organizar():
    for root, dirs, files in os.walk(path):
        for file in files:
            caminho_antigo = os.path.join(root, file)
            caminho_txt = os.path.join(Arq_Text, file)
            caminho_music = os.path.join(Arq_Music, file)
            caminho_foto = os.path.join(Arq_foto, file)
            caminho_zip = os.path.join(Arq_zip, file)

            if '.TXT' in file:
                time.sleep(1)
                shutil.move(caminho_antigo, caminho_txt)
                print(f'Arquivo {file} movido com sucesso!')
                return
            
            elif '.doc' in file:
               shutil.move(caminho_antigo, caminho_txt)
               print(f'Arquivo {file} movido com sucesso!')    
               return       

            elif '.mp3' in file:
                shutil.move(caminho_antigo, caminho_music)
                print(f'Arquivo {file} movido com sucesso!')
                return

            elif '.zip' in file:
               shutil.move(caminho_antigo, caminho_zip)
               print(f'Arquivo {file} movido com sucesso!')    
               return

            elif '.rar' in file:
               shutil.move(caminho_antigo, caminho_zip)
               print(f'Arquivo {file} movido com sucesso!')    
               return   

            elif '.png' in file:
               shutil.move(caminho_antigo, caminho_foto)
               print(f'Arquivo {file} movido com sucesso!')    
               return           
            
            elif '.bmp' in file:
               shutil.move(caminho_antigo, caminho_foto)
               print(f'Arquivo {file} movido com sucesso!')    
               return  



def on_modified(event):
    print ("Modificado")    
    organizar()
    pass
def on_deleted(event):
    print("Deletado")
    pass
def on_created(event):
    print("Novo")
    pass

def on_moved(event):
    print("Movido")
    organizar()
    pass

if __name__ == "__main__":
    event_handler = FileSystemEventHandler()
    #Chamando as funções
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved


    
    observer = Observer()   
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print ("Monitorando")
        organizar()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Encerrando")
        observer.join()