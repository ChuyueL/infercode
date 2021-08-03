from os import listdir
from os.path import isfile, join
import sys 

path = join(sys.path[0], "files")
files = [f for f in listdir(path) if isfile(join(path, f))]

print(files)