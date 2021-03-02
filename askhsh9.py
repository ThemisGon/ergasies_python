#Φτιαχνω μια συναρτηση που βρίσκει το πλήθος του καθε γράμματος
def letterFrequency(fileName, letter): 
    # open file in read mode 
    file = open(fileName, 'r') 
  
    # store content of the file in a variable 
    text = file.read() 
  
    # using count() 
    return text.count(letter) 
  
#open file in read mode
f = open('two_cities_ascii.txt', 'r') 

#read the content of file and replace spaces with nothing
data = f.read().replace(" ","")

#get the length of the data
number_of_characters = len(data)
#print('Number of characters in text file :', number_of_characters)




with open('two_cities_ascii.txt', 'r') as f:
    file_contents = f.read() 
#metatrepo to keimeno se ascii kai ta bazo se lista
ascii_vals = [ord(char) for char in file_contents]
#print (ascii_vals)

#brisko posa stoixeia einai monoi apo to keimeno kai ypologizo to plhthos tous

c=0
k=range(65,90,2)
f=65
posa=0
for n in k:
#to modulo 3 den pairnei to a mesa stis metriseis tou 
    
    if(letterFrequency('two_cities_ascii.txt', chr(ascii_vals[f]))):
        #print("O "+ chr(f)+" exei :")
        #print(letterFrequency('two_cities_ascii.txt', chr(ascii_vals[f])))
        posa +=1

    f +=2

#ektypono to plhthos

k=range(97,122,2)
f=97

for n in k:
#to modulo 3 den pairnei to a mesa stis metriseis tou 
    if(letterFrequency('two_cities_ascii.txt', chr(ascii_vals[f]))):
        #print("O "+ chr(f)+" exei :")
        #print(letterFrequency('two_cities_ascii.txt', chr(ascii_vals[f])))
        posa +=1

    f +=2


#print (posa)


c=0
k=range(65,90,2)
f=65
asteri="*"
for n in k: 
    if(letterFrequency('two_cities_ascii.txt', chr(ascii_vals[f]))):
        c=letterFrequency('two_cities_ascii.txt', chr(ascii_vals[f]))
        tl=c/(posa*100)
        if (c % (posa*100) == 0) :
            print (chr(f)+":"+asteri*tl)
        else :
            tl=(c//(posa*100))+1
            print (chr(f)+":"+asteri*tl)
    f +=2

c=0
k=range(97,122,2)
f=97
asteri="*"
for n in k:
    if(letterFrequency('two_cities_ascii.txt', chr(ascii_vals[f]))):
        c=letterFrequency('two_cities_ascii.txt', chr(ascii_vals[f]))
        tl=c/(posa*100)
        if (c % (posa*100) == 0) :
            print (chr(f)+":"+asteri*tl)
        else :
            tl=(c//(posa*100))+1
            print (chr(f)+":"+asteri*tl)
    f +=2




