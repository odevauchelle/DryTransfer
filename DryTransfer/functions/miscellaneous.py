
def figname( filename = None , ext = '.pdf' ):
    '''
    Generate figure name based on current script name.

    Arguments
    ---------
    file : str
        The file name to be converted, typically __file__
    ext : str
        Extension

    Returns
    -------
    figure_name : str
        File name with a new extension
    '''

    if filename is None :
        filename = __file__

    figure_name = filename.split('/')[-1].split('.')[0] + ext

    return figure_name

def float2str( num, rounding_scale = 100 ) :
    '''
    Round number for display.

    Arguments
    ---------
    num : float
        The number to be displayed
    rounding_scale : int
        How many significant figures

    Returns
    -------
    disp_num : str
        String ready for display
    '''

    disp_num = round( num*rounding_scale )/float(rounding_scale)

    return str( disp_num )

###################################
#
# try it out
#
###################################

if __name__ == '__main__' :

    print(figname(__file__))
