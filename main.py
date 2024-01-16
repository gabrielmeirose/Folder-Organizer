import os
from getpass import getuser
import shutil
import sys


USERNAME = getuser()


def path(folder):
    return f'/home/{USERNAME}/{folder}/'


def move_file(source, destination):

    # Simple function that moves a file at 'source' to a 'destination' folder

    try:
        shutil.move(source, destination)

    except FileNotFoundError:
        print(f'File was not found at {source}')

    except PermissionError:
        print(f"App doesn't have necessary permissions to move file at {source}")

    except Exception:
        print(f'ERROR: {Exception}')


def make_folder(name, path):

    # Makes a folder at a certain path an checks if it already exists

    try:
        os.chdir(path)

        if name not in os.listdir():
            os.mkdir(path+name)

        return path+name

    except FileExistsError:
        print(f'make_folder - {name} Folder already exists at {path}')

    except PermissionError:
        print(f"App doesn't have necessary permissions to make folder at {path}")

    except Exception:
        print(f'ERROR: {Exception}')


def organize_file(source, folder_path, folder_name):
    # Creates a folder named 'folder_name' at 'folder_path', then puts the file at 'source' in it.

    new_dir = make_folder(folder_name, folder_path)

    move_file(source, new_dir)


def organize(folder, new_folder):

    # Moves to the folder that will be organized and saves the current directory
    os.chdir(path(folder))
    current_dir = path(folder)

    if new_folder == '':
        new_folder = 'misc'

    # Variable to check the possible extentions
    filetypes = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
        'videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
        'music': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a'],
        'text': ['.txt', '.csv', '.doc', '.docx', '.pdf', '.rtf', '.html']
    }

    for file in os.listdir():
        name, extention = os.path.splitext(file)

        current_file = current_dir+file

        # Organize the files based on the extention
        # Uses the 'organize_file' function to move the files to the desired folders

        # If extention is known, move to the respective folders

        if extention in filetypes['images']:
            organize_file(current_file, path('Pictures'), new_folder)

        elif extention in filetypes['videos']:
            organize_file(current_file, path('Videos'), new_folder)

        elif extention in filetypes['music']:
            organize_file(current_file, path('Music'), new_folder)

        elif extention in filetypes['text']:
            organize_file(current_file, path('Documents'), new_folder)
        
        # If not, organize the files inside the current directory
            
        elif extention:
            # Make a folder for the extention
            make_folder(new_folder,current_dir)

            # Moves the file to the new folder
            organize_file(current_file, current_dir+new_folder+'/', extention)

if len(sys.argv) != 3:
    print(""" Como Usar:
          
 Este programa recebe dois argumentos: A pasta que você deseja organizar e o nome da pasta que receberá os arquivos.
 Os arquivos serão movidos para pastas de acordo com sua extensão (.png para Imagens, .txt para Documentos, etc).

 Exemplo de uso:
 python3 main.py Downloads misc

 Neste exemplo, os arquivos serão retirados da pasta Downloads e movidos para suas respectivas pastas, e então dentro de uma nova pasta 'misc'.
 'misc' é o nome padrão da pasta.""")

# 1 -> Folder to organize
# 2 -> Folder name

else:
    organize(sys.argv[1], sys.argv[2])
    print(f"Your {sys.argv[1]} folder has been organized!")