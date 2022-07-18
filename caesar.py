def caesar_cipher(string, x):
    i = 0 
    phrase = ''
    while i < len(string):
#remplacer chaque lettre en fonction de si elle est majuscule, normale ou rien de ces deux, symboles notamment.        
        if ord(string[i]) >= 65 and ord(string[i]) <=90: #pour les lettres qui sont en majuscules
            if ord(string[i]) + x > 90:
                phrase += chr((64 + ord(string[i]) + x - 90))
            else: 
                phrase += chr(ord(string[i])+  x )
   
    
        elif ord(string[i]) >= 97 and ord(string[i]) <=122: #pour les lettres en minuscules
            if ord(string[i]) + x > 122:
                phrase += chr((96 + ord(string[i]) + x - 122))
            else: 
                phrase += chr(ord(string[i])+  x )
        
        else: phrase += string[i] #tout ce qui n'est ni majuscule ni minuscule
            
        i += 1
    print (phrase)
                
caesar_cipher("WHAT a strings, c'est coolos, je vais aller me peter une biere", 5)

