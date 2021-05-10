
from .default import *

####################
#
#   Template name
#
####################

name = 'JFM'
full_name = 'Journal of Fluid Mechanics'
url = r'https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/information/instructions-contributors'

####################
#
#   Figure size
#
####################

page_width = 16.3 # cm
page_width = page_width*inches_per_cm # inches

regular_figure_width = 0.75*page_width
large_figure_width = .99*page_width

regular_figure_size = array( [ 1, regular_aspect_ratio ] )*regular_figure_width
large_figure_size = array( [ 1, regular_aspect_ratio ] )*large_figure_width

graphical_abstract_figure_size = array([6,5]) # cm
graphical_abstract_figure_size = graphical_abstract_figure_size*inches_per_cm # inches


####################
#
#   Resolution
#
####################

graphical_abstract_dpi = 300

####################
#
#   Matplotlib rcParms
#
####################

mpl.rcParams['figure.figsize'] = regular_figure_size
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['text.usetex'] = True

###################

#  label_axes parameters

###################

default_label_axes = label_axes

def label_axes( *args, **kwargs ) :

    label_axes_kwargs = dict(
        label = lambda i: '(' + 'abcdefghijklmnopqrstuvwxyz'[i] + ')',
        bbox = None
        )

    label_axes_kwargs.update( kwargs )

    return default_label_axes( *args, **label_axes_kwargs )

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
