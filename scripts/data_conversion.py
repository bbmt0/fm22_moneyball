import pandas as pd
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def select_file():
    """Ouvre une boîte de dialogue pour sélectionner un fichier HTML."""
    Tk().withdraw()  # Empêche l'apparition de la fenêtre principale Tkinter
    current_directory = os.getcwd()
    filename = askopenfilename(initialdir=current_directory, filetypes=[("HTML files", "*.html")])
    return filename

def convert_html_to_csv(filename, output_dir='../data/raw/'):
    """Convertit un fichier HTML en CSV et le sauvegarde dans le répertoire spécifié."""
    df_list = pd.read_html(filename, encoding='utf-8')
    df = df_list[0]
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, 'initial_data.csv')
    df.to_csv(csv_path, index=False)
    return csv_path

if __name__ == "__main__":
    filename = select_file()
    if filename:
        csv_path = convert_html_to_csv(filename)
        print(f"Fichier converti en CSV: {csv_path}")
    else:
        print('Aucun fichier sélectionné')
