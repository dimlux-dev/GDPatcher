from program import open_file, write_file, patcher, base64_encode

#открытие файлов
dir = "/storage/emulated/0/DimLux/python/gdpatcher/" #нужно указать путь, где находится main.py. (опционально, некоторых случия можно не указывать, зависит от ОС, Windows или Linux)

#можно использовать свои библиотеки

#параметр "rb" открывает файл в байтах
arm7 = open_file(dir + "libs/libcocos2dcpp.so", "rb") 
modmenu = open_file(dir + "libs/libgame.so", "rb")

#параметр "r" открывает файл как обычный текст
IAD_icon = open_file(dir + "IAD_icon.txt", "r")
luxcoriaIcon = open_file(dir + "luxcoriaIcon.txt", "r")
######################################

#шаблоны
# arm7 = patcher("", "", arm7)
# modmenu = patcher("", "", modmenu)
##############################

#конфиги
url_database = "http://luxcoria.7m.pl/server/////" #не больше не меньше 33 символов
####################################

#пачинг
print("\nЗамена URL сервера:")
arm7 = patcher("http://www.boomlings.com/database", url_database, arm7)
arm7 = patcher(base64_encode("http://www.boomlings.com/database"), base64_encode(url_database), arm7)

print("\nДругое:")
arm7 = patcher("Download the soundtracks", ":)", arm7)

print("\nЗамена иконки:")
modmenu = patcher(IAD_icon, luxcoriaIcon, modmenu)
##########################################


#сохранения файлов
write_file(arm7, dir + "patched_libs/libcocos2dcpp.so")
write_file(modmenu, dir + "patched_libs/libgame.so")
################################

print("\nУспешно!")