# plotify
A simple class to give plots some styling.

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
