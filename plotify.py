from matplotlib import rcParams
import matplotlib.font_manager
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np

class Plotify:
  def __init__(self):
    # Basic configuration
    self.use_grid = True
    rcParams['font.sans-serif'] = ['Arial']
    plt.style.use('dark_background')

    # Color Constants
    self.background_color = '#1C2024'
    self.grid_color = '#444444'
    self.legend_color = '#282D33'
    self.c_cyan = '#4FB99F'
    self.c_orange = '#F2B134'
    self.c_red = '#ED553B'
    self.c_white = '#FFFFFF'

    self.plot_colors = [self.c_cyan, self.c_orange, self.c_red]

  def boxplot(self, data, labels, title, ylabel):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(self.background_color)
    ax.set_facecolor(self.background_color)

    bplot = ax.boxplot(
      data,
      vert=True,
      patch_artist=True,
      labels=labels,
      boxprops=dict(facecolor=self.c_white, color=self.c_white),
      capprops=dict(color=self.c_white),
      whiskerprops=dict(color=self.c_white),
      flierprops=dict(markeredgecolor=self.c_white),
      medianprops=dict(color=self.c_white)
    )

    for patch, color in zip(bplot['boxes'], self.plot_colors):
        patch.set_facecolor(color)

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend((bplot['boxes']), labels, loc=2, facecolor=self.legend_color)

    plt.subplots_adjust(top=0.85)
    plt.grid(self.use_grid, color=self.grid_color)

    plt.show()
  
  def scatter_plot(
    self,
    x_list,
    y_list,
    linewidth = 0.5,
    alpha = 1,
    xlabel = 'X label',
    ylabel = 'Y label',
    title = 'Title',
    legend_labels = ('Men', 'Women')
  ):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(self.background_color)
    ax.set_facecolor(self.background_color)

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

    for i, x in enumerate(x_list):
      ax.scatter(
        x,
        y_list[i],
        linewidths = linewidth,
        alpha=alpha,
        c=self.plot_colors[i]
      )

    ax.grid(self.use_grid, color=self.grid_color)

    ax.legend(legend_labels, facecolor=self.legend_color)
    plt.show()

  def histogram(
    self,
    x_list,
    ylabel = 'Y label',
    xlabel = 'X label',
    title = 'Title',
    labels = ('Label 1', 'Label 2')
  ):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(self.background_color)
    ax.set_facecolor(self.background_color)
    ax.grid(self.use_grid, color=self.grid_color)

    for i, x in enumerate(x_list):
      ax.hist(x, int(np.max(x) - np.min(x)), facecolor=self.plot_colors[i])

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.legend(labels, facecolor=self.legend_color)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

    plt.show()
