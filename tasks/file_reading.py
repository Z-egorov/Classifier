from pathlib import Path

def perm_files(dir_way):

    folder = Path(dir_way)


    if folder.is_dir():

        for file in folder.iterdir():
            file_read = open(file, encoding='utf-8')
            file_write = open("classification.txt", "a")
            file_write.write(file.name + " ")
