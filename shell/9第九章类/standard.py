from collections import OrderedDict
from random import randint

fav_language=OrderedDict()

fav_language['lily']="C++"
fav_language['lucy']="Java"
fav_language['jim']="Python"
fav_language['lilei']="JS"
fav_language['hmm']="SQL"

for name,lan in fav_language.items():
    print(name.title() + " fav language is" + lan.title() + ".")

num=0
while True:
    num += 1
    print(randint(1,100))
    if num ==10:
        break