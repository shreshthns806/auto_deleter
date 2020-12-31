import os
import shutil
import time

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime


def main():

    deleted_folder_count = 0
    deleted_file_count = 0

    path = "I:/WHJR/Python/C-99/Auto_Deleter/deleteThisFolder"

    days = 30

    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):

        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                shutil.rmtree(root_folder)
                deleted_folder_count = deleted_folder_count + 1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        shutil.rmtree(root_folder)
                        deleted_folder_count = deleted_folder_count+1
                for file in files:
                    file_path = os.path.join(root_folder,file)
                    if seconds >= get_file_or_folder_age(file_path):
                        os.remove(path)
                        deleted_file_count += 1
        else:
            if seconds >= get_file_or_folder_age(path):
                os.remove(path)
    else:
        print('Path not found!')
    
main()