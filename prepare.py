from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random

# creat directory
dataset_home = 'Real Sample V1/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
    labeldirs = ['Clays/', 'Loams/', 'Reds/', 'Sandys/']
    for labldir in labeldirs:
        newdir = dataset_home + subdir + labldir
        makedirs(newdir, exist_ok=True)

# seed random
seed(1)
# define ratio
val_ratio = 0.2
# copy training
src_directory = 'Prepare IMG/'
for file in listdir(src_directory):
    src = src_directory + '/' + file
    dst_dir = 'train/'

    if random() < val_ratio:
        dst_dir = 'test/'
    if file.startswith('clay'):
        dst = dataset_home + dst_dir + 'Clays/' + file
        copyfile(src, dst)
    elif file.startswith('loam'):
        dst = dataset_home + dst_dir + 'Loams/' + file
        copyfile(src, dst)
    elif file.startswith('red'):
        dst = dataset_home + dst_dir + 'Reds/' + file
        copyfile(src, dst)
    elif file.startswith('sand'):
        dst = dataset_home + dst_dir + 'Sandys/' + file
        copyfile(src, dst)
