run1 = [1,2,3]
run2 = [2,3,4]
run3 = [3,4,5]
run4 = [4,5,6]


def titlegen(title):
	print("+"*60)
	print(" "*25+title)
	print("+"*60)

def pokehan():
	
titlegen(title="Poke-Han")

Microsoft Windows [Version 10.0.17134.1130]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\19PZmyslony.avtos>cd desktop

C:\Users\19PZmyslony.avtos\Desktop>python pokehan.py
Traceback (most recent call last):
  File "pokehan.py", line 9, in <module>
    titlegen()
TypeError: titlegen() missing 1 required positional argument: 'title'

C:\Users\19PZmyslony.avtos\Desktop>python pokehan.py
Traceback (most recent call last):
  File "pokehan.py", line 8, in <module>
    titlegen(Poke-Han)
NameError: name 'Poke' is not defined

C:\Users\19PZmyslony.avtos\Desktop>python pokehan.py
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    poke-han
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

C:\Users\19PZmyslony.avtos\Desktop>python pokehan.py
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         Poke-Han
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

C:\Users\19PZmyslony.avtos\Desktop>python pokehan.py
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         Poke-Han
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

C:\Users\19PZmyslony.avtos\Desktop>