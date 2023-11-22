import os
import shutil

from_dir = "C:/Users/Sayed/Downloads"
to_dir = "C:/Users/Sayed/Documents"
files_name = os.listdir(from_dir)
documents = [".txt", ".doc", ".docx", ".pdf"]
for file_name in files_name:
    root, ext = os.path.splitext(file_name)
    if ext == "":
        continue
    if ext in documents:
        path_1 = from_dir + "/" + file_name
        path_2 = to_dir + "/" + "Document_Files"
        path_3 = path_2 + "/" + file_name
        if os.path.exists(path_2):
            shutil.move(path_1, path_3)
            print(f"{file_name} has been moved")
        else:
            print("There is not Document_Files folder")
            print("System is going to Document_Files folder...") 
            os.makedirs(path_2)
            shutil.move(path_1,path_2)
        