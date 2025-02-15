import pypdf # biblioteca para manipulação de PDFs

def extract_text_from_pdf(pdf_file):
    """
    Função para extrair o texto de um pdf carregado no Streamlit.

    Parâmetros:
    pdf_file (UploadedFile): Ariquivo PDF carregado pelo usúario.

    Retorna:
    str: Texto extraido do PDF.
    """
    
    reader = pypdf.PdfReader(pdf_file) # Cria um objeto para ler o PDF

    # Percorre todas as paginas e extrai o texto disponivel
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text # Retorna o texto extraido