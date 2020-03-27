import os
def show_files_in_directory():
    path = input("Welke directory moet getoond worden?\n")
    for fn in os.listdir(path):
        print(os.path.join(path,fn))
