import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
#import seaborn as sns
#import matplotlib.pyplot as plt
#import numpy as np

def select_file():
    Tk().withdraw()
    current_directory = os.getcwd()
    filename = askopenfilename(initialdir=current_directory, filetypes=[("HTML files", "*.html")])
    return filename

def convert_html_to_csv(filename):
    df_list = pd.read_html(filename, encoding='utf-8')
    df = df_list[0]
    df.to_csv('initial_data.csv', index=False)

def clean_data():
    df = pd.read_csv('initial_data.csv', encoding='utf-8-sig')
    df['Club'] = df.apply(lambda row: row['Club'].replace(f" - {row['Division']}", ""), axis=1)
    drop_columns(df)
    rename_columns(df)
    return df

def drop_columns(df):
    columns_to_drop = ['Inf', 'Personality', 'Transfer Value', 'Rec']
    df.drop(columns=columns_to_drop, inplace=True)


def rename_columns(df):
    column_mapping = {
        'UID': 'ID', 'Inf': 'Inf', 'Name': 'Name', 'Personality': 'Personality', 'Nat': 'Nat',
        'Age': 'Age', 'Position': 'Position', 'Club': 'Club', 'Division': 'Division', 'Av Rat': 'Rating',
        'Wage': 'Wage', 'Expires': 'Contract Exp', 'Transfer Value': 'Transfer Value', 'Rec': 'Coach Recommendation',
        'Apps': 'Apps', 'Gls': 'Goals', 'CCC': 'Clear Cut Chances', 'Ch C/90': 'Chances Created/90',
        'Mins/Gl': 'Minutes per Goal', 'Gls/90': 'Goals/90', 'xG': 'Expected Goals', 'Shot %': 'Shot Accuracy %', 
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
    df.rename(columns=column_mapping, inplace=True)
    return df

filename = select_file()

if filename:
    convert_html_to_csv(filename)
    df = clean_data()
    print(df.columns) 
    df.to_csv('cleaned_data.csv', index=False, encoding='utf-8-sig')



    
else: 
    print('No file selected')


#load the centra_midfid.html html file and convert it to a csv file

# Load the data
#df = pd.read_csv('france_mc.csv')

# # Offensive metrics
# df['Buts/90'] = round((df['Buts'] / df['Min.']) * 90, 3)
# df['xG/90'] = round((df['xG'] / df['Min.']) * 90, 3)
# df['goals_overperf'] = round(df['Buts/90'] - df['xG/90'], 3)
# df['kp_per_attemptedp'] = round(df['PCl/90'] / df['Ps T/90'], 3)
# df['passes_efficency'] = round((df['PCl/90'] * df['% passes']) / df['Ps T/90'], 3)
# df['kp_per_accuracy'] = round(((df['PCl/90'] / df['% passes']) / df['Min.']) * 90, 3)

# # New creativity metrics
# df['key_passes_90'] = round((df['PCl/90'] * 90), 3)
# df['chances_created_90'] = round((df['Occ. / 90 min.'] * 90), 3)
# df['successful_dribbles_90'] = round((df['Drb/90'] * 90), 3)

# Percentiles ranking
# metrics_to_rank = ['Buts/90', 'xG/90', 'goals_overperf', 'kp_per_attemptedp', 
#                    'passes_efficency', 'kp_per_accuracy', 'key_passes_90', 
#                    'chances_created_90', 'successful_dribbles_90']

# for metric in metrics_to_rank:
#     df[f'{metric}_percentile'] = round(df[metric].rank(pct=True), 3)

# # Define weights for each creativity-related metric
# weights = {
#     'key_passes_90_percentile': 0.4,
#     'chances_created_90_percentile': 0.4,
# 'successful_dribbles_90_percentile': 0.1,
#     'passes_efficency_percentile': 0.1
# }

# # Calculate creativity index
# df['creativity_index'] = (
#     df['key_passes_90_percentile'] * weights['key_passes_90_percentile'] +
#     df['chances_created_90_percentile'] * weights['chances_created_90_percentile'] +
# df['successful_dribbles_90_percentile'] * weights['successful_dribbles_90_percentile'] +
#     df['passes_efficency_percentile'] * weights['passes_efficency_percentile']
# )

# # Sort by creativity index
# df_sorted = df.sort_values(by='creativity_index', ascending=False)

# # Export to csv
# df_sorted.to_csv('creative_midfielders_index.csv', index=False)

