import pandas as pd
import matplotlib
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



na_soloq = pd.read_csv('na_dataset.csv')
na_soloq['Blue Won'] = na_soloq['Blue Won']==1 #turning 'blue won' into a bool variable
na_soloq['Red Won'] = na_soloq['Blue Won']==0 #creating a 'red_won variable
na_soloq['avg_win_dif'] = na_soloq['Blue Winrates Avg'] - na_soloq['Red Winrates Avg'] #creating an 'avg_winrate-dif' variable
na_soloq.info()


sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

fig_1 = px.histogram(na_soloq, x='Blue Winrates Avg', title='Winrate distribution vs Win, for Blue',color='Blue Won')

fig_2 = px.histogram(na_soloq, x='Red Winrates Avg', title='Winrate distribution vs Win, for Red',color='Red Won')

fig_3 = px.scatter(na_soloq.sample(2000),title='Avg Winrates vs Avg Masteries.',x='Blue Winrates Avg',y='Blue Masteries Avg',color='Blue Won')

fig_4 = px.histogram(na_soloq, x='avg_win_dif', title='Winrate Diff vs Win, for Blue',color='Blue Won')

'''fig_1.show()
fig_2.show()
fig_3.show()
fig_4.show()'''


plt.title("Winrate distribution among teams")
sns.kdeplot(na_soloq,x= 'Red Winrates Avg', y = 'Blue Winrates Avg', fill=True, thresh=False);
plt.show()

plt.title("Boxplots of Avg Winrate for Red/Blue")
boxplot_1 = na_soloq.boxplot(column=['Red Winrates Avg', 'Blue Winrates Avg'])
plt.show()
plt.title("Boxplots of Avg Masteries for Red/Blue")
boxplot_2 = na_soloq.boxplot(column=['Red Masteries Avg', 'Blue Masteries Avg'])
plt.show()
