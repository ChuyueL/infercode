from os import listdir
from os.path import isfile, join, splitext
from sklearn.cluster import KMeans
import pdb
import importlib
import sys 
import numpy as np
import argparse
from pathlib import Path
from scipy import spatial
from sklearn.neighbors import NearestNeighbors
from infercode.data_utils import language_util
sys.path.append(str(Path('.').absolute().parent))
import infercode
infercode = importlib.reload(infercode)
from infercode.client.infercode_client import InferCodeClient
#from infercode.data_utils.language_util import LanguageUtil
from language_util import LanguageUtil
import logging
logging.basicConfig(level=logging.INFO)

#language_util = importlib.reload(language_util)
#print(language_util)

def read_file(filepath):
    with open(filepath) as f:
        code = f.read().splitlines()
    code = remove_trailing_spaces(code)
    code = ' '.join(code)
    print(code)
    return code

def encode_file(filepath):
    code = read_file(filepath)
    _, extension = splitext(filepath)
    #pdb.set_trace()
    util = LanguageUtil()
    #lang = extension.replace('.', '')
    lang = util.get_language_by_file_extension(extension)
    print(lang)
    infercode = InferCodeClient(language=lang)
    infercode.init_from_config()
    print("code again: ", code)
    vector = infercode.encode(code)
    print(vector)
    return vector


def remove_trailing_spaces(arr):
    return [s.strip() for s in arr]



parser = argparse.ArgumentParser()
parser.add_argument('file', type = str, help = 'File to search for implementations of in other languages')
args = parser.parse_args()


original_file = args.file
original_vector = encode_file(original_file)

path = join(sys.path[0], "files")
files = [f for f in listdir(path) if isfile(join(path, f))]

vectors = []

for entry in files:
    filepath = join(sys.path[0], "files", entry)
    vector = encode_file(filepath)
    print("current vector:", vector)
    vectors.append(vector)

vectors = np.array(vectors)

code_vecs = np.column_stack((files, vectors))
print("all vectors: ", vectors)

neighbours = NearestNeighbors(n_neighbors = 2).fit(vectors)
#will return indices - just find the filename using the index
indices = neighbours.kneighbours(original_vector, return_distance = False)
closest_files = []
for i in indices:
    closest_files.append(files[i])

print(closest_files)



