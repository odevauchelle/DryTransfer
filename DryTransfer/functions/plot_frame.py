from matplotlib.pyplot import gcf, gca
from pylab import mean, array, norm, sqrt
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
    z_offset : float
        Distance of third label from origin (in points)
    origin_marker : list
        Markers denoting origin
    kwargs : dict
        Passed to matplotlib.annotate (overrides color argument)
    '''

    if ax is None :
        ax = gca()

    if z_offset is None :

        z_offset_to_fontsize_ratio = .6

        try :
            z_offset = z_offset_to_fontsize_ratio*kwargs['fontsize']
        except :
            z_offset = z_offset_to_fontsize_ratio*rcParams['font.size']

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

    xy_start = [ center ]*2
    xy_end = [ ( center[0] + arrow_length[0], center[1]  ), ( center[0], center[1] + orientation*arrow_length[1] ) ]

    for i, letter in enumerate( letters ) :

        if i < 2 :
            ax.annotate( '', xy = xy_start[i], xytext = xy_end[i], **annotate_kwargs ) # arrow, two annotate calls for exact arrow length
            direction = array( xy_end[i] ) - array( xy_start[i] )
            direction /= norm( direction )
            xytext = direction*z_offset

            if ( i == 0 and ax.xaxis_inverted() ) or ( i == 1 and ax.yaxis_inverted() ) :
                xytext *= -1

            ghost_xy = xy_end[i]

        else :
            direction = - mean( array( xy_end ) - array( xy_start ), axis = 0 )
            direction /= norm( direction )
            xytext = sqrt(2)*direction*z_offset

            if ax.xaxis_inverted( ) :
                xytext[0] *= -1

            if ax.yaxis_inverted( ) :
                xytext[1] *= -1

            ghost_xy = center


        ghost_annotate_kwargs = annotate_kwargs.copy()
        ghost_annotate_kwargs.update( arrowprops = None, textcoords = 'offset points' )

        ax.annotate( letter, xy = ghost_xy, xytext = xytext, **ghost_annotate_kwargs ) # arrow label


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
    # gca().invert_yaxis()
    print( gca().yaxis_inverted() )

    plot_frame( arrow_length = .3, color = 'm', letters = ('x', 'y', 'z'), orientation = 1 )

    show()
