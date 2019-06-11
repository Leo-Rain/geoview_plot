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
# import os

import geopandas as gpd
import geoviews as gv
import cartopy.crs as ccrs
import geoviews.feature as gf

from cartopy import crs
from geoviews import opts

gv.extension('bokeh')

tiles = gv.tile_sources.Wikipedia

from datetime import timedelta


def perdelta(strt, end, delta):
    curr = strt
    while curr < end:
        yield curr
        curr += delta


# import matplotlib.tri as mtri
datamat = loadmat('IOEC_ECM2017_BC.mat')
xp = datamat['Xp']
yp = datamat['Yp']

strt = datetime.datetime(2017, 1, 11, 0, 0)
end = datetime.datetime(2017, 1, 21, 0, 0)
numdays = 3

tri_new = pd.read_csv('fort.ele', delim_whitespace=True, names=('A', 'B', 'C', 'D'), usecols=[1, 2, 3],
                      skiprows=1,
                      dtype={'D': np.int})

for result in perdelta(strt, strt + timedelta(days=2), timedelta(hours=3)):
    dat = result
    # print(result)
    dt = parse(str(dat))
    yr = dt.year
    mn = dt.month
    d = dt.day
    hr = dt.hour
    mi = dt.minute
    # print(y,mn,d,hr,mi)
    if hr < 10:
        # d='0'+str(d)
        hr = '0' + str(hr)
    else:
        d = str(d)
        hr = str(hr)
    if int(d) < 10:
        d = '0' + str(d)
    else:
        d = str(d)
    varname = 'Hsig_' + str(yr) + '0' + str(mn) + str(d) + '_' + hr + '0000'
    print(varname)

    x = xp.flatten()
    y = yp.flatten()
    z = datamat[varname]
    z1 = z.flatten()
    print(z1)

    tri_sub = tri_new.apply(lambda x: x - 1)
    print(tri_sub.shape)

    trimesh = gv.TriMesh((tri_sub, (x, y)))
    trimesh.opts(padding=0.1, width=200, height=200)