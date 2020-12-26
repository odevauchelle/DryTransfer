import sys
sys.path.append('../')
from inspect import *

from DryTransfer.templates import JFM as journal

from pylab import subplots, linspace, show, sin

fig, axs = subplots( nrows = 3, sharex = True )
x = linspace(-5,5,100)

for i, ax in enumerate(axs) :
    ax.plot(x,sin(i*x))

print(getmembers(journal,isfunction))

# journal.label_axes(ax)

show()
