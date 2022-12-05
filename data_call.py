import pandas as pd
import matplotlib
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



na_soloq = pd.read_csv('na_dataset.csv')
na_soloq['Blue Won'] = na_soloq['Blue Won']==1
na_soloq['Red Won'] = na_soloq['Blue Won']==0
na_soloq['winr_diff'] = na_soloq['Blue Winrates Avg'] - na_soloq['Red Winrates Avg']
na_soloq.info()


sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

fig = px.histogram(na_soloq, x='Blue Winrates Avg', title='Winrate vs Win, for Blue',color='Blue Won')
fig.show()


fig = px.histogram(na_soloq, x='Red Winrates Avg', title='Winrate vs Win, for Red',color='Red Won')
fig.show()


fig = px.scatter(na_soloq.sample(2000),title='Avg Winrates. vs Avg Masteries.',x='Blue Winrates Avg',y='Blue Masteries Avg',color='Blue Won')
fig.show()


fig = px.histogram(na_soloq, x='winr_diff', title='Winrate Diff vs Win, for Blue',color='Blue Won')
fig.show()
