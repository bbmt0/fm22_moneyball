import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(input_csv):
    """Analyse les données pour extraire des insights spécifiques."""
    df = pd.read_csv(input_csv)

    # Ajouter un filtre sur les positions
    positions_to_analyze = ["Attaquant", "Milieu Offensif"]
    df_filtered = df[df['Position'].isin(positions_to_analyze)]

    # Calculer l'overperformance des buteurs
    df_filtered['Overperformance_Gls_xG'] = df_filtered['Goals'] - df_filtered['xG']

    # Sélectionner les 15 premières overperformances
    top_overperformers = df_filtered.nlargest(15, 'Overperformance_Gls_xG')

    # Filtrer par salaire
    top_overperformers = top_overperformers[top_overperformers['Wage'] <= 50000]

    # Scatter plot avec overperformance en X et salaire en Y
    plt.figure(figsize=(14, 10))

    # Taille des points en fonction de l'âge
    age_factor = (top_overperformers['Age'].max() - top_overperformers['Age']) + 10
    plt.scatter(top_overperformers['Overperformance_Gls_xG'], top_overperformers['Wage'], 
                s=age_factor * 10, color='blue', alpha=0.6)

    # Ajouter les noms des joueurs et leurs ligues
    for i in range(len(top_overperformers)):
        player_name = top_overperformers.iloc[i]['Name']
        league_name = top_overperformers.iloc[i]['Division']
        age = top_overperformers.iloc[i]['Age']
        x = top_overperformers.iloc[i]['Overperformance_Gls_xG']
        y = top_overperformers.iloc[i]['Wage']
        
        plt.annotate(f"{age}", (x, y), textcoords="offset points", 
                     xytext=(0, 0), ha='center', va='center', fontsize=9, color='white', weight='bold')

        plt.annotate(f"{player_name} ({league_name})", (x, y), textcoords="offset points", 
                     xytext=(0, 10), ha='center', fontsize=8)

    plt.xlabel('Overperformance (Gls - xG)')
    plt.ylabel('Salary (Wage)')
    plt.title('Top 15 Overperforming Players: Overperformance vs Salary (Sized by Age)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    input_csv = '../data/processed/cleaned_data.csv'
    analyze_data(input_csv)
