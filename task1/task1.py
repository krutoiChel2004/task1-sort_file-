import os
import re
from create_file import create_file

path = 'D:\\work\\task1\\data'

list_cls = ['dog', 'cat', 'panda', 'elephant', 'lion', 'tiger', 'cow', 'bear', 'zebra', 'giraffe']


# create file for sorting
for i in list_cls:
    create_file(i, 5)

# создание системы папок
os.mkdir("data_sort")
for i in list_cls:
    os.mkdir(f"data_sort//{i}")
    
list_dir = os.listdir('data')   
patern = r'\d+'
repl = r''

# сортировка
for i in list_dir:
    dir = re.sub(patern, repl, i.split('.')[0]).strip()
    if dir in list_cls:
        os.replace(f"data//{i}", f"data_sort//{dir}//{i}")


