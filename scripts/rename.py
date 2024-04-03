import os
import re

def rename_files_with_numbering(folder_path):
    pattern = r"^(\d+)"

    files = os.listdir(folder_path)

    files.sort(key=lambda x: int(re.findall(pattern, x)[0]))

    for i, file in enumerate(files):
        old_path = os.path.join(folder_path, file)
        new_file_name = re.sub(pattern, str(i+1), file)
        new_path = os.path.join(folder_path, new_file_name)
        os.rename(old_path, new_path)

if __name__ == "__main__":
    folder_path = "/home/kushal/Documents/textcat/outputfiles"

    rename_files_with_numbering(folder_path)
