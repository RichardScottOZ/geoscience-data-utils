"""
Author: richardutils authors
Licence: MIT

"""

import math
import os
import copy
import json
import os
from functools import partial

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

from osgeo import gdal

import geopandas as gpd
import fiona
from shapely.geometry import box, mapping

import rasterio

import xarray as xr
import rioxarray
import geocube
from geocube.api.core import make_geocube
from geocube.rasterize import rasterize_points_griddata, rasterize_points_radial, rasterize_image

import xrspatial
from xrspatial import proximity

import pyvista as pv

from geoh5py.workspace import Workspace
from geoh5py.objects import BlockModel, Grid2D


def richardfunction(n: float) -> float:
    """
    This is not currently used so pointless to look at currently
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
    newcmp = cetrainbow()
    cm.register_cmap(name='cetrainbow', cmap=newcmp)

    To reverse: cet_r = ListedColormap(newcmp.colors[::-1])
                cm.register_cmap(name='cetrainbow_r', cmap=cet_r)

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


def plotmap3(da, robust=False, cmap='cetrainbow', size=6, title='Title Here', clip=None, savefig=True, slide_dict=None, background=False):
    """
    Plot a dataarray with a title.
    Allow saving to a png
    Allow adding to a dictionary e.g. for presentation use

    Args:
        da: A DataArray with 3 bands
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
        da.plot.imshow(cmap='Greys')
    
    else:
        background.plot()
        
    if clip is not None:
        quantile = np.nanpercentile(da, clip)
        da.plot.imshow(cmap=cmap, robust=robust, ax=ax, vmax=quantile)
    else:
        da.plot.imshow(cmap=cmap, robust=robust, ax=ax)
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
    Plot a geodataframe with a title.
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

def plotgdf_da(gdf, da, column, title,alpha=0.5, savefig=True, cmap='cetrainbow', cmap_da='cetrainbow',slide_dict=None, size=7, legend=False, robust=False):
    """
    Plot a geopdataframe with a title.
    Allow saving to a png
    Allow adding to a dictionary e.g. for presentation use

    Args:
        gdf: A gepdataframe
        column: string column to plot
        title: title of plot
        alpha: transparently
        savefig: write a png to the directory
        cmap: a matplotlib colormap or a string with color_colorwanted e.g. plotgdf(da,cmap="color_white") to get a flat color gdf plot
        slide_dict: dictionary to store reference to plots in


    Examples:
    
    """
    fig, ax = plt.subplots(figsize=(size,size))
    da.plot(ax=ax, cmap=cmap_da, robust=robust)
    if column is not None:
        if "color_" in cmap:
            gdf.plot(column=column,  alpha=alpha, color=cmap.split('_')[-1], legend=legend, ax=ax)
        else:
            gdf.plot(column=column,  alpha=alpha, cmap=cmap, legend=legend, ax=ax)
    else:
        if "color_" in cmap:
            gdf.plot(alpha=alpha, color=cmap.split('_')[-1], legend=legend, ax=ax)
        else:
            gdf.plot(column=column,  alpha=alpha, cmap=cmap, legend=legend, ax=ax)
    plt.title(title)
    plt.gca().collections[0].colorbar.remove()
    ax.axis('tight')
    #ax.axis('off')
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
    for l in fiona.listlayers(gdbpath):
        gdb_dict[l] = gpd.read_file(gdbpath, driver='FileGDB', layer=l)
    
    print(gdb_dict.keys())
    return gdb_dict
    

def shape_dict(shapepath):
    """
    Returns a dictionary of geodataframes
    
    Args: 
        shapepath: path to a directory with shapefiles
    """
    shape_dict = {}
    for root, dirs, files in os.walk(shapepath):
        for file in files:
            if '.shp' in file and 'xml' not in file:
                #print("reading: ", file
                newfile = file.replace('.shp','')
                shape_dict[newfile] = gpd.read_file(os.path.join(root,file))
    
    print(shape_dict.keys())
    return shape_dict


