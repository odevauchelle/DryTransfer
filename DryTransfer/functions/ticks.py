from matplotlib.pyplot import gcf, gca
from pylab import array, argmin

def add_tick( location, label = None, ax = None, xy = 'x', remove_neighbor = 0 ) :
    '''
    Adds a new tick with label.
    From https://stackoverflow.com/questions/22245949/adding-a-custom-tick-and-label

    add_tick( location, label = None, ax = None, xy = 'x', remove_neighbor = 0 )

    Arguments:
    location : Where the label is to appear.
    label : Which label to show.
    ax : The axes instance.
    xy ('x' or 'y') : The coordinate.
    remove_neighbor (int) : Number of neighboring ticks to remove.

    '''

    if ax is None :
        ax = gca()

    if label is None:
        label = str( location )

    ax.figure.canvas.draw() # this is required, or the ticklabels may not exist (yet) at the next step

    if xy == 'x' :
        labels = [ w.get_text() for w in ax.get_xticklabels() ]
        locs = list( ax.get_xticks() )

    elif xy == 'y' :
        labels = [ w.get_text() for w in ax.get_yticklabels() ]
        locs = list( ax.get_yticks() )

    for _ in range( remove_neighbor ) :

        try :
            index = argmin( ( array( locs ) - location )**2 )
            labels.pop( index )
            locs.pop( index )

        except :
            break

    labels += [ label ]
    locs += [ location ]


    if xy == 'x' :
        ax.set_xticklabels(labels)
        ax.set_xticks(locs)

    elif xy == 'y' :
        ax.set_yticks(locs)
        ax.set_yticklabels(labels)

def hide_tick_labels( ax = None, xy = 'xy' ) :
    '''
    Hide all labels, but not the ticks. Usefull when using GridSpec.

    hide_tick_labels( ax = None, xy = 'xy' )

    Arguments:
    ax : The axes instance.
    xy ('x' or 'y' or 'xy') : The coordinate.
    '''

    if ax is None :
        ax = gca()

    if 'x' in xy :

        for label in ax.get_xticklabels( which = "both" ):
                label.set_visible(False)

    if 'y' in xy :

        for label in ax.get_yticklabels( which = "both" ):
                label.set_visible(False)
