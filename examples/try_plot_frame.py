import sys
sys.path.append('../')

from DryTransfer.functions import plot_frame
from pylab import *

x = linspace(0,10,100)
plot( x, 3*sin(x) )
axis('equal')
axis('off')

plot_frame()

savefig( '../figures/try_plot_frame.svg', bbox_inches = 'tight' )
show()
