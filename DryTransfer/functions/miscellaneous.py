
def figname( file, ext = '.pdf' ):
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

    figure_name = file.split('/')[-1].split('.')[0] + ext

    return figure_name

###################################
#
# try it out
#
###################################

if __name__ == '__main__' :

    print(figname(__file__))
