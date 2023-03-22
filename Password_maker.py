import random 



# Letters, numbers and symbols
alpha1 = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
alpha2 = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
alpha3 = ["0","1","2","3","4","5","6","7","8","9"]
alpha4 = ["!","@","#","$","%","-","_","&"]


alpha = alpha1 + alpha2 + alpha3 + alpha4

#Enter the length of the password
long = input("Long Password : ")

#We turn it into integer
long = int(long)

#Random selection according to the length of the word
x = random.choices(alpha , k=long)

#Transfer from the list to string
x = "".join(x)

print(x)

