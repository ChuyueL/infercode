from client.infercode_client import InferCodeClient
from sklearn.manifold import TSNE
import logging
logging.basicConfig(level=logging.INFO)

import configparser 
config = configparser.ConfigParser()
config.read("configs/java_small_config.ini")



infercode = InferCodeClient(config)
vectors = infercode.encode(["for (i = 0; i < n; i++)", "struct book{ int num; char s[27]; }shu[1000];"])

print(vectors)
# vectors = infercode.encode(["for int i = 0"])


# print(vectors )