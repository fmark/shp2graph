from setuptools import setup, find_packages
import sys

readme_text = file('README', 'rb').read()

setup_args = dict(
    metadata_version = '0.1',
    name = 'shp2graph',
    version = '0.1',
#    requires_python = '>=2.5,<3',
#    requires_external = 'libgeos_c (>=3.1)',
    description = 'Convert shapefiles to graphs',
    license = 'LGPL',
    keywords = 'topology gis shapefile ogr network graph',
    author = 'F. Markham',
    author_email = 'fmarkham@gmail.com',
    maintainer = 'F. Markham',
    maintainer_email = 'fmarkham@gmail.com',
    url = 'http://github.com/fmark/shp2graph',
    long_description = readme_text,
    packages = ['shp2graph'],
    scripts = ['examples/shp2graph.py'],
#    test_suite = 'shapely.tests.test_suite',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
        ],
    )

# Add DLLs for Windows
# if sys.platform == 'win32':
#     setup_args.update(
#         data_files=[('DLLs', ['DLLs/geos.dll', 'DLLs/libgeos-3-0-0.dll']),]
#         )

setup(**setup_args)
