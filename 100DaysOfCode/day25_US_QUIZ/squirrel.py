# task : count squirrel with same color

import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
serie = data['Primary Fur Color']
colors = {"Gray": 0,
          "Cinnamon": 0,
          "Black": 0,
          "others": 0}

for value in serie.values:
    if value == 'Gray':
        colors['Gray'] += 1

    elif value == 'Cinnamon':
        colors['Cinnamon'] += 1

    elif value == 'Black':
        colors['Black'] += 1
    else:
        colors["others"] += 1

new_data = pd.DataFrame(colors, index=[1])
new_data.to_csv("squirrel_color.csv")
