"""
Author: richardutils authors
Licence: MIT

"""

import math
import os
import copy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

import xarray as xr
import rioxarray
import geocube
from geocube.api.core import make_geocube
import geopandas as gpd
import fiona

def richardfunction(n: float) -> float:
    """
    My function makes square roots.

    Args:
        n: A number of some kind.

    Returns:
        The squarest root.

    Examples:
    >>> richardfunction(9)
    3.0
    >>> richardfunction(100)
    10.0
    """
    return math.sqrt(n)
    
    
def cetrainbow():
    """
    Make a CET perceptually uniform rainbow colormap
    """

    CET = """0 0 48 245
1 0 52 242
2 0 55 238
3 0 59 235
4 3 62 231
5 9 66 228
6 14 69 225
7 18 72 221
8 20 74 218
9 22 77 214
10 23 80 211
11 24 82 207
12 25 85 204
13 25 87 200
14 25 90 197
15 25 92 193
16 25 94 190
17 25 96 187
18 24 99 183
19 24 101 180
20 24 103 177
21 23 105 173
22 23 106 170
23 24 108 167
24 24 110 164
25 25 112 160
26 27 113 157
27 28 115 154
28 30 117 151
29 32 118 148
30 34 120 145
31 36 121 142
32 39 122 139
33 41 124 136
34 43 125 133
35 45 126 130
36 47 128 127
37 49 129 124
38 51 130 121
39 53 132 118
40 54 133 115
41 56 134 112
42 57 136 109
43 58 137 106
44 59 138 103
45 60 139 99
46 61 141 96
47 62 142 93
48 62 143 90
49 63 145 87
50 63 146 83
51 64 147 80
52 64 149 77
53 64 150 74
54 65 151 70
55 65 153 67
56 65 154 63
57 65 155 60
58 66 156 56
59 66 158 53
60 67 159 50
61 68 160 46
62 69 161 43
63 70 162 40
64 71 163 37
65 73 164 34
66 75 165 31
67 77 166 28
68 79 167 26
69 82 168 24
70 84 169 22
71 87 170 20
72 90 171 19
73 93 172 18
74 96 173 17
75 99 173 17
76 102 174 16
77 105 175 16
78 108 176 16
79 111 176 16
80 114 177 17
81 117 178 17
82 121 179 17
83 124 179 18
84 127 180 18
85 130 181 19
86 132 182 19
87 135 182 20
88 138 183 20
89 141 184 20
90 144 184 21
91 147 185 21
92 150 186 22
93 153 186 22
94 155 187 23
95 158 188 23
96 161 188 24
97 164 189 24
98 166 190 25
99 169 190 25
100 172 191 25
101 175 192 26
102 177 192 26
103 180 193 27
104 183 194 27
105 186 194 28
106 188 195 28
107 191 195 29
108 194 196 29
109 196 197 30
110 199 197 30
111 202 198 30
112 204 199 31
113 207 199 31
114 210 200 32
115 212 200 32
116 215 201 33
117 217 201 33
118 220 202 34
119 223 202 34
120 225 202 34
121 227 203 35
122 230 203 35
123 232 203 35
124 234 203 36
125 236 203 36
126 238 203 36
127 240 203 36
128 241 202 36
129 243 202 36
130 244 201 36
131 245 200 36
132 246 200 36
133 247 199 36
134 248 197 36
135 248 196 36
136 249 195 36
137 249 194 35
138 249 192 35
139 250 191 35
140 250 190 35
141 250 188 34
142 250 187 34
143 250 185 34
144 250 184 33
145 250 182 33
146 250 180 33
147 250 179 32
148 249 177 32
149 249 176 32
150 249 174 31
151 249 173 31
152 249 171 31
153 249 169 30
154 249 168 30
155 249 166 30
156 248 165 29
157 248 163 29
158 248 161 29
159 248 160 29
160 248 158 28
161 248 157 28
162 248 155 28
163 247 153 27
164 247 152 27
165 247 150 27
166 247 148 26
167 247 147 26
168 246 145 26
169 246 143 26
170 246 142 25
171 246 140 25
172 246 138 25
173 245 137 24
174 245 135 24
175 245 133 24
176 245 132 24
177 244 130 23
178 244 128 23
179 244 127 23
180 244 125 23
181 244 123 22
182 243 121 22
183 243 119 22
184 243 118 22
185 243 116 21
186 242 114 21
187 242 112 21
188 242 110 21
189 241 109 21
190 241 107 21
191 241 105 21
192 241 103 21
193 240 101 21
194 240 100 22
195 240 98 22
196 240 96 23
197 240 95 24
198 240 93 26
199 240 92 27
200 240 90 29
201 240 89 31
202 240 88 33
203 240 87 36
204 240 87 38
205 241 86 41
206 241 86 44
207 242 86 47
208 242 86 51
209 243 86 54
210 243 87 58
211 244 88 62
212 245 88 65
213 245 89 69
214 246 90 73
215 247 91 77
216 247 92 82
217 248 94 86
218 249 95 90
219 249 96 94
220 250 97 98
221 251 99 102
222 251 100 106
223 252 101 111
224 252 103 115
225 253 104 119
226 253 105 123
227 254 107 128
228 254 108 132
229 255 109 136
230 255 111 140
231 255 112 145
232 255 114 149
233 255 115 153
234 255 116 157
235 255 118 162
236 255 119 166
237 255 120 170
238 255 122 175
239 255 123 179
240 255 125 183
241 255 126 188
242 255 127 192
243 255 129 196
244 255 130 201
245 255 132 205
246 255 133 210
247 255 134 214
248 255 136 219
249 255 137 223
250 255 139 227
251 255 140 232
252 255 141 236
253 254 143 241
254 254 144 245
255 253 146 250
"""

    import io

    data = io.StringIO(CET)
    df = pd.read_csv(data, sep=" ", header=None,names=["i",'r','g','b'], low_memory=False)

    def makecmp(df):
        df['r'] = df['r']/255
        df['g'] = df['g']/255
        df['b'] = df['b']/255

        del df['i']
        df['a'] = (df['r']+df['g']+df['b']+0.001)/(df['r']+df['g']+df['b']+0.001)
        arr = df.to_numpy()
        newcmp = ListedColormap(arr)
        
        return newcmp

    newcmp = makecmp(df)
    
    return newcmp


