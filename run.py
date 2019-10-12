#A simple project on Morse code translation from plain text to morse code and vice versa

#Importing the user defined modules
import encryption as cipher
import decryption as decipher                           

print("\t\t\t\t***********************")
print("\t\t\t\t MORSE CODE TRANSLATOR ")
print("\t\t\t\t***********************")
print("\n")

ch= input("Press 'E' to encrypt and 'D' to decrypt: ")
print("\n")

if (ch=='E' or ch== 'e'):
    plain_text= input("Enter text to encrypt: ").upper()
    print("\n")
    
    #Calling encryption function
    cipher.encryptor(plain_text)

elif (ch=='D' or ch== 'd'):
    morse_code= input("Enter morse code to decrypt: ")
    print("\n")
    
    #Calling decryption function
    decipher.decryptor(morse_code)

else:
    print("Invalid input!!!")        