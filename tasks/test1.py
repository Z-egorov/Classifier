from pathlib import Path

dir_way = str(input())
folder = Path(dir_way)


if folder.is_dir(): #
    #folder_count = len([1 for file in folder.iterdir()])
    for file in folder.iterdir():
        file_read = open(file, encoding='utf-8')
        file_write = open("classification.txt", "a")
        file_write.write(file.name + " ")

'''
for i in range(101, 100+folder_count+1):
    f = open(dir_way + str(i)+".txt",  encoding='utf-8')
    print(str(i)+".txt")
    print(f.read())
    print('\t')
'''