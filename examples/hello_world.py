import sys
sys.path.append('../')

from DryTransfer import JFM as journal

from pylab import *

fig, axs = subplots( nrows = 3, sharex = True )
x = linspace(-5,5,100)

for i, ax in enumerate(axs) :
    ax.plot( x, sin( i*x ) )

# axs[0].set_title( journal.full_name )

journal.label_axes()

savefig( '../figures/hello_world.svg', bbox_inches = 'tight' )

show()
