from os import listdir
from os.path import isfile, join, splitext
from sklearn.cluster import KMeans
import sys 
import numpy as np
import argparse
from pathlib import Path
from scipy import spatial
sys.path.append(str(Path('.').absolute().parent))
from infercode.client.infercode_client import InferCodeClient
import logging
logging.basicConfig(level=logging.INFO)

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
    lang = extension.replace('.', '')
    print(lang)
    infercode = InferCodeClient(language=lang)
    infercode.init_from_config()
    vector = infercode.encode(code)
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
    vectors.append(vector)

code_vecs = np.column_stack((files, vectors))


