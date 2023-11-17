from pathlib import Path
import re
import os
from initial_form import initial
from zeroing import zeroing_file, zeroing
from delpred import pos

zeroing_file('result_themes')

folder = Path(str(input()))
result = ''

for file in folder.iterdir(): # перебор файлов
    file = open(file, 'r', encoding='utf-8')
    functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP', 'ADVB', 'NPRO'}
    words = file.read()
    words = re.findall('[a-zа-яё]+', words, flags=re.IGNORECASE)
    words = ([word1 for word1 in words if pos(word1) not in functors_pos])
    file.close()
    for word in words:
        result += (initial(word)).upper() + ' '

    result_file = open("result_themes/" + os.path.basename(file.name) + ".txt", "w+", encoding="ANSI")
    result_file.write(result)
    result_file.close()
    result = ''

