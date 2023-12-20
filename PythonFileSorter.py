import shutil

import os

# Change this to the file path where you want the program to sort
path = r"C:/Users/Ben/Desktop/Python File Sorter/"

file_name = os.listdir(path)

# Add the folders that you want the program to create
folder_names = ['text files', 'pdf files', 'image files','csv files', 'other files']

# Change the range to the amount of folders listed under folder_names              
for loop in range (0,5):
    if not os.path.exists(path + folder_names[loop]):
     print(path + folder_names[loop])
     os.makedirs(path + folder_names[loop])
     
# If you need to add a file type, copy and paste any of the elif statements below and modify the "." portion and the path portion
# Be sure to paste the elif statement in between the if and else statement
for file in file_name:
   if ".csv" in file and not os.path.exists(path +"csv files/" + file):
      shutil.move(path + file,path +"csv files/" + file)
   elif ".png" in file and not os.path.exists(path +"image files/" + file):
      shutil.move(path + file,path +"image files/" + file)
   elif ".jpg" in file and not os.path.exists(path +"image files/" + file):
      shutil.move(path + file,path +"image files/" + file)
   elif ".txt" in file and not os.path.exists(path +"text files/" + file):
      shutil.move(path + file,path +"text files/" + file)
   elif ".pdf" in file and not os.path.exists(path +"pdf files/" + file):
      shutil.move(path + file,path +"pdf files/" + file)   
   else:    
      shutil.move(path + file,path +"other files/" + file)   




