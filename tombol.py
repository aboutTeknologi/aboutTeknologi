import os
from time import sleep

Red = '\033[91m'
Green = '\033[92m'
b = '\033[94m'
c = '\033[96m'
White = '\033[97m'
y = '\033[93m'
m = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'
os.system('clear')
print(y+'═'*54)
print(m+'\t                TERMUX KEY!')
print(c+'\t             BY ABOUT TEKNOLOGI')
print(y+'═'*54)
print('\nProses..')
sleep(1)
print(b+'\n-> Loading 20%')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(b+'-> Loading 40%')
sleep(1)
print(b+'-> Loading 60%')
sleep(1)
print(b+'-> Loading 80%')
sleep(1)
print(b+'-> Loading 90%')
sleep(1)
print(b+'-> Loading 100%')
sleep(1)
key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(Red+'\n-> Installing Key...')
sleep(2.5)
os.system('termux-reload-settings')
print(Green+'-> Done! Termux Key Succes Installed')

# untuk memudahkan anda menggunakan termux!
# by saha aing
