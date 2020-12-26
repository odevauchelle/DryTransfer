
default_style = dict(
    letter_index = 0,
    label = lambda i: '(' + 'abcdefghijklmnopqrstuvwxyz'[i] + ')',
    bbox = dict( boxstyle = "round, pad=.2", fc = 'white', ec = 'none', alpha = .5 ),
    xytext = ( 5, -5 ),
    zorder = None,
    xy = ( 0, 1 ),
    xycoords = 'axes fraction',
    textcoords = 'offset points',
    ha = 'left',
    va = 'top',
    )

def label_axes( axes, **kwargs ) :

    '''
    Add labels on axes.
    '''

    st = default_style.copy()
    st.update(kwargs)

    letter_index = st.pop('letter_index')

    for ax in axes :

        ax.annotate( st['label']( letter_index ), **st )

        letter_index += 1

    return letter_index

if __name__ == '__main__' :

    from pylab import subplots, show, imag, meshgrid, linspace

    fig, axs = subplots( nrows = 2, ncols = 2 )

    x = linspace(-1,1,25)
    x, y = meshgrid( x, x )
    z = x + 1j*y

    for i, ax in enumerate( axs.flatten() ) :
        ax.contourf( x, y, imag( z**i-z+3 ) )

    label_axes( axs.flatten() )

    show()
