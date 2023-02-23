import sys
import os
import base64

print("GDPatcher был написан DimLux#2690\n")

def open_file(file, type):
    if os.path.isfile(file):
        with open(str(file), type) as f:
            return f.read()
    else:
        sys.exit('Файла "' + file + '" не существует!')

def write_file(text, file):
    with open(str(file), "wb") as f:
        return f.write(text)

def patcher(old, new, lib):   
    if len(old) > len(new):
        null = ""
        null_length = 0
        while null_length < len(old) - len(new):
            null = null + "\0"
            null_length = null_length + 1
        if len(old) > 35:
            _old = old[:35] + "..."
        else:
            _old = old
        if len(new) > 35:
            _new = new[:35] + "..."
        else:
            _new = new
        print('Заменено "' + _old + '" на "' + _new + '"')
        return lib.replace(old.encode(), new.encode() + null.encode())
    elif  len(old) == len(new):
        if len(old) > 35:
            _old = old[:35] + "..."
        else:
            _old = old
        if len(new) > 35:
            _new = new[:35] + "..."
        else:
            _new = new
        print('Заменено "' + _old + '" на "' + _new + '"')
        return lib.replace(old.encode(), new.encode())
    else:
        sys.exit("\n       Ошибка: заменяющий текст больше по длине, чем оригинал!\n       Оригинальный текст: " + old + "\n       Заменяющий текст: " + new)
            
def base64_encode(text):
        if isinstance(text, int) == True:
            text = str(text)
        return base64.b64encode(text.encode("utf-8")).decode("UTF-8")