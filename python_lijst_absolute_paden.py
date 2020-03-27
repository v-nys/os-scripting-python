import os
def get_files_in_directory(path):
    file_paths = []
    for fn in os.listdir(path):
        file_paths.append(os.path.join(path,fn))
