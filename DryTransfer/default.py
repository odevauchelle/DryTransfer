from pylab import array
import matplotlib as mpl
from scipy.constants import golden

from .functions.plot_frame import plot_frame
from .functions.label_axes import label_axes
from .functions.miscellaneous import *

####################
#
# constants
#
####################

inches_per_cm = 0.3937

####################
#
#   Reset Matplotlib rcParams
#
####################

print('DryTransfer resetting Matplotlib rcParams.')
from matplotlib import rcParams, rcParamsDefault
rcParams.update( rcParamsDefault ) # reset

####################
#
#   Template name
#
####################

name = 'default'
full_name = 'Generic style'
url = ''

####################
#
#   Figure size
#
####################

page_width = 16.3 # cm
page_width = page_width*0.3937 # inches

regular_figure_width = 0.75*page_width
large_figure_width = .99*page_width

regular_aspect_ratio = 1/golden

regular_figure_size = array( [ 1, regular_aspect_ratio ] )*regular_figure_width
large_figure_size = array( [ 1, regular_aspect_ratio ] )*large_figure_width

####################
#
#   Matplotlib rcParms
#
####################

mpl.rcParams['figure.figsize'] = regular_figure_size

####################
#
#   Try it out
#
####################

if __name__ == '__main__' :

    from pylab import subplots, linspace, show, sin

    fig, axs = subplots( nrows = 3, sharex = True )
    x = linspace(-5,5,100)

    for i, ax in enumerate(axs) :
        ax.plot(x,sin(i*x))

    show()
