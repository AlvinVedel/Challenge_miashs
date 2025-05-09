# -*- coding: utf-8 -*-
"""Collemboles Analyses descriptives .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W_uk4zlMhdcbi4-aIL7BQQKgy88Fx0wR
"""

import pandas as pd
import os
from PIL import Image
import numpy as np
import plotly.express as px
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

labels_df = pd.read_csv('/content/drive/My Drive/Challenge DEEP/data/crops/raw_crops/labels.csv')
labels_df

X_train = []
Y_train = []

folder_path = '/content/drive/MyDrive/Challenge DEEP/data/crops/raw_crops/'

for index, row in labels_df.iterrows():
    image_name = row['img_name']
    labels = [row['label1'], row['label2'], row['label3'], row['label4']]

    image_path = os.path.join(folder_path, image_name)
    image = Image.open(image_path)
    image_np = np.array(image)
    X_train.append(image_np)

    for i, label in enumerate(labels):
        Y_train.append(int(label))

print(len(X_train))

print(len(Y_train))

"""# Labels"""

print("Valeurs uniques dans Y_train :", np.unique(Y_train))

value_counts = pd.Series(Y_train).value_counts().sort_index()
colors = ['#2f6632', '#b8d8b2', '#6d8f72', '#a9cfa3', '#3b5e4b', '#cfe8cd']

fig = px.bar(
    x=value_counts.index,
    y=value_counts.values,
    labels={'x': 'Valeur', 'y': 'Nombre d\'occurrences'},
    title="Distribution des labels dans le jeu d'entraînement",
    color=value_counts.index.astype(str),
    color_discrete_sequence=colors
)

fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family="Arial", color="black", size=16),
    title_font_size=22,
    title_x=0.5,
    showlegend=False
)

fig.show()

import numpy as np
import pandas as pd
import plotly.express as px


Y_quadruplets = [Y_train[i:i+4] for i in range(0, len(Y_train), 4)]
unique_counts = [len(np.unique(q)) for q in Y_quadruplets]

unique_distribution = pd.Series(unique_counts).value_counts().sort_index()

colors = ['#2f6632', '#b8d8b2', '#6d8f72', '#a9cfa3', '#3b5e4b', '#cfe8cd']


fig = px.bar(
    x=unique_distribution.index,
    y=unique_distribution.values,
    labels={'x': 'Nombre de valeurs uniques dans le quadruplet', 'y': 'Nombre d\'images'},
    title="Diversité des labels par image",
    color=unique_distribution.index.astype(str),
    color_discrete_sequence=colors
)

fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family="Arial", color="black", size=16),
    title_font_size=22,
    title_x=0.5,
    showlegend=False
)

fig.update_xaxes(
    tickmode='array',
    tickvals=[1, 2, 3, 4],
    ticktext=['1', '2', '3', '4']
)

fig.show()

Y_quadruplets = pd.DataFrame(Y_quadruplets)
quadruplet_counts = Y_quadruplets.value_counts().sort_values(ascending=False)

quadruplet_counts.head(10)

quadruplet_target = [8, 8, 8, 8]
nb_occurrences = sum(np.array_equal(q, quadruplet_target) for q in Y_quadruplets)

print(f"[8, 8, 8, 8] apparaît {nb_occurrences} fois.")

sns.heatmap(position_df.corr(), annot=True, cmap='Greens')

"""# Images"""

import plotly.express as px
import pandas as pd

# Extraire hauteur et largeur
dims = [(img.shape[0], img.shape[1]) for img in X_train]
df_dims = pd.DataFrame(dims, columns=["hauteur", "largeur"])

# Scatter plot
fig = px.scatter(
    df_dims,
    x="largeur", y="hauteur",
    title="Distributions des crops",
    labels={"largeur": "Largeur", "hauteur": "Hauteur"},
    opacity=0.8,
    color_discrete_sequence=['#2f6632']
)
fig.add_shape(
    type="rect",
    x0=0, x1=1250,
    y0=0, y1=1250,
    line=dict(color="green", width=0.5, dash="dot"),
    fillcolor="rgba(47, 102, 50, 0.1)",  # Vert forêt transparent
    layer="below"
)

fig.update_layout(
    title_x=0.5,
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family="Arial", color="black", size=16),
)

fig.show()