def plotmap(da, robust=False, cmap='cetrainbow', size=6, title='Title Here', clip=None, savefig=True, slide_dict=None, background=False):
    """
    Plot a dataarray with a title.
    Allow saving to a png
    Allow adding to a dictionary e.g. for presentation use

    Args:
        da: A DataArray
        robust: clip to 2/98 or not
        cmap: a matplotlib colormap
        size: integer size of plot
        title: string title of plot
        clip: quantile number to clip to
        savefig: save png to directory
        slide_dict: add png path to a dictionary
        background: plot a background shape layer

    Returns:
        The squarest root.

    Examples:
    
    """

    fig, ax = plt.subplots(figsize=(size,size))
    if background is False:
        pass
    elif background is True:
        daback = da / da
        da.plot(cmap='Greys')
    
    else:
        background.plot()
        
    if clip is not None:
        quantile = np.nanpercentile(da, clip)
        da.plot(cmap=cmap, robust=robust, ax=ax, vmax=quantile)
    else:
        da.plot(cmap=cmap, robust=robust, ax=ax)
    plt.title(title)
    ax.axes.set_aspect('equal')
    if savefig:
        plt.savefig(title + '.png',bbox_inches='tight')
        if slide_dict is not None:
        
        
            slide_dict[title] = title + '.png'
            
            
