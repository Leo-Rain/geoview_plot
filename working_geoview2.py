import numpy as np
import geoviews as gv
import geoviews.feature as gf
import cartopy.crs as ccrs
import bokeh
from scipy.io import loadmat
import datetime
import pandas as pd
from dateutil.parser import parse
# import matplotlib as mpl
# from pylab import  *
import numpy as np
#import os


gv.extension('bokeh')


from datetime import timedelta

# import matplotlib.tri as mtri
datamat = loadmat('IOEC_ECM2017_BC.mat')
xp = datamat['Xp']
yp = datamat['Yp']

tri_new = pd.read_csv('fort.ele', delim_whitespace=True, names=('A', 'B', 'C', 'D'), usecols=[1, 2, 3], skiprows=1,
                      dtype={'D': np.int})

x = xp.flatten()
y = yp.flatten()

tri_sub = tri_new.apply(lambda x: x - 1)
print(tri_sub.shape)

trimesh = gv.TriMesh((tri_sub, (x, y)))
trimesh.opts(padding=0.1, width=800, height=600)