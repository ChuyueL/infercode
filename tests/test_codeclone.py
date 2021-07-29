#cosine similarity
import numpy as np
import sys
from pathlib import Path
# To import upper level modules
sys.path.append(str(Path('.').absolute().parent))
from infercode.client.infercode_client import InferCodeClient
import logging
logging.basicConfig(level=logging.INFO)

def cosine_similarity(a, b):
    similarity = np.dot(a, b)/(np.linalg.norm(a) * np.linalg.norm(b))
    return similarity

infercode = InferCodeClient(language="c")
infercode.init_from_config()

vectors = infercode.encode(["for (i = 0; i < n; i++)", "struct book{ int num; char s[27]; }shu[1000];"])

if cosine_similarity(vectors[0], vectors[1]) > 0.8:
    print("code clone")
else:
    print("not clone")



