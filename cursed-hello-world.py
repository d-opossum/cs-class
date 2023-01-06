# Trying to find ways to do the worst method of "Hello World"
#a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = "H", "E", "L", "O", " ", "W", "R", "D", "!"; print("{}{}{}{}{}{}{}{}{}{}{}{}".format(a_1, a_2, a_3, a_3, a_4, a_5, a_6, a_4, a_7, a_3, a_8, a_9))
#letters = ["H","e","l","o","W","r","d","!", " "]; print(letters[0],letters[1],letters[2],letters[2],letters[3],letters[8],letters[4],letters[3],letters[5],letters[2],letters[6],letters[7])

# a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = "H", "E", "L", "O", " ", "W", "R", "D", "!"; print("{}{}{}{}{}{}{}{}{}{}{}{}".format(a_1, a_2, a_3, a_3, a_4, a_5, a_6, a_4, a_7, a_3, a_8, a_9))
# letters = ["H","e","l","o","W","r","d","!", " "]; print(letters[0],letters[1],letters[2],letters[2],letters[3],letters[8],letters[4],letters[3],letters[5],letters[2],letters[6],letters[7])
# HELLO WORLD!
# -------------------------------------------
# Not really a class work
# trying to do the most cursed way to say hello world
# -------------------------------------------
# It doesn't need to be said, but don't run this.
# -------------------------------------------
import os
import random
a = 0
while (a < 6942069):
  a += 1
  a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = "H", "E", "L", "O", " ", "W", "R", "D", "!"
  hellno = ("{}{}{}{}{}{}{}{}{}{}{}{}".format(a_1, a_2, a_3, a_3, a_4, a_5, a_6, a_4, a_7, a_3, a_8, a_9))
  a_string = str(a)
  ran_a = random.randint(0,9999999999999999999)
  a_ran = str(ran_a)
  why = str("ohnoes"+ a_string +".py")
  runme = ("python3 " + why) 
  curse = open(why, "x")
  curse.write('''
import random
a = 0
while (a < 420):
 a += 1
 a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = "H", "E", "L", "O", " ", "W", "R", "D", "!"
 hellno = ("{}{}{}{}{}{}{}{}{}{}{}{}".format(a_1, a_2, a_3, a_3, a_4, a_5, a_6, a_4, a_7, a_3, a_8, a_9))
 b_string = str(a) + str(a)
 ran_b = random.randint(0,99999999999999999999)
 b_ran = str(ran_b)
 why = str(b_ran + b_string + "ohyes.txt")
 curse = open(why, "x")
 curse.write("HELLO WORLD!")
 curse.close()
  ''')
  letters = ["H","e","l","o","W","r","d","!", " "]; print(letters[0],letters[1],letters[2],letters[2],letters[3],letters[8],letters[4],letters[3],letters[5],letters[2],letters[6],letters[7])
  curse.close()
  os.system(runme)
