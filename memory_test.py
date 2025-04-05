import chromadb
from sentence_transformers import SentenceTransformer

# 初始化，建立chromadb的client
client = chromadb.Client()
# 選擇意使用的嵌入模型
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# 初始化collection(類似sql的資料表)，如果存在就直接使用，不存在就建立
collection_name = 'test'
collection = client.get_or_create_collection(collection_name)

# 要存入的內容(以list的方式)
memories = [
    "使用者說他喜歡貓咪。",
    "Agent 建議使用者可以養暹羅貓。",
    "使用者問了關於暹羅貓的餵養問題。",
    "Agent 回答了暹羅貓的餵養指南。",
    "使用者表示他考慮養一隻暹羅貓了。"
]

# 將內容轉換為向量
embeddings = embedding_model.encode(memories)
# 設置每個記憶的id
ids = [f"memory_{i}" for i in range(len(memories))]

# 將記憶存入collection，要存入的包含記憶的向量(embeddings.tolist())、記憶內容(documents=memories)、記憶id(ids=ids)
collection.add(embeddings=embeddings.tolist(),documents=memories, ids=ids)
print(f"已加入 {collection.count()} 個記憶到向量資料庫。")

# 查詢
query = '貓咪'
# 將查詢轉換為向量
query_embedding = embedding_model.encode(query)
# 查詢與記憶最相似的內容，query_embedding為查詢的向量，n_results為要查詢的數量
# 查詢結果為一個字典，包含documents(內容)、distances(距離)、ids(對應的id)
results = collection.query(query_embedding, n_results=2)
print("查詢結果:")
print(type(results))
print(results)
print(results["documents"][0])
documents = results["documents"][0]
distances = results["distances"][0]
for i in range(len(documents)):
    print(f"內容：{documents[i]}, 距離：{distances[i]}")
print(type(results["documents"]))
# 刪除collection
client.delete_collection(name=collection_name)