def zonal_stats(vector_data, measurements, dalike, variable):
    """
    Get a dataframe of zonal statistics from a DataArray

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
        rasterize_function=partial(rasterize_image, all_touched=True)
        
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
        da: DataArray to sample:
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


def gdf_shape_dict(strpath):    
    """
    Walks a directory of shapefiles
    Args:
        strpath: directory name
    Returns:
        a dictionary of geodataframes
        
    Examples: 
       gdf_shape_dict(r'D:\BananaSplits')
    
    """
    check_dict = {}
    for root, dirs, files in os.walk(strpath):
        for file in files:
            if '.shp' in file:
                check_dict[file] = gpd.read_file(os.path.join(root,file))
                
    return check_dict


def gdf_parquet_dict(strpath):    
    """
    Walks a directory of parquet geodataframes
    Args:
        strpath: directory name
    Returns:
        a dictionary of geodataframes
        
    Examples: 
       gdf_parquet_dict(r'D:\BananaSplits')
    
    """
    check_dict = {}
    for root, dirs, files in os.walk(strpath):
        for file in files:
            if '.parquet' in file:
                check_dict[file] = gpd.read_parquet(os.path.join(root,file))
                
    return check_dict

                
def gdf_parquet_list(strpath):    
    """
    Walks a directory of parquet geodataframes
    Args:
        strpath: directory name
    Returns:
        a list of geodataframes
        
    Examples: 
       gdf_parquet_list(r'D:\BananaSplits')
    
    """
    check_list = []
    for root, dirs, files in os.walk(strpath):
        for file in files:
            if '.parquet' in file:
                check_list.append(gpd.read_parquet(os.path.join(root,file)) )
                
    return check_list
            
   
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

    
def ers_dict(strpath, masked=True, chunks=None, dsmatch=None):
    """
    Walks a directory of ers grids and returns a dictionary of rioxarray DataArrays
    Args:
        strpath: directory name
        chunks: tuple of integers
        dsmatch: data array to match the directory of raster to
        masked: whether to mask by nodata, default is yes, pass masked=False if not desired
    Returns:
        a dictionary of rioxarrays
        
    Examples: 
       ers_dict(r'D:\BananaSplits')
       ers_dict(r'D:\BananaSplits', chunk=s(1,1024,1024))
    
    """

    check_dict = {}
    for root, dirs, files in os.walk(strpath):
        for file in files:
            
            if '.ers' in file and '.gi' not in file and '.xml' not in file:
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
    

def create_vrt_for_geotiffs(directory):
    """
    Args:
        directory: Path to raster tifs
    """

    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter only GeoTIFF files
    geotiff_files = [file for file in files if file.endswith('.tif') or file.endswith('.tiff')]
    
    # Iterate over GeoTIFF files and create VRT for each
    for geotiff_file in geotiff_files:
        geotiff_path = os.path.join(directory, geotiff_file)
        vrt_path = os.path.splitext(geotiff_path)[0] + '.vrt'
        
        # Create a VRT using GDAL
        gdal.BuildVRT(vrt_path, geotiff_path)
        print(f"Created VRT for {geotiff_file} at {vrt_path}")
        
        
def tif_to_ers(strpath, masked=True, chunks=None, dsmatch=None):
    """
    Walks a directory of geotiffs and returns each as an ers grid and writes to file
    Args:
        strpath: directory name
        chunks: tuple of integers
        dsmatch: data array to match the directory of rasters to
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
                        
    for file in check_dict:
        ersfile = file.replace('.tif','.ers')
        print(file.replace('.tif','.ers'))
        check_dict[file].rio.to_raster(ersfile, driver='ERS')
        
                
    return check_dict
    
    
def ers_to_tif(strpath, masked=True, chunks=None, dsmatch=None):
    """
    Walks a directory of ers and returns each as an ers geotiff
    Args:
        strpath: directory name
        chunks: tuple of integers
        dsmatch: data array to match the directory of rasters to
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
            if '.ers' in file and '.xml' not in file:
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
                        
    for file in check_dict:
        ersfile = file.replace('.ers','.tif')
        print(file.replace('.ers','.tif'))
        check_dict[file].rio.to_raster(ersfile, driver='GTiff')
        
                
    return check_dict
    
        

def tif_to_img(strpath, masked=True, chunks=None, dsmatch=None):
    """
    Walks a directory of geotiffs and returns each as an img rasterl
    Args:
        strpath: directory name
        chunks: tuple of integers
        dsmatch: data array to reproject match the directory of rasters to
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
                        
    for file in check_dict:
        ersfile = file.replace('.tif','.img')
        print(file.replace('.tif','.img'))
        check_dict[file].rio.to_raster(ersfile, driver='HFA', COMPRESSED='YES')
        
                
    return check_dict
     

def clip_da(da, gdfpath):
    """
    Clips a rioxarray raster by geodataframe polygons
    
    Args:
        da: rioxarray Data Array
        gdfpath: Path to vector polygon dataset
    
    Returns:
        Clipped rioxarray
        
    Examples: 
        schaus = clip_da('dapath', 'gdfpath')
    
    """

    gdf = gpd.read_file(gdfpath)
    clipped = da.rio.clip(gdf.geometry.values, gdf.crs, drop=True, invert=False)
    
    return clipped


