import os
import subprocess

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[0m"


def make_past():
    past_name = "Dash SkyNet"
    folder_path = os.path.abspath("./functions/files/")
    
    link_path = os.path.expanduser("~/Documentos/") + past_name
    
    link_path2 = os.path.expanduser("~/Documentos/") + past_name+"/"    
    
    if not os.path.exists(link_path):
        subprocess.call(['mkdir', link_path])
        
        print(g+"[+] "+w+"Transferindo Dados")
        
        subprocess.call(['cp','-r', folder_path , link_path2])
       
    else:
        print(g+"Buscando dados...")
        
