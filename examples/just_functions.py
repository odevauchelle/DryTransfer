import sys
sys.path.append('../')

from DryTransfer.functions import *

from pylab import subplots, show, angle, meshgrid, linspace, sqrt

fig, axs = subplots( nrows = 2, ncols = 2 )

x = linspace(-1,1,50)
x, y = meshgrid( x, x )
z = x + 1j*y

for i, ax in enumerate( axs.flatten() ) :
    ax.contourf( x, y, angle( sqrt( z**i - .1*z + .3 ) ) )

label_axes()
plot_frame( axs[0,0], arrow_length = .5 )

show()
