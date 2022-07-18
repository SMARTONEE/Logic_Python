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
                


def Jean_Michel_Trader(arr):
    benef_max = 0
    i = 0
    index_achat = 0
    index_vente = 0
    while i < len(arr):
        y = i + 1
        while y < len(arr):
            if benef_max < arr[y] - arr[i]:
                benef_max = arr[y] - arr[i] 
                index_achat = i
                index_vente = y
            y += 1
        i += 1      
    print(benef_max)
    print ([index_achat, index_vente])

a = [-4, 20.7, -100, 9, 15, 8, 20, 1, 10]

print(a[4]-a[2])
print(len(a))

Jean_Michel_Trader(a)