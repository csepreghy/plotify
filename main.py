import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from scipy import stats
from matplotlib import rcParams
import matplotlib.font_manager
import matplotlib.ticker as ticker

from plotify import Plotify

# age – a positive integer (years)
# FEV1 – a continuous valued measurement(liter)
# height – a continuous valued measurement(inches) 
# gender – binary(female: 0, male: 1)
# smoking status – binary(non-smoker: 0, smoker: 1) 
# weight – a continuous valued measurement(kg)

# Exercise 1: 
# - Divide data into smokers and non-smokers
# - Calculate the mean FEV1 score for both group

smoking_data = np.loadtxt('smoking.txt', delimiter="\t")

smokers = []
nonsmokers = []

for person in smoking_data:
  if person[4] == 0:
    nonsmokers.append(person)
  elif person[4] == 1:
    smokers.append(person)

print(np.array(smokers))
smokers = np.array(smokers)
nonsmokers = np.array(nonsmokers)

smokers_FEV1 = smokers[:,1]
nonsmokers_FEV1 = nonsmokers[:,1]

print('number of smoker FEV1 scores ' + str(len(smokers_FEV1)))
print('number of non-smoker FEV1 scores ' + str(len(nonsmokers_FEV1)))
 
smokers_avg_FEV1 = np.mean(smokers_FEV1)
nonsmokers_avg_FEV1 = np.mean(nonsmokers_FEV1)

print("Smokers' FEV1 score: ", str(smokers_avg_FEV1))
print("Non-smokers' FEV1 score: ", str(nonsmokers_avg_FEV1))

# Exercise 2

plotify = Plotify()

plotify.boxplot(
    data=[smokers_FEV1, nonsmokers_FEV1],
    labels=['Smokers', 'Non-smokers'],
    ylabel='FEV1 score',
    title='FEV1 scores for smokers\nand non-smokers'
)


# Exercise 3

variance_smokers = smokers_FEV1.var(ddof=1)
variance_nonsmokers = nonsmokers_FEV1.var(ddof=1)
print(variance_smokers)
print(variance_nonsmokers)

standard_deviation = np.sqrt((variance_smokers + variance_nonsmokers)/2)

print(standard_deviation)

# t = (smokers_FEV1.mean() - nonsmokers_FEV1.mean())/(standard_deviation*np.sqrt(2/N))

alpha = 0.05

t, p = stats.ttest_ind(smokers_FEV1, nonsmokers_FEV1, equal_var=False)

print('t is: ', t)
print('p is: ', p)

if p < alpha:
  print('Null hypothesis is rejected. The likeliness of it being true is: ' + str(p*100) + '%')

if p > alpha:
  print('Null hypothesis is acceoted.')

smokers_x = smokers[:,0]
smokers_y = smokers[:, 1]

nonsmokers_x = nonsmokers[:, 0]
nonsmokers_y = nonsmokers[:, 1]

plotify.scatter_plot(
    x_list=[nonsmokers_x, smokers_x],
    y_list=[nonsmokers_y, smokers_y],
  linewidth = 0.25,
  alpha = 0.5,
  xlabel = 'Age',
  ylabel = 'FEV1 score',
  title='FEV1 scores among different agegroups',
  legend_labels = ('Non-smokers', 'Smokers')
)

# Exercise 5

plotify.histogram(
  x_list = [nonsmokers_x, smokers_x],
  ylabel = 'Number of People',
  xlabel = 'Age',
  title = 'Numbeer of datapoints in different agegroups',
  labels = ('Non-smokers', 'Smokers')
)