def clip_raster(dapath, gdfpath):
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
    Clips a rioxarray by bounding box
    
    Args:
        dapath: Path to raster
        bb: boundingbox coordinates iterable xmin, ymin, xmax, ymax
    
    Returns:
        Clipped rioxarray
        
    Examples: 
        schaus = clip_dabox('dapath', bb)
    
    """

    da = rioxarray.open_rasterio(dapath)
    clipped = da.rio.clip_box(minx = bb[0], miny=bb[1],maxx=bb[2],maxy=bb[3])
    
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
            
            
def rasterize_one(tilow, strpath, da):
    """
    Rasterize a geodataframe to a default one raster
    
    Args:
        tilow: gdf
        strpath: output geotif path
        da: raster for resolution and bounds to match
    
    Returns:
        geotiff to file
        
    Examples: 
        rasterize_one(gdf, outpath, darock)
    
    """

    bb = da.rio.bounds()
    geom=json.dumps(mapping(box(bb[0], bb[1], bb[2], bb[3])))

    print(tilow.crs)
    tilow['TIONE'] = 1

    column = "TIONE"

    out_grid = make_geocube(
        vector_data=tilow,
        measurements=[column],
        resolution=da.rio.resolution(),
        fill = 0,
        geom = geom,
        rasterize_function = partial(rasterize_image, all_touched=True)
    )
    out_grid[column].rio.write_nodata(255, inplace=True)
    out_grid[column]=out_grid[column].astype('uint8')

    out_grid[column].rio.to_raster(strpath, compress='PACKBITS')
    
## TODO
## naive grids in 2D and 3D?
## generic geophysics derivatives via harmonica
## boring github actions things if ever have time

def csv_to_pyvista(csv_file_path):
    """
    Import an X,Y,Z CSV file and convert it to a PyVista mesh.

    Parameters:
    csv_file_path (str): Path to the CSV file containing X,Y,Z coordinates.

    Returns:
    pyvista.PolyData: PyVista mesh object created from the CSV data.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Ensure the CSV has X, Y, and Z columns
        required_columns = ['X', 'Y', 'Z']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("CSV must contain 'X', 'Y', and 'Z' columns")

        # Extract X, Y, Z coordinates
        points = df[required_columns].values

        # Create PyVista mesh from points
        mesh = pv.PolyData(points)

        return mesh

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

### 3D

def df_to_rioxarray(df, data):
    """
    Import a dataframe with x,y columns and convert to raster

    Parameters:
    df - dataframe
    data - column in the dataframe to be used as raster data

    Returns:
    pyvista.PolyData: PyVista mesh object created from the CSV data.
    
    Examples:
    da_grav = df_to_xarray(dfjoin,'gravity')
    """

    data = np.asarray(df[data]).reshape(1,df.y.unique().size,df.x.unique().size)
    da = xr.DataArray(data=data,dims=["band","y","x"],coords={"band":[1],"y":df.y.unique(),"x":df.x.unique()})
    return da
    
    
def df_to_xarray(df, data):
    """
    Import a dataframe with x,y,z columns and convert to raster

    Parameters:
    df - dataframe
    data - column in the dataframe to be used as 3D grid

    Returns:
    pyvista.PolyData: PyVista mesh object created from the CSV data.
    
    Examples:
    da_grav = df_to_xarray(dfjoin,'gravity')
    """
    
    df = df.sort_values(by=["z","y","x"])
    data = np.asarray(df[data]).reshape(df.z.unique().size,df.y.unique().size,df.x.unique().size)
    da = xr.DataArray(data=data,dims=["z","y","x"],coords={"z":df.z.unique(),"y":df.y.unique(),"x":df.x.unique()})

    return da

    
def pad_grid_with_nulls(df, x_min, x_max, y_min, y_max, z_min, z_max, x_step, y_step, z_step):
    """
    Pad a partial grid dataframe with nulls to create a complete 3D grid.
    
    Parameters:
    df (pd.DataFrame): Input dataframe with columns 'x', 'y', 'z', and any other data columns
    x_min, x_max, y_min, y_max, z_min, z_max: Bounding box coordinates
    x_step, y_step, z_step: Step sizes for each dimension
    
    Returns:
    pd.DataFrame: Padded dataframe with nulls for missing grid points
    """
    
    # Create complete grid
    x = np.arange(x_min, x_max + x_step, x_step)
    y = np.arange(y_min, y_max + y_step, y_step)
    z = np.arange(z_min, z_max + z_step, z_step)
    
    complete_grid = pd.DataFrame([(xi, yi, zi) for xi in x for yi in y for zi in z],
                                 columns=['x', 'y', 'z'])
    
    # Merge complete grid with existing data
    merged_df = pd.merge(complete_grid, df, on=['x', 'y', 'z'], how='left')
    
    return merged_df
    
    
