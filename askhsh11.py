#testaro1.txt
import json 
import re
#bazo ton xrhsth na mou dosei ena fakelo pou periexei lexiko
print ('dose ena onoma arxeiou pou periexei ena h perissotera lexika: ')
c= str(input(''))
file=open (c,'r')



lex={}
def syn(res):
 for keys,values in res.items():
     
     
     if type(values)is dict:
         syn(values)#ama einai lexiko xana kalo thn sunarthsh gia na kano thn idia diadikasia
         if (keys in lex):#koitao ama yparxei to kleidi
            lex[keys]+=1
         else:
            lex[keys]=1
     elif (keys in lex):
         lex[keys] += 1
     else:
         lex[keys]=1
     if type(values) is list:
         for x in range(len(values)):
               if type(values[x]) is dict:
                 syn(values[x])
                 











for line in file:
   print (type (line))
   print (line)
   res = json.loads(line)#to metatrepo se lexiko
   syn(res)#synarthsh pou bohtha sta kleidia apo ta emfoleumena lexika
   
   Maxkleid = max(lex.items(), key=lambda x: x[1])
   Maxlex = list()
   for keys, values in lex.items():
      if values == Maxkleid[1]:
         Maxlex.append(keys)
   print(Maxlex)
   
   
   
   
   
   
   
   
   
   
   
   
   #to metatrepo se lexiko
   #res = json.loads(line)
   #print (res)
   #print (type (res))
   #for keys,values in res.items():
     # kleidia= keys
      #times=values
      #if kleidia==times:
         #for kleidia in times:
          #  plth+=1
     # times1=len(times)
      #print (times1)
      #times12=times1-1
      #for times[0] in times[times12]:
      #  posa+=1 
      #print (posa) 
     # for times[1] in times[times12]:
     #    posa1+=1
     # print (posa1)


file.close()     
         
   #kleidia=res.keys()
   #print (kleidia)
   #times=res.values()
   #print(times)
   #print(type(times))
   
   #g=list(res.values())
   #print (g)
   #for i in kol:
     # if pap==2:
      #   key=i
     #    print(i)
      #   pap=0
     # if i=="{":
      #  pap+=1
     #   plth+=1
 #  print (plth)
   