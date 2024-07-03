import pdfkit
def convert_url_to_pdf(url, output_pdf):
    options = {
        'enable-javascript': '',
        'javascript-delay': 5000, 
        'load-error-handling': 'ignore',
        'custom-header': [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        ] 
    }
    try:
        pdfkit.from_url(url, output_pdf, options=options)
        print(f"Le fichier PDF a été créé avec succès : {output_pdf}")
    except Exception as e:
        print(f"Erreur lors de la conversion de l'URL en PDF : {e}")

url = "https://www.demandelogement44.fr/imhowebGP44/44/espace_public/statistique/afficherFormulaire/commune/109/quartier/8?pageCmsDemande=0"
output_pdf = 'output.pdf'
convert_url_to_pdf(url, output_pdf)