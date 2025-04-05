import chromadb
from sentence_transformers import SentenceTransformer

class Memory:
    def __init__(self,collection_name : str | None = 'test'):
        self.client = chromadb.Client()
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.collection_name = collection_name
        self.collection = self.client.get_or_create_collection(self.collection_name)

    def add_memory(self,memory: str, id: str):
        memory = f"[{id},{memory}]"
        ids = [id]
        embeddings = self.embedding_model.encode(memory)
        self.collection.add(embeddings=embeddings.tolist(),documents=memory, ids=ids)

    def query_memory(self,query: str, n_results: int | None = 1):
        query_embedding = self.embedding_model.encode(query)
        results = self.collection.query(query_embedding, n_results=n_results)
        result = results["documents"][0]
        return result
    
    def clear_collection(self):
        self.client.delete_collection(name=self.collection_name)
