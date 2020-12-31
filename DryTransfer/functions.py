from matplotlib.pyplot import gcf, gca

###################################
#
# Label axes
#
###################################

_label_axes_default_style = dict(
    letter_index = 0,
    label = lambda i: 'abcdefghijklmnopqrstuvwxyz'[i],
    bbox = dict( boxstyle = "round, pad=.2", fc = 'white', ec = 'none', alpha = .5 ),
    xytext = ( 5, -5 ),
    zorder = None,
    xy = ( 0, 1 ),
    xycoords = 'axes fraction',
    textcoords = 'offset points',
    ha = 'left',
    va = 'top',
    )

def label_axes( axes = None, fig = None, **kwargs ) :

    '''
    Add labels on axes.

    Arguments
    ---------
    axes : list
        List of axes to be labelled (optional)
    fig : figure handle
        Figure from which axes are guessed (optional)
    letter_index : int
        Index of first label
    **kwargs : dict
        Style arguments passed to annotate

    Returns
    --------
    letter_index : int
        Index of next label
    '''

    if axes is None :
        try :
            axes = fig.axes
        except :
            axes = gcf().axes


    st = _label_axes_default_style.copy()
    st.update(kwargs)

    letter_index = st.pop('letter_index')

    for ax in axes :

        ax.annotate( st['label']( letter_index ), **st )

        letter_index += 1

    return letter_index

###################################
#
# PLOT FRAME
#
###################################

_plot_frame_default_style = dict(
    color = 'k',
    center = ( 0.,0. ),
    arrow_length = 1.,
    letters = ( 'x', 'y', 'z' ),
    orientation = 1,
    textcoords = 'data',
    xycoords = 'data',
    va="center",
    ha="center",
    arrowprops = dict( arrowstyle = "->" ),
    text_shift_ratio = 0.1,
    origin_markers = True
    )

_default_origin_markers = [
        dict( marker = '.', ms = 5 ),
        dict( mfc = 'none', marker = 'o', ms = 7 )
        ]

def plot_frame( ax = None, **kwargs ) :

    '''
    Draws a two-dimensional reference frame.

    Arguments
    ---------
    ax : Matplotlib axes
        Axes on which to draw reference frame (optional)
    arrow_length : float or list
        Length of frame arrows
    text_color : str or tuple
        Axis names color
    center : tuple
        Position of origin
    letters : list
        Name of axis
    orientation : 1 or -1
        Left or right
    text_shift_ratio : float
        Labels position with respect to arrows
    origin_markers : list
        Markers denoting origin
    '''

    if ax is None :
        ax = gca()

    st = _plot_frame_default_style.copy()
    st.update( kwargs )

    try :
        st['arrow_length'][0]
    except :
        st['arrow_length'] = 2*[ st['arrow_length'] ]

    try :
        text_color = st.pop('text_color')
    except :
        text_color = st['color']

    try :
        st['arrowprops']['color']
    except :
        st['arrowprops']['color'] = st['color']


    arrow_length = st.pop('arrow_length')
    center = st.pop('center')
    letters = st.pop('letters')
    orientation = st.pop('orientation')
    text_shift_ratio = st.pop('text_shift_ratio')
    origin_markers = st.pop('origin_markers')

    try :
        if origin_markers :
            origin_markers = _default_origin_markers
        else :
            origin_markers = []
    except :
        pass

    ax.annotate("",
            xy=( center[0], center[1] + orientation*arrow_length[1] ),
            xytext = center,
            **st
            )

    ax.annotate("",
            xy=( center[0] + arrow_length[0], center[1]  ),
            xytext = center,
            **st
            )

    text_st = dict( ha = 'center', va = 'center', color = text_color )

    letter_position = [
        ( center[0] + ( 1 + text_shift_ratio)*arrow_length[0], center[1] ),
        ( center[0], center[1] + orientation*(1 + text_shift_ratio)*arrow_length[1] ),
        ( center[0] - 3*text_shift_ratio*arrow_length[0], center[1] )
        ]

    for i, letter in enumerate( letters ) :
        ax.text( *letter_position[i], letter, **text_st )

    for marker_style in origin_markers :
        ax.plot( *center, color = st['color'], **marker_style )

###################################
#
# try it out
#
###################################

if __name__ == '__main__' :

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
