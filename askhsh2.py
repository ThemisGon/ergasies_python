import random
print ('Δώσε έναν όρο απο την ακολουθεία Fibonacci για τον οποιο θες να ελέγχεις αν είναι πρώτος ή οχι:')
p= int(input(''))
if p<= 1:
    Fib= p
f0=0
f1=1
for i in range (1,p):
    Fib =f0+f1
    f0 = f1
    f1 = Fib
k=0#μετράμε ενα πλήθος ετσι ώστε να ελεγξουμε αν για 20 αριθμους είναι πρώτος
arithmoi=[]
for i in range (0,20):   
        arithmoi.append(random.randrange(1,p))
        if ((arithmoi[i]**Fib)%Fib==arithmoi[i] % Fib):
            k +=1
            #print (k)
#print (arithmoi)
#print (k)
if k==20:
    print (str(p) +"ος όρος είναι ο "+ str(Fib) +" και είναι πρώτος")
else: 
    print (str(p) +"ος όρος είναι ο "+ str(Fib) +" και δεν είναι πρώτος")