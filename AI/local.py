import os
import subprocess as sp


paths = {
  'Discord'  "C:\Users\Dell_M4500\AppData\Local\Discord\Update.exe --processStart Discord.exe"
     'icq'  "C:\Users\Dell_M4500\AppData\Roaming\ICQ\bin\icq.exe"
       'Telegram' "C:\Users\Dell_M4500\AppData\Roaming\Telegram Desktop\Telegram.exe"
       'notepad++' "C:\Program Files\Notepad++\notepad++.exe"
       'skype' "C:\Program Files (x86)\Microsoft\Skype for Desktop\Skype.exe"
       }

def open_camera():
     sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad++'])


def open_discord():
    os.startfile(paths['discord'])

def open_icq():
    os.startfile(paths['icq'])

def open_Telegram():
    os.startfile(paths['Telegram'])

def open_skype():
    os.startfile(paths['skype'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])

def open_Terminal():
    os.system('Terminal')
    
