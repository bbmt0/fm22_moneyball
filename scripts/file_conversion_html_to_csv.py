import pandas as pd
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

def select_files():
    """Ouvre une boîte de dialogue pour sélectionner plusieurs fichiers HTML."""
    Tk().withdraw()  # Empêche l'apparition de la fenêtre principale Tkinter
    current_directory = os.getcwd()
    filenames = askopenfilenames(initialdir=current_directory, filetypes=[("HTML files", "*.html")])
    return filenames

def convert_html_to_csv(filename, output_dir='../data/raw/'):
    """Convertit un fichier HTML en CSV et le sauvegarde dans le répertoire spécifié."""
    df_list = pd.read_html(filename, encoding='utf-8')
    df = df_list[0]
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(filename))[0]
    csv_path = os.path.join(output_dir, f'{base_name}_initial_data.csv')
    df.to_csv(csv_path, index=False)
    return csv_path

if __name__ == "__main__":
    filenames = select_files()
    if filenames:
        for filename in filenames:
            csv_path = convert_html_to_csv(filename)
            print(f"Fichier converti en CSV: {csv_path}")
    else:
        print('Aucun fichier sélectionné')
