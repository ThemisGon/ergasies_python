import os
import json


#bazo ton xrhsth na mou dosei ena fakelo pou periexei lexiko
print ('dose ena onoma arxeiou pou periexei ena h perissotera lexika: ')
c= str(input(''))
file=open (c,'r')

 


max=0
for line in file:
    length=(len(line))
    counta=line.count("{")+line.count("[")
    countamhn=line.count("],[")+line.count("},{")
    if length<=3:
        #print (line +' bathos einai 0')
        bathmos=0
        if max<bathmos:
            max=bathmos
            max_lex=line
    elif counta==2: 
        #print (line +' bathos einai 2')
        bathmos=2
        if max<bathmos:
            max=bathmos
            max_lex=line
    elif counta==1:
        #print (line +' bathos einai 1')
        bathmos=1
        if max<bathmos:
            max=bathmos
            max_lex=line
    else:
        bathmos=counta-countamhn
        if max<bathmos:
            max=bathmos
            max_lex=line
        #print (line+'o bathmos einai'+ str(bathmos))

print (max_lex+'βάθος: '+str(max))     




#print(json.dumps(file, indent=4))
#print (type(x))
#test-lexiko.txt
#koitao thn json gai bohtheia
#print(json.dumps(x, indent=4)) na do auth thn entolh
#testaro.txt