# plotify
A simple class to give plots some styling. It is a very light skin over `matplotlib.pyplot`.

Once you have `plotify.py` in your root directory:
```
from plotify import Plotify

plotify = Plotify()
```

Then use the available methods. So far we have `boxplot()`, `scatter_plot`, `histogram`.

## Examples

A few examples using the Plotify class

### Boxplot

```
plotify.boxplot(
  data=[smokers_FEV1, nonsmokers_FEV1],
  labels=['Smokers', 'Non-smokers'],
  ylabel='FEV1 score',
  title='FEV1 scores for smokers\nand non-smokers'
)
```
<img src="https://raw.githubusercontent.com/csepreghy/plotify/master/examples_img/boxplot.png" width="600px" />

### Scatter Plot

```
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
```
<img src="https://raw.githubusercontent.com/csepreghy/plotify/master/examples_img/scatterplot.png" width="600px" />

### Histogram

```
plotify.histogram(
  x_list = [nonsmokers_x, smokers_x],
  ylabel = 'Number of People',
  xlabel = 'Age',
  title = 'Numbeer of datapoints in different agegroups',
  labels = ('Non-smokers', 'Smokers')
)
```
<img src="https://raw.githubusercontent.com/csepreghy/plotify/master/examples_img/scatterplot.png" width="600px" />
