#cosine similarity
import numpy as np
import sys
import argparse
from pathlib import Path
# To import upper level modules
sys.path.append(str(Path('.').absolute().parent))
from infercode.client.infercode_client import InferCodeClient
import logging
logging.basicConfig(level=logging.INFO)

def cosine_similarity(a, b):
    similarity = np.dot(a, b)/(np.linalg.norm(a) * np.linalg.norm(b))
    return similarity


parser = argparse.ArgumentParser()
parser.add_argument('file1', type = str, help = '')
parser.add_argument('file2', type = str, help = '')
args = parser.parse_args()

file1 = args.file1
file2 = args.file2

with open(file2) as f:
    code1 = f.read().splitlines()

with open(file2) as f:
    code2 = f.read().splitlines()

code1 = ' '.join(code1)
code2 = ' '.join(code2)

print(code1)
print(code2)


infercode = InferCodeClient(language="c")
infercode.init_from_config()

vectors = infercode.encode([code1, code2])


if cosine_similarity(vectors[0], vectors[1]) > 0.8:
    print("code clone")
    print(cosine_similarity(vectors[0], vectors[1]))
else:
    print("not clone")
    print(cosine_similarity(vectors[0], vectors[1]))

