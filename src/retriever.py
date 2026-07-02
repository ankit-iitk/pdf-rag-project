import faiss
import numpy as np


class Retriever:

    def __init__(self, index, chunks, embedding_model):
        self.index = index
        self.chunks = chunks
        self.embedding_model = embedding_model

    def search(self, query, top_k=3):

        query_embedding = self.embedding_model.model.encode(
            [query],
            convert_to_numpy=True
        ).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []

        for idx in indices[0]:
            results.append(self.chunks[idx])

        return results