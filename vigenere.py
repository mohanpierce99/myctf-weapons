from itertools import cycle

def upper(x):
    return str(x).upper()

def crackVigenere(cipher,password):
    l=list(filter(lambda x:True if x!='{' and x!='}' else False,cipher)) #Remove curleys
    version=[ord(d1)%64-ord(d2)%64 for d1,d2 in zip(list(map(upper,l)),cycle(list(map(upper,password))))] #Do the calculation
    characters=[chr(num+65) if num>=0 else chr(65+(26+num)) for num in version] #Deal with mod26 subtraction
    return ''.join(characters) #Join em all finally

print(crackVigenere("gwox{RgqssihYspOntqpxs}",'blorpy'))