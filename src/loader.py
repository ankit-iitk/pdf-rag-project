import pdfplumber


def load_documents(uploaded_files):
    """
    Extract text from uploaded PDF files.
    """

    documents = []

    for uploaded_file in uploaded_files:

        with pdfplumber.open(uploaded_file) as pdf:

            for page_number, page in enumerate(pdf.pages, start=1):

                text = page.extract_text()

                if text:

                    documents.append({
                        "file": uploaded_file.name,
                        "page": page_number,
                        "text": text
                    })

    return documents