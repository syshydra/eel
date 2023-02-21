import os
import eel
from functions.header import *


os.system('clear')

print(g+'[+]'+w+' opening...')
make_past()
eel.init('web')


eel.username(os.getlogin())

eel.start('index.html', size=(330, 630))