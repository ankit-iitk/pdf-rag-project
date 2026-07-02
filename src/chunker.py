def create_chunks(documents, chunk_size=500, overlap=100):
    """
    Split extracted text into overlapping chunks.
    """

    chunks = []

    step = chunk_size - overlap

    for doc in documents:

        text = doc["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            chunks.append(
                {
                    "text": chunk_text,
                    "file": doc["file"],
                    "page": doc["page"]
                }
            )

            start += step

    return chunks