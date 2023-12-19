from matplotlib.pyplot import gcf, gca
from pylab import mean, array, norm, sqrt
from matplotlib.pyplot import rcParams

###################################
#
# LENGTH ARROW
#
###################################

_arrow_default_style = dict(
    textcoords = 'data',
    xycoords = 'data',
    va = "center",
    ha = "center",
    arrowprops = dict( arrowstyle = "->", shrinkB = 0, shrinkA = 0, patchA = 0 ),
    )

_text_default_style = dict(
    ha = 'center',
    va = 'center'
)

def length_arrow( points, label = '', ax = None, arrow_style = None, text_style = None, relative_text_space = .1, **kwargs ) :

    if ax is None :
        ax = gca()

    if arrow_style is None :
        arrow_style = _arrow_default_style

    arrow_style['arrowprops'].update( kwargs )

    if text_style is None :
        text_style = _text_default_style

    center = mean( array( points ), axis = 0 )
    ax.text( *center, label, **text_style  )

    for end in points :
        start = center + ( array(end) - center )*relative_text_space
        ax.annotate( '', end, start , **arrow_style )

###################################
#
# try it out
#
###################################

if __name__ == '__main__' :

    from pylab import linspace, plot, axis, cos, show

    x = linspace(0,1,100)
    plot(x, .5*cos( 20*x**2 ))
    axis('equal')
    # axis('off')

    length_arrow( [(0,-.3),(0,.3)], 'toto' )
    # plot_frame( arrow_length = .3, color = 'm', letters = ('x', 'y', 'z') )

    show()
