import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import json

# Setting up global variables
file_path = './data/house_data.csv'
model_file_name = './data/rowhouse_model.pickle'


def load_model():
    print("Model loading")
    model = pickle.load(open(model_file_name, 'rb'))
    return model


def save_model(lm):
    pickle.dump(lm, open(model_file_name, 'wb'))
    print("Model saved!")


def train_model(df):
    x = df[['Year build', 'Ejerudgift', 'Enhedsareal', 'Værelser',
            'Antal toiletter', 'Antal badeværelser', 'Grundstørrelse']]
    y = df['Pris']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    lm = LinearRegression()
    lm.fit(x_train, y_train)

    save_model(lm)
    return lm, x_train, x_test, y_train, y_test


def read_and_clean_data():
    df = pd.read_csv(file_path)
    df = df[df['Type'] == 'Rækkehus']

    df.drop([
        'Vejareal',
        'Adresse',
        'Lands ejerlav kode',
        'Kommunal ejerlav kode',
        'Energimærke',
        'Ydervæg',
        'Tag',
        'Etager',
        'Ejendomsnummer',
        'Primær matrikel',
        'Lands ejerlav navn',
        'Kommunal ejerlav navn',
        'Matrikelnummer',
        'Afvigende etager',
        'Boligstørrelse tinglyst',
        'Objekt status',
        'Boligstørrelse BBR',
        'Bygningsnummer',
        'Beboelsesareal',
        'URL',
        'Boligydelse',
        'Anvendelse',
        'Type',
        'Boligstørrelse',
        'Energikode',
        'Carport',
        'Udhus',
        'Boligenhed med eget køkken',
        'Boligenhed uden eget køkken',
        'Boligtype',
        'Badeforhold',
        'Varmeinstallation',
        'Seneste ombygning',
        'Køkkenforhold',
        'Toiletforhold',
        'Ejendomsværdiskat',
        'Grundskyld'
    ], 'columns', inplace=True)

    # format some values from objects to floats
    df['Year build'] = pd.to_numeric(df['Year build'], errors='coerce')
    df['Pris'] = pd.to_numeric(df['Pris'], errors='coerce')
    df['Ejerudgift'] = pd.to_numeric(df['Ejerudgift'], errors='coerce')
    df['Enhedsareal'] = pd.to_numeric(df['Enhedsareal'], errors='coerce')

    # remove data with abnormal feature values
    df = df[df['Enhedsareal'] < 300]
    df = df[df['Værelser'] < 10]
    df = df[df['Antal toiletter'] <= 3]
    df = df[df['Antal badeværelser'] <= 3]
    df = df[df['Grundstørrelse'] < 1500]
    df = df[(df['Year build'] > 1850) & (df['Year build'] < 2020)]

    # remove data with abnormal target value
    df = df[df['Pris'] < 6000000]

    # find missing values in the data and drop those rows:
    df = df.dropna()

    return df
