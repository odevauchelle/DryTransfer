from matplotlib.pyplot import gcf, gca
from pylab import mean, array, norm
from matplotlib.pyplot import rcParams

###################################
#
# PLOT FRAME
#
###################################

_plot_frame_default_style = dict(
    textcoords = 'data',
    xycoords = 'data',
    va = "center",
    ha = "center",
    arrowprops = dict( arrowstyle = "<-", shrinkB = 0, shrinkA = 0, patchA = 0 ),
    )

_default_origin_markers = [
        dict( marker = '.', ms = 5 ),
        dict( mfc = 'none', marker = 'o', ms = 7 )
        ]

def plot_frame( ax = None, center = ( 0., 0. ), arrow_length = 1., letters = ( 'x', 'y' ), color = 'k', origin_marker = None, z_offset = None, orientation = 1,**kwargs ) :

    '''
    Draws a two-dimensional reference frame.

    Arguments
    ---------
    ax : Matplotlib axes
        Axes on which to draw reference frame (optional)
    arrow_length : float or list
        Length of frame arrows
    color : str or tuple
        Axis names color
    center : tuple
        Position of origin
    letters : list
        Name of axis
    orientation : 1 or -1
        Left or right
    text_offset : float
        Distance of third label from origin (in points)
    origin_marker : list
        Markers denoting origin
    kwargs : dict
        Passed to matplotlib.annotate (overrides color argument)
    '''

    if ax is None :
        ax = gca()

    if z_offset is None :

        try :
            z_offset = kwargs['fontsize']
        except :
            z_offset = rcParams['font.size']

    annotate_kwargs = _plot_frame_default_style.copy()
    annotate_kwargs['arrowprops']['color'] = color
    annotate_kwargs['color'] = color
    annotate_kwargs.update( kwargs )

    try :
        arrow_length[0]
    except :
        arrow_length = 2*[ arrow_length ]

    if origin_marker is None :
        try :
            letters[2]
            origin_marker = _default_origin_markers
        except :
            origin_marker = []
    else :
        try :
            if origin_marker :
                origin_marker = _default_origin_markers
            else :
                origin_marker = []
        except :
            pass

    xytext = [ ( center[0], center[1] + orientation*arrow_length[1] ), ( center[0] + arrow_length[0], center[1]  ) ]
    xy = [ center ]*2

    xytext += [ -mean( array( xytext ), axis = 0 ) ]
    xy += [ center ]

    for i, letter in enumerate( letters ) :

        direction = array( xytext[i] ) - array( xy[i] )
        direction *= z_offset/norm( direction )

        ghost_annotate_kwargs = annotate_kwargs.copy()
        ghost_annotate_kwargs.update( arrowprops = None, textcoords = 'offset points' )

        if i < 2 :
            ax.annotate( '', xy = xy[i], xytext = xytext[i], **annotate_kwargs ) # arrow, two annotate calls for exact arrow length
            ghost_xy = xytext[i]
        else :
            ghost_xy = center

        ax.annotate( letter, xy = ghost_xy, xytext = direction, **ghost_annotate_kwargs ) # arrow label


    for marker_style in origin_marker :
        ax.plot( *center, color = color, **marker_style )


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
    axis('off')
    plot_frame( arrow_length = .3, color = 'm', letters = ('x', 'y', 'z') )

    show()