def plotmap_background(da, robust=False, cmap='cetrainbow', size=6, title='Title Here', clip=None, savefig=True, slide_dict=None, background=False, alpha=0.999):
    """
    Plot a dataarray with a title.
    Allow saving to a png
    Allow adding to a dictionary e.g. for presentation use

    Args:
        da: A DataArray
        robust: clip to 2/98 or not
        cmap: a matplotlib colormap
        size: integer size of plot
        title: string title of plot
        clip: quantile number to clip to
        savefig: save png to directory
        slide_dict: add png path to a dictionary
        background: plot a background shape layer if True is passed based on the DataArray, if a da is passed, use that - assumes data > 0

    Returns:
        

    Examples:
    
    """

    fig, ax = plt.subplots(figsize=(size,size))
    if background is False:
        pass
    elif background is True:
        daback = da / da
        daback.plot(cmap='Greys',ax=ax, alpha=alpha)
        x_range = plt.xlim()
        y_range = plt.ylim()
    
    else:
        background.plot(add_colorbar=False,cmap='Greys',ax=ax)
        x_range = plt.xlim()
        y_range = plt.ylim()
        
    da = da.where(da >=0, drop=True)
    
    if clip is not None:
        quantile = np.nanpercentile(da, clip)
        da.plot(cmap=cmap, robust=robust, ax=ax, vmax=quantile)
    else:
        x_range = plt.xlim()
        y_range = plt.ylim()
        
        da.plot(cmap=cmap, robust=robust, ax=ax)
        
    plt.title(title)
    ax.axes.set_aspect('equal')
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)

    if savefig:
        plt.savefig(title + '.png',bbox_inches='tight')
        if slide_dict is not None:
        
        
            slide_dict[title] = title + '.png'
            
        
def plotmapc(da, robust=False, cmap='cetrainbow', size=6, title='Title Here', clip=None, savefig=True, slide_dict=None, background=False):
    """
    Plots a dataarray and makes the colorbar the same height as the plot
    
    Plot a dataarray with a title.
    Allow saving to a png
    Allow adding to a dictionary e.g. for presentation use

    Args:
        da: A DataArray
        robust: clip to 2/98 or not
        cmap: a matplotlib colormap
        size: integer size of plot
        title: string title of plot
        clip: quantile number to clip to
        savefig: save png to directory
        slide_dict: add png path to a dictionary
        background: plot a background shape layer

    Returns:
        The squarest root.

    Examples: plotmapc(da_exploding_stars, cmap='magma', title='Exploding Stars')
    
    """

    fig, ax = plt.subplots(figsize=(size,size))
    if background is False:
        pass
    elif background is True:
        daback = da / da
        da.plot(cmap='Greys',add_colorbar=False, ax=ax)
    
    else:
        background.plot()
        
    if clip is not None:
        quantile = np.nanpercentile(da, clip)
        im = da.plot(cmap=cmap, robust=robust, ax=ax, vmax=quantile,add_colorbar=False)
    else:
        im = da.plot(cmap=cmap, robust=robust, ax=ax, add_colorbar=False)
    plt.title(title)
    ax.axes.set_aspect('equal')
    
    cax = fig.add_axes([ax.get_position().x1+0.01,ax.get_position().y0,0.02,ax.get_position().height])
    plt.colorbar(im, cax=cax) # Similar to fig.colorbar(im, cax = cax)

    if savefig:
        plt.savefig(title + '.png',bbox_inches='tight')
        if slide_dict is not None:
        
        
            slide_dict[title] = title + '.png'

        
def plothist(da, title, color='Orange', savefig=True, slide_dict = None):
    da.plot.hist(density=True, color=color)
    plt.yscale('log')
    plt.title(title)
    if savefig:
        plt.savefig(title + '.png',bbox_inches='tight')     
        if slide_dict is not None:        
            slide_dict[title] = title + '.png'        

        
def plothist_combo(da, da2, title, color1='Orange',color2='Gold', savefig=True, slide_dict = None):
    """
    Plot a gepdataframe with a title.
    Allow saving to a png
    Allow adding to a dictionary e.g. for presentation use

    Args:
        da: A DataArray
        da2: A DataArray to compare
        color1: string color for first histogram
        color2: string color for secondt histogram
        title: title of plot
        alpha: transparently
        savefig: write a png to the directory
        slide_dict: dictionary to store reference to plots in
    """
    da.plot.hist(density=True, color=color1)
    da2.plot.hist(density=True, color=color2)
    plt.yscale('log')
    plt.title(title) 
    if savefig:
        plt.savefig(title + '.png',bbox_inches='tight')     
        if slide_dict is not None:        
            slide_dict[title] = title + '.png'  


