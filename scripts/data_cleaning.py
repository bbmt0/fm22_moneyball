import pandas as pd
import os

def clean_data(input_csv, output_csv='../data/processed/cleaned_data.csv'):
    """Nettoie les données et les enregistre dans un nouveau fichier CSV."""
    df = pd.read_csv(input_csv, encoding='utf-8-sig')


    # Remplacer les "-" par des 0
    df = df.applymap(lambda x: 0 if x == '-' else x)

    # Remplacer les "" par des 0
    df = df.applymap(lambda x: 0 if x == '' else x)


    if 'Mins' in df.columns:
        df['Mins'] = df['Mins'].astype(str)  # Convertir en chaîne pour manipulation
        df['Mins'] = df['Mins'].str.replace(',', '', regex=False)  # Supprimer les virgules
        df['Mins'] = df['Mins'].str.replace('.', '', regex=False)  # Supprimer les points
        df['Mins'] = df['Mins'].astype(int)  # Convertir en int
    
    # Nettoyer la colonne "Wage"
    if 'Wage' in df.columns:
        df['Wage'] = df['Wage'].astype(str)  # Convertir en chaîne pour manipulation
        df['Wage'] = df['Wage'].str.replace('€', '', regex=False)  # Supprimer le symbole €
        df['Wage'] = df['Wage'].str.replace(' p/w', '', regex=False)  # Supprimer le suffixe p/w
        df['Wage'] = df['Wage'].str.replace('.', '', regex=False)  # Supprimer les points de milliers
        df['Wage'] = df['Wage'].str.replace(',', '.', regex=False)  # Remplacer les virgules par des points décimaux
        df['Wage'] = pd.to_numeric(df['Wage'], errors='coerce')

    if 'Name' in df.columns:
        df['Name'] = df['Name'].apply(lambda x: x.split(' - ')[0] if pd.notna(x) and ' - ' in x else x)


    # Transformer les pourcentages (%) en fractions (0.00)
    df = convert_percentages(df)

    # Nettoyer les valeurs de distance
    df['Dist/90'] = df['Dist/90'].str.replace('km', '').astype(float)

    # Supprimer la division du nom de club
    df['Club'] = df.apply(lambda row: row['Club'].replace(f" - {row['Division']}", ""), axis=1)
    
    df = drop_columns(df)
    df = rename_columns(df)
    
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"Fichier nettoyé sauvegardé: {output_csv}")
    return df

def convert_percentages(df):
    """Convertit les colonnes contenant des pourcentages en valeurs décimales."""
    for column in df.columns:
        if df[column].dtype == 'object':
            if df[column].str.contains('%').any():
                df[column] = df[column].str.replace('%', '')
                try:
                    df[column] = df[column].astype(float) / 100.0
                except ValueError:
                    print(f"Impossible de convertir la colonne {column} en float.")
    return df

def drop_columns(df):
    columns_to_drop = ['Inf', 'Personality', 'Transfer Value', 'Rec']
    return df.drop(columns=columns_to_drop)

def rename_columns(df):
    column_mapping = {
        'UID': 'ID', 'Name': 'Name', 'Nat': 'Nationality', 'Age': 'Age', 'Position': 'Position',
        'Club': 'Club', 'Division': 'Division', 'Av Rat': 'Rating', 'Wage': 'Wage', 'Expires': 'Contract Expiration',
        'Apps': 'Appearances', 'Gls': 'Goals', 'CCC': 'Clear Cut Chances', 'Ch C/90': 'Chances Created/90',
        'Mins/Gl': 'Minutes per Goal', 'Gls/90': 'Goals/90', 'xG': 'xG', 'Shot %': 'Shot Accuracy %', 
        'Shot/90': 'Shots/90', 'ShT/90': 'Shots on Target/90', 'Ast': 'Assists', 'Asts/90': 'Assists/90', 
        'K Ps/90': 'Key Passes/90', 'Pas A': 'Passes Attempted', 'Ps A/90': 'Passes Attempted/90', 
        'Ps C/90': 'Passes Completed/90', 'Pas %': 'Pass Completion %', 'Cr A': 'Crosses Attempted', 
        'Cr C': 'Crosses Completed', 'Cr C/A': 'Crosses Completed/Attempted', 'Drb': 'Dribbles', 
        'Drb/90': 'Dribbles/90', 'Itc': 'Interceptions', 'Int/90': 'Interceptions/90', 'K Tck': 'Key Tackles', 
        'Tck': 'Tackles', 'Tck R': 'Tackle Success Rate', 'Hdrs': 'Headers Won', 'Hdrs W/90': 'Headers Won/90', 
        'Aer A/90': 'Aerial Duels/90', 'Hdrs A': 'Aerial Duels', 'Hdr %': 'Header Success %', 'Fls': 'Fouls', 
        'Gl Mst': 'Errors Leading to Goal', 'Yel': 'Yellow Cards', 'Red': 'Red Cards', 'Dist/90': 'Distance Covered/90', 
        'PoM': 'Man of the Match', 'Mins': 'Minutes'
    }
    return df.rename(columns=column_mapping)

if __name__ == "__main__":
    input_csv = '../data/raw/initial_data.csv'
    df = clean_data(input_csv)
    print(df.columns)
