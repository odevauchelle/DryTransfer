from matplotlib.pyplot import gcf, gca

###################################
#
# Function argument management
#
###################################
#
# def get_arg_names( func ):
#     return func.__code__.co_varnames[ :func.__code__.co_argcount ]
#
# def filter_out_kwargs( func, kwargs ) :
#
#     filtered_kwargs = {}
#     remaining_kwargs = kwargs.copy()
#
#     for key in kwargs.keys() :
#         if key in get_arg_names( func ) :
#             filtered_kwargs[key] = remaining_kwargs.pop( key )
#
#     return func( **filtered_kwargs ), remaining_kwargs

###################################
#
# Label axes
#
###################################

_label_axes_default_style = dict(
    bbox = dict( boxstyle = "round, pad=.2", fc = 'white', ec = 'none', alpha = .5 ),
    )

def generate_label( letter_index, alphabet = 'abcdefghijklmnopqrstuvwxyz', ornament = ('', '') ):
    return alphabet[letter_index].join(ornament)

def generate_label_location( loc, padding ) :

    loc_kwargs = dict(
        xy = [ 0, 0 ],
        xytext = [ 0, 0 ],
        ha = '',
        va = '',
        xycoords = 'axes fraction',
        textcoords = 'offset points'
        )

    y, x = loc.split(' ')

    if x == 'left' :
        loc_kwargs['xy'][0] = 0
        loc_kwargs['xytext'][0] = padding[0]
        loc_kwargs['ha'] = 'left'

    elif x == 'right' :
        loc_kwargs['xy'][0] = 1
        loc_kwargs['xytext'][0] = -padding[0]
        loc_kwargs['ha'] = 'right'

    elif x == 'center' :
        loc_kwargs['xy'][0] = .5
        loc_kwargs['xytext'][0] = 0
        loc_kwargs['ha'] = 'center'

    if y == 'upper' :
        loc_kwargs['xy'][1] = 1
        loc_kwargs['xytext'][1] = -padding[1]
        loc_kwargs['va'] = 'top'

    elif y == 'lower' :
        loc_kwargs['xy'][1] = 0
        loc_kwargs['xytext'][1] = padding[1]
        loc_kwargs['va'] = 'bottom'

    elif y == 'center' :
        loc_kwargs['xy'][1] = .5
        loc_kwargs['xytext'][1] = 0
        loc_kwargs['va'] = 'center'

    return loc_kwargs

def label_axes( axes = None, fig = None, letter_index = 0, loc = 'upper left', padding = ( 5, 5 ), generate_label = generate_label, **kwargs ) :

    '''
    Add labels on axes.

    Arguments
    ---------
    axes : list
        List of axes to be labelled (optional)
    fig : figure handle
        Figure from which axes are guessed (optional)
    letter_index : int
        Index of first label (defaults to one)
    loc : str
        Location keywords; 'upper left', 'lower center', etc. (defaults to 'upper left')
    padding : tuple
        Label horizontal and vertical padding (defaults to (5,5))
    generate_label : function
        Converts letter_index into a label (string)
    **kwargs : dict
        Style arguments passed to matplotlib.annotate

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

    annotate_kwargs = _label_axes_default_style.copy() # overrides annotate default
    annotate_kwargs.update( generate_label_location( loc, padding ) )
    annotate_kwargs.update( kwargs ) # overrides location keywords

    for ax in axes :

        ax.annotate( s = generate_label( letter_index ), **annotate_kwargs )

        letter_index += 1

    return letter_index

if __name__ == '__main__' :

    from pylab import subplots, show, angle, meshgrid, linspace, sqrt

    fig, axs = subplots( nrows = 2, ncols = 2 )

    x = linspace(-1,1,50)
    x, y = meshgrid( x, x )
    z = x + 1j*y

    for i, ax in enumerate( axs.flatten() ) :
        ax.contourf( x, y, angle( sqrt( z**i - .1*z + .3 ) ) )

    label_axes( loc = 'lower left', color = 'red' )

    show()