def plotgdf(gdf, column, title,alpha=0.5, savefig=True, cmap='cetrainbow', slide_dict=None, size=7, legend=False):
    """
    Plot a gepdataframe with a title.
    Allow saving to a png
    Allow adding to a dictionary e.g. for presentation use

    Args:
        gdf: A gepdataframe
        column: string column to plot
        title: title of plot
        alpha: transparently
        savefig: write a png to the directory
        cmap: a matplotlib colormap
        slide_dict: dictionary to store reference to plots in


    Examples:
    
    """
    fig, ax = plt.subplots(figsize=(size,size))
    gdf.plot(column=column,  alpha=alpha, cmap=cmap, legend=legend, ax=ax)
    plt.title(title)
    ax.axes.set_aspect('equal')
    if savefig:
        plt.savefig(title + '.png',bbox_inches='tight')     
        if slide_dict is not None:        
            slide_dict[title] = title + '.png' 


def plotmapw(da, robust=False, cmap='cetrainbow', size=6, title='Title Here', clip=None, savefig=True, slide_dict=None, vmax=None):
    """
    Plot a dataarray with a title. Remove colorbar in the way
    Allow saving to a png
    Allow adding to a dictionary e.g. for presentation use

    Args:
        da: A DataArray


    Examples:
    
    """
    fig, ax = plt.subplots(figsize=(size,size))
    if clip is not None:
        quantile = np.nanpercentile(da, clip)
        da.plot(cmap=cmap, robust=robust, ax=ax, vmax=quantile)
    elif vmax is not None:
        da.plot(cmap=cmap, robust=robust, ax=ax, vmax=vmax)
    else:
        da.plot(cmap=cmap, robust=robust, ax=ax, vmax=vmax)
            
    plt.title(title)
    plt.gca().collections[0].colorbar.remove()
    ax.axes.set_aspect('equal')
    if savefig:
        plt.savefig(title + '.png',bbox_inches='tight')
        if slide_dict is not None:
            slide_dict[title] = title + '.png'
        
    return ax
   
        
def mmnorm(da):
    """
    Minmax norm xarray DataArray

    Args:
        da: A DataArray

    Returns:
        normalised DataArray

    Examples:
        mnorm(geoscience_raster)
    """

    da_norm = (da - da.min(skipna=True))/(da.max(skipna=True) - da.min(skipna=True))
    
    return da_norm      


def norm_diff_comparison(da1, da2):
    """
    Normalised difference and ratio of two xarray

    Args:
        da1, da2: DataArrays

    Returns:
        Difference and ratio of reprojected match DataArrays

    Examples:
        norm_diff_comparison(daarea1, daarea2):
    """

    da1 = da1.rio.reproject_match(da2)
    da1_norm = mmnorm(da1)
    da2_norm = mmnorm(da2)
    diff = da1_norm - da2_norm    
    ratio = da1_norm / da2_norm    
    
    return diff, ratio
        
    
def makegdf(df, xcol='longitude', ycol='latitude', crs='EPSG:4326'):
    """
    Turn a dataframe of a csv of points into a geodataframe

    Args:
        df: a dataframe from csv
        xcol: x coordinate [longitude, easting etc.]
        ycol: y coordinate

    Returns:
        gdf geodataframe

    Examples:
        gdf = makegdf(df,'longitude','latitude','EPSG:4326')    
    """

    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[xcol],df[ycol], crs=crs))
    
    return gdf


def df_bb(df, bb, xcol='longitude', ycol='latitude'):
    """
    Clips a dataframe of points by a bounding box

    Args:
        df: a dataframe from csv
        xcol: x coordinate [longitude, easting etc.]
        ycol: y coordinate
        bb: a bounding box

    Returns:
        df trimmed to bounding box

    Examples:
        dfbb = df_bb(df,bb, 'longitude','latitude')    
    """

    dfbb = df.loc[df[xcol] > bb[0]]
    dfbb = dfbb.loc[df[xcol] < bb[2]]
    dfbb = dfbb.loc[df[ycol] > bb[1]]
    dfbb = dfbb.loc[df[ycol] < bb[3]]
    
    return dfbb
    
    
