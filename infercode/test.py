from client.infercode_client import InferCodeClient
infercode = InferCodeClient()
vectors = infercode.encode(["for (i = 0; i < n; i++)", "struct book{ int num; char s[27]; }shu[1000];"])
print(vectors)  

