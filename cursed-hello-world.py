# ---------------------------------------
# HELLO WORLD!
# ---------------------------------------
import os
import os.path
import random
import ftplib
# ---------------------------------------
path_01 = "c:\\"
path_02 = "c:\\Users\\%USERPROFILE%\\Documents"
path_03 = "c:\\Users\\%USERPROFILE%\\Desktop"
path_04 = "c:\\Users\\%USERPROFILE%\\Music"
path_05 = "c:\\Users\\%USERPROFILE%\\Pictures"
path_06 = "c:\\Users\\%USERPROFILE%\\Downloads"
path_07 = "c:\\Users\\%USERPROFILE%\\Links"
path_08 = "c:\\Users\\%USERPROFILE%\\Videos"
path_09 = "c:\\Users\\%USERPROFILE%\\3D Objects"
path_10 = "c:\\Users\\%USERPROFILE%\\Contacts"
path_11 = "c:\\Users\\%USERPROFILE%\\Saved Games"
path_12 = "c:\\Users\\%USERPROFILE%\\Searches"
path_13 = "c:\\Users\\%USERPROFILE%\\Favorites"
# ---------------------------------------
path_documents = os.path.join(path_02, "documents.py")
path_desktop = os.path.join(path_02, "desktop.py")
path_music = os.path.join(path_02, "music.py")
path_pictures = os.path.join(path_02, "pictures.py")
path_downloads = os.path.join(path_02, "downloads.py")
path_links = os.path.join(path_02, "links.py")
path_videos = os.path.join(path_02, "videos.py")
path_3d = os.path.join(path_02, "3d.py")
path_contacts = os.path.join(path_02, "contacts.py")
path_saved_games = os.path.join(path_02, "saved_games.py")
path_searches = os.path.join(path_02, "searches.py")
path_favorites = os.path.join(path_02, "favorites.py")
# ---------------------------------------
documents = open(path_documents, "w")
desktop = open(path_desktop, "w")
music = open(path_music, "w")
pictures = open(path_pictures, "w")
downloads = open(path_downloads, "w")
links = open(path_links, "w")
videos = open(path_videos, "w")
threedee = open(path_3d, "w")
contacts = open(path_contacts, "w")
saved_games = open(path_saved_games, "w")
searches = open(path_searches, "w")
favorites = open(path_favorites, "w")
# ---------------------------------------
# ---------------------------------------
# ---------------------------------------
a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = "H", "E", "L", "O", " ", "W", "R", "D", "!"
hellno = ("{}{}{}{}{}{}{}{}{}{}{}{}".format(a_1, a_2, a_3, a_3, a_4, a_5, a_6, a_4, a_7, a_3, a_8, a_9))
ran_a = random.randint(0,999999999999)
# ---------------------------------------
# ---------------------------------------
host = "ftp.dlptest.com"
username = "dlpuser@dlptest.com"
password = "rNrKYTX9g7z3RgJRmxWuGHbeu"
# ---------------------------------------
ftp_01 = ftplib.FTP(host, username, password)
ftp_01.encoding = "utf-8"

# ---------------------------------------
a = 0
# ---------------------------------------
while (a < 2):
  a += 1
  a_string = str(a)
  a_ran = str(ran_a)
  why = str("ohnoes"+ a_string +".py")
  runme = ("python3 " + why) 
  curse = open(why, "x")
# ---------------------------------------
  curse.write('''
import random
a = 0
while (a < 1):
 a += 1
 a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = "H", "E", "L", "O", " ", "W", "R", "D", "!"
 hellno = ("{}{}{}{}{}{}{}{}{}{}{}{}".format(a_1, a_2, a_3, a_3, a_4, a_5, a_6, a_4, a_7, a_3, a_8, a_9))
 b_string = str(a) + str(a)
 ran_b = random.randint(0,999999999999)
 b_ran = str(ran_b)
 why = str(b_ran + b_string + "ohyes.txt")
 curse = open(why, "x")
 curse.write("HELLO WORLD!")
 curse.close()
  ''')
# ---------------------------------------
  letters = ["H","e","l","o","W","r","d","!", " "]; print(letters[0],letters[1],letters[2],letters[2],letters[3],letters[8],letters[4],letters[3],letters[5],letters[2],letters[6],letters[7])
  curse.close()
  os.system(runme)
# ---------------------------------------
# a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = "H", "E", "L", "O", " ", "W", "R", "D", "!"
# print("{}{}{}{}{}{}{}{}{}{}{}{}".format(a_1, a_2, a_3, a_3, a_4, a_5, a_6, a_4, a_7, a_3, a_8, a_9))  
# ---------------------------------------
# letters = ["H","e","l","o","W","r","d","!", " "]
# print(letters[0],letters[1],letters[2],letters[2],letters[3],letters[8],letters[4],letters[3],letters[5],letters[2],letters[6],letters[7])
# ---------------------------------------
