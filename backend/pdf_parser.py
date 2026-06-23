import pdfplumber


def extract_text_from_pdf(uploaded_file) -> str:
    """Extract readable text from an uploaded PDF resume."""

    extracted_text = []

    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    extracted_text.append(page_text)

        return "\n".join(extracted_text)

    except Exception as error:
        raise ValueError(f"Could not read the PDF file: {error}") from error