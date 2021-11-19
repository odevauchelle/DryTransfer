
from .default import *

####################
#
#   Template name
#
####################

name = 'PNAS'
full_name = 'Proceedings of the National Academy of Sciences of the United States of America'
url = r'https://www.pnas.org/authors/submitting-your-manuscript#latex'
####################
#
#   Figure size
#
####################

regular_figure_width = 8.5 # cm
regular_figure_width *= 0.3937 # inches

page_width = 17.5 # cm
page_width *= 0.3937 # inches

large_figure_width = page_width

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