def gdf_bb(gdf, bb):
    """
    Returns a bounding box filtered gdf
    
    Args: 
        gdf: geodataframe
        bb: bounding box
    """
    gdfbb = gdf.cx[bb[0]:bb[2],bb[1]:bb[3]]
    
    return gdfbb
    

def gdb_dict(gdbpath):
    """
    Returns a dictionary of geodataframes
    
    Args: 
        gdbpath: path to a FileGDB
    """
    gdb_dict = {}
    for l in fiona.listlayers(gdpath):
        gdb_dict[l] = gpd.read_file(gdbpath, driver='FileGDB', layer=l)
    
    return gdb_dict
    


def zonal_stats(vector_data, measurements, dalike, variable):
    """
    Get a dataframe of zonal statistics from a DataArra

    Args:
        vector_data: a dataframe with a unique id
        measurements: unique column of interest
        dalike: DataArray to make grid from
        variable: Name to give the out grid variable

    Returns:
        zonal stats dataframe

    Examples:
        gdf = zonal_stats(gdf,'USEID',da,'LASERBLASTRADIUS')    
    """

    out_grid = make_geocube(
        vector_data=vector_data,
        measurements=[measurements],
        like=dalike, # ensure the data are on the same grid
    )
    out_grid[variable] = (dalike.dims, dalike.values, dalike.attrs, dalike.encoding)
    
    grouped_da = out_grid.drop("spatial_ref").groupby(out_grid[measurements])

    grid_mean = grouped_da.mean(skipna=True)
    grid_min = grouped_da.min(skipna=True)
    grid_max = grouped_da.max(skipna=True)
    grid_std = grouped_da.std(skipna=True)
    grid_quantile = grouped_da.quantile(0.999, skipna=True)

    grid_mean = grid_mean.rename({variable: variable + "_mean"})
    grid_max = grid_max.rename({variable: variable + "_max"})
    grid_min = grid_min.rename({variable: variable + "_min"})
    grid_std = grid_std.rename({variable: variable + "__std"})
    grid_quantile = grid_quantile.rename({variable: variable + "_quantile999"})
    
    zonal_stats_out = xr.merge([grid_mean, grid_min, grid_max, grid_std, grid_quantile]).to_dataframe()
    
    zonal_data = vector_data.merge(zonal_stats_out, on=measurements)
    
    return zonal_stats_out    
    

def global_low_res():
    """
    Returns:
        built in global low res world polygons for cheap clipping
    """
    world_filepath = gpd.datasets.get_path('naturalearth_lowres')
    world = gpd.read_file(world_filepath)

    return world


def world_low_res(country):
    """
    Args:
        country: string of desired country border e.g. Australia
    Returns: 
        Built in global low res world polygons for cheap clipping filtered to one country

    """
    world_filepath = gpd.datasets.get_path('naturalearth_lowres')
    world = gpd.read_file(world_filepath)

    country_out = world.loc[world['name'] == country]

    return country_out

    
def zonal_onshore(country, data):
    """
    Returns geodataframe clipped to a country low res boundary: e.g. for after zonal stats dataframe production
    
    Args:
        country: string of desired country border e.g. Australia
        data: ataframe with a geometry column
        
    Returns:
        onshore lowres clipped geodataframe
    """

    gdf_data = gpd.GeoDataFrame(data, geometry = data['geometry'])
    boundary = world_low_res(country)
    if boundary.crs != gdf_data.crs:
        boundary = boundary.to_crs(gdf_data.crs)
    
    data_onshore = gpd.clip(data, boundary)
    
    return data_onshore

    
def zonal_onshore_globe(data):
    """
    Returns geodataframe clipped to global land:  e.g. for after zonal stats dataframe production
    
    Args:
        data: dataframe with a geometry column
    Returns:
        Onshore zonal data
        
    """

    gdf_data = gpd.GeoDataFrame(data, geometry = data['geometry'])
    boundary = global_low_res()
    if boundary.crs != gdf_data.crs:
        boundary = boundary.to_crs(gdf_data.crs)
    
    data_onshore = gpd.clip(data, boundary)
    
    return data_onshore

    
