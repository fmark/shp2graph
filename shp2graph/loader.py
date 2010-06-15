
try:
    from osgeo import ogr
except ImportError:
    import ogr

class Graph:
    
    def __init__(filename):
        self._filename = filename
