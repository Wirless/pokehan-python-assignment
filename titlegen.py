#################################
# Module name: title gen
# Version: 1.00
# Author: Patryk Zmyslony 
#
#
#################################

def titlegen(symbol, title):
    '''
    titlegen module purpose is to take in 2 strings
    and output a Title screen name into the window.
    (str+str) -> str
    >>>titlegen(symbol="+",title="Poke-Han")
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                           Poke-Han                               
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    '''
	print(f"{symbol}"*60)
	print(" "*25+title)
	print(f"{symbol}"*60)
    
#titlegen(symbol="+",title="Poke-Han")