def pad_grid_with_nulls2d(df, x_min, x_max, y_min, y_max, x_step, y_step):
    """
    Pad a partial grid dataframe with nulls to create a complete 2d grid.
    
    Parameters:
    df (pd.DataFrame): Input dataframe with columns 'x', 'y', 'z', and any other data columns
    x_min, x_max, y_min, y_max, z_min, z_max: Bounding box coordinates
    x_step, y_step, z_step: Step sizes for each dimension
    
    Returns:
    merged_df: Padded dataframe with nulls for missing grid points
    """
    
    # Create complete grid
    x = np.arange(x_min, x_max + x_step, x_step)
    y = np.arange(y_min, y_max + y_step, y_step)
    
    complete_grid = pd.DataFrame([(xi, yi) for xi in x for yi in y for zi in z], columns=['x', 'y'])
    
    # Merge complete grid with existing data
    merged_df = pd.merge(complete_grid, df, on=['x', 'y', 'z'], how='left')
    
    return merged_df
    
    
def pad_rectilinear_grid_with_nulls(df, x_coords, y_coords, z_coords):
    """
    Pad a partial rectilinear grid dataframe with nulls to create a complete grid.
    
    Parameters:
    df (pd.DataFrame): Input dataframe with columns 'x', 'y', 'z', and any other data columns
    x_coords, y_coords, z_coords: Lists of coordinates for each dimension
    
    Returns:
    merged_df: Padded dataframe with nulls for missing grid points
    """
    
    # Create complete grid
    complete_grid = pd.DataFrame([(x, y, z) for x in x_coords for y in y_coords for z in z_coords],
                                 columns=['x', 'y', 'z'])
    
    # Merge complete grid with existing data
    merged_df = pd.merge(complete_grid, df, on=['x', 'y', 'z'], how='left')
    
    return merged_df
    
    
def xarray_to_geoh5(ds, workspace_path)
    """
    Assume x,y,z are dims in lowercase and that you want z in metres and negative
    
    Parameters:
    ds - xarray dataset
    workspace path - string of location to read/create geoh5 workspace
    
    returns blockmodel for reference - not really useful
    """
    
    with Workspace(workspace_path) as workspace:
        print("using:",workspace.geoh5)

        if 'z' in ds.dims:
            origin = [ds.rio.bounds()[0],ds.rio.bounds()[1],ds.z.min().values]

            xarr =  np.diff(ds.x)
            xarr = np.insert(xarr, 0, 0)
            xarr = np.insert(xarr, -1, 0)
            u_cell_delimiters =  np.cumsum(xarr)

            yarr =  np.diff(ds.y)
            yarr = np.insert(yarr, 0, 0)
            yarr = np.insert(yarr, -1, 0)
            v_cell_delimiters =  np.cumsum(yarr) * -1

            zarr =  np.diff(ds.z)
            zarr = np.insert(zarr, 0, 0)
            zarr = np.insert(zarr, -1, 0)
            z_cell_delimiters =  np.cumsum(zarr)

            if ds.z.min().values > 0 and 1 == 1:
                origin = [ds.rio.bounds()[0],ds.rio.bounds()[1],ds.z.min().values * -1]
                z_cell_delimiters =  z_cell_delimiters * -1

            if max(abs(ds.z.min().values),abs(ds.z.max().values)) < 1000:
                z_cell_delimiters =  z_cell_delimiters * 1000

            blockmodel = BlockModel.create(
                workspace,
                origin=origin,
                u_cell_delimiters=u_cell_delimiters,  # Offsets along u
                v_cell_delimiters=v_cell_delimiters,  # Offsets along v
                z_cell_delimiters=z_cell_delimiters,  # Offsets along z (down)
                rotation=0.0,
                name=key,
            )

            for var in ds.data_vars:
                print(key, var)
                if var != 'spatial_ref':

                    ds[var].values = np.rot90(ds[var].values, k=2, axes=(0, 1))
                    data = ds[var].transpose("y","x","z").values.flatten()

                    print(data.shape, ds[var].shape)

                    print("BLOCKMODEL INFO",blockmodel.n_cells)
                    blockmodel.add_data({
                        var : {"association":"CELL","values": data}
                    })

        else: #2d
            print("NO z dimension")
            pass
        
        return blockmodel    
    
    
