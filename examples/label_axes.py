import sys
sys.path.append('../')

from DryTransfer.functions import label_axes

from pylab import *

fig, axs = subplots( nrows = 2, ncols = 2 )

x = linspace(-1,1,50)
x, y = meshgrid( x, x )
z = x + 1j*y

for i, ax in enumerate( axs.flatten() ) :
    ax.contourf( x, y, angle( sqrt( z**i - .1*z + .3 ) ) )
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])


label_axes()
savefig( '../figures/try_label_axes.svg', bbox_inches = 'tight' )

show()