def location_sample(gdf, da, name_col):
    """
    Returns a dataframe of points sample from a DataArray by location at once
    
    Args:
        gdf: geodataframe of points
        da: DataArrau to sample:
        name_col: String to identify the location names
        
    Returns:
        Onshore location sample dataframe
    
    """

    lat = gdf.geometry.y.tolist()
    lon = gdf.geometry.x.tolist()
    xl = xr.DataArray(lon, dims=['location'],coords={"location":gdf[name_col].tolist()})
    yl = xr.DataArray(lat, dims=['location'],coords={"location":gdf[name_col].tolist()})
    
    dapt = da.sel(x=xl,y=yl,method="nearest")
    dfda = dapt.to_dataframe().reset_index()  
   
    return dfda

    
def tif_dict(strpath, masked=True, chunks=None, dsmatch=None):
    """
    Walks a directory of geotiffs and returns a dictionary of rioxarray DataArrays
    Args:
        strpath: directory name
        chunks: tuple of integers
        dsmatch: data array to match the directory of raster to
        masked: whether to mask by nodata, default is yes, pass masked=False if not desired
    Returns:
        a dictionary of rioxarrays
        
    Examples: 
       tif_dict(r'D:\BananaSplits')
       tif_dict(r'D:\BananaSplits', chunk=s(1,1024,1024))
    
    """

    check_dict = {}
    for root, dirs, files in os.walk(strpath):
        for file in files:
            if '.tif' in file and '.xml' not in file:
                if dsmatch is None:
                    if chunks is None:
                        check_dict[file] = rioxarray.open_rasterio(os.path.join(root,file),masked=masked)    
                    else:
                        check_dict[file] = rioxarray.open_rasterio(os.path.join(root,file), masked=masked, chunks=chunks)    
                else:
                    if chunks is None:
                        check_dict[file] = rioxarray.open_rasterio(os.path.join(root,file), masked=masked).rio.reproject_match(dsmatch)    
                    else:
                        check_dict[file] = rioxarray.open_rasterio(os.path.join(root,file), masked=masked, chunks=chunks).rio.reproject_match(dsmatch)    
                
    return check_dict
     


def clip_da(dapath, gdfpath):
    """
    Clips a rioxarray by geodataframe polygons
    
    Args:
        dapath: Path to raster
        gdfpath: Path to vector polygon dataset
    
    Returns:
        Clipped rioxarray
        
    Examples: 
        schaus = clip_da('dapath', 'gdfpath')
    
    """

    da = rioxarray.open_rasterio(dapath)
    gdf = gpd.read_file(gdfpath)
    clipped = da.rio.clip(gdf.geometry.values, gdf.crs, drop=True, invert=False)
    
    return clipped
    

def clip_dabox(dapath, bb):
    """
    Clips a rioxarray by geodataframe polygons
    
    Args:
        dapath: Path to raster
        bb: boundingbox coordinates xmin, ymin, xmax, ymax
    
    Returns:
        Clipped rioxarray
        
    Examples: 
        schaus = clip_dabox('dapath', bb)
    
    """

    da = rioxarray.open_rasterio(dapath)
    clipped = da.rio.clip_box(xmin = bb[0], ymin=bb[1],xmax=bb[2],ymax=bb[3])
    
    return clipped
    


def extract_band(tifpath, findstr):
    """
    Extract a named band from a geotiff via rioxarray
    
    Args:
        tifpath: Path to raster
    
    Returns:
        geotiff band
        
    Examples: 
        darock = extract_band(usepath, 'ROCK')
    
    """

    print("finding band:", findstr)
    da = rioxarray.open_rasterio(tifpath, masked=True)
    for idx, name in enumerate(da.attrs['long_name']):
        
        if name == findstr:
            print(os.path.basename(tifpath))
            da.attrs['long_name'] = findstr
            newpath = tifpath.replace('.tif', '_' + findstr + '.tif')
            print(newpath)
            
            da[idx].rio.to_raster(newpath)
            
            return da[idx]
            
            
            
