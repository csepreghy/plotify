import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from scipy import stats
from matplotlib import rcParams
import matplotlib.font_manager
import matplotlib.ticker as ticker

from pyplotify.__init__ import Plotify

# Data preprocessing

smoking_data = np.loadtxt('smoking.txt', delimiter="\t")

smokers = []
nonsmokers = []

for person in smoking_data:
  if person[4] == 0:
    nonsmokers.append(person)
  elif person[4] == 1:
    smokers.append(person)

smokers = np.array(smokers)
nonsmokers = np.array(nonsmokers)

smokers_FEV1 = smokers[:,1]
nonsmokers_FEV1 = nonsmokers[:,1]

# Initialize plotify

plotify = Plotify()

# Boxplot

plotify.boxplot(
  data=[smokers_FEV1, nonsmokers_FEV1],
  labels=['Smokers', 'Non-smokers'],
  ylabel='FEV1 score',
  title='FEV1 scores for smokers\nand non-smokers'
)

# Scatter plot

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

# Histogram

plotify.histogram(
  x_list = [nonsmokers_x, smokers_x],
  ylabel = 'Number of People',
  xlabel = 'Age',
  title = 'Numbeer of datapoints in different agegroups',
  labels = ('Non-smokers', 'Smokers')
)
