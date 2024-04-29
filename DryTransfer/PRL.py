
from .default import *

####################
#
#   Template name
#
####################

name = 'PRL'
full_name = 'Physical Review Letters'
url = r'https://journals.aps.org/prl/authors'

####################
#
#   Figure size
#
####################

regular_figure_width = 8.6 # cm, https://journals.aps.org/prl/authors
regular_figure_width *= 0.3937 # inches
regular_figure_width *= 1.3 # finer lines, smaller font

page_width = 2*regular_figure_width

large_figure_width = 2*regular_figure_width

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
