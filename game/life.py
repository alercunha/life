# still lifes

def block():
    return _convert(_block())


def _block():
    return '''
    ----
    -##-
    -##-
    ----
    '''


def bee_hive():
    return _convert(_bee_hive())


def _bee_hive():
    return '''
    ------
    --##--
    -#--#-
    --##--
    ------
    '''


def loaf():
    return _convert(_loaf())


def _loaf():
    return '''
    ------
    --##--
    -#--#-
    --#-#-
    ---#--
    ------
    '''


def boat():
    return _convert(_boat())


def _boat():
    return '''
    -----
    -##--
    -#-#-
    --#--
    -----
    '''


def tub():
    return _convert(_tub())


def _tub():
    return '''
    -----
    --#--
    -#-#-
    --#--
    -----
    '''


# oscillators

def blinker():
    return _convert(_blinker())


def _blinker():
    return '''
    -----
    --#--
    --#--
    --#--
    -----
    ''' 


def toad():
    return _convert(_toad()) 


def _toad():
    return '''
    ------
    --###-
    -###--
    ------
    '''


def beacon():
    return _convert(_beacon()) 


def _beacon():
    return '''
    ------
    -##---
    -##---
    ---##-
    ---##-
    ------
    '''


def penta_decathlon():
    return _convert(_penta_decathlon())


def _penta_decathlon():
    return '''
    ------------
    ---#----#---
    -##.####.##-
    ---#----#---
    ------------
    '''

# spaceships

def glider():
    return _convert(_glider())


def _glider():
    return '''
    -----
    -#-#-
    --##-
    --#--
    -----
    '''


def _convert(rep: str):
    lines = [l.strip() for l in rep.split()]
    y = 0
    cells = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                cells.append((x, y))
    return cells
