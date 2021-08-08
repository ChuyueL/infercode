from os import listdir
from os.path import isfile, join
from sklearn.cluster import KMeans
import sys 
import numpy as np

path = join(sys.path[0], "files")
files = [f for f in listdir(path) if isfile(join(path, f))]

