import shutil
import os
from colorama import Fore, Style, init

init()


banner = r"""
$$$$$$$$\                   $$\      $$$$$$\                                
$$  _____|                  $$ |    $$  __$$\                               
$$ |   $$$$$$\   $$$$$$$\ $$$$$$\   $$ /  \__| $$$$$$\   $$$$$$\  $$\   $$\ 
$$$$$\ \____$$\ $$  _____|\_$$  _|  $$ |      $$  __$$\ $$  __$$\ $$ |  $$ |
$$  __|$$$$$$$ |\$$$$$$\    $$ |    $$ |      $$ /  $$ |$$ /  $$ |$$ |  $$ |
$$ |  $$  __$$ | \____$$\   $$ |$$\ $$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |
$$ |  \$$$$$$$ |$$$$$$$  |  \$$$$  |\$$$$$$  |\$$$$$$  |$$$$$$$  |\$$$$$$$ |
\__|   \_______|\_______/    \____/  \______/  \______/ $$  ____/  \____$$ |
                                                        $$ |      $$\   $$ |
                                                        $$ |      \$$$$$$  |
                                                        \__|       \______/                     
"""

print(Fore.GREEN + Style.BRIGHT + banner+ Style.RESET_ALL)


def copy_files(source_dir, destination_dir):

    if not os.path.isdir(source_dir):
        print(Fore.RED + Style.BRIGHT + "The Source directory is not valid !")
        return
    if not os.path.isdir(destination_dir):
        print(Fore.RED + Style.BRIGHT+  "The Destination directory is not valid!")
        return

   
    files = os.listdir(source_dir)
    for file in files:
        source_file = os.path.join(source_dir, file)
        destination_file = os.path.join(destination_dir, file)

        
        if os.path.isfile(source_file):
            shutil.copy(source_file, destination_file)
            print(Fore.GREEN + Style.BRIGHT + "File : " + Fore.WHITE + file +"Copy !")


source_dir = input(Fore.WHITE + Style.BRIGHT + "Directory Source :  ")
destination_dir = input(Fore.WHITE + Style.BRIGHT +"Directory Destination :  ")


copy_files(source_dir, destination_dir)
