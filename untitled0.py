import rasterio
import numpy as np

# CHANGE paths
file1 = r"D:\NW_Imagery\SN5262.tif"
file2 = r"D:\NW_Imagery\SN5263.tif"
output = r"D:\NW_Imagery\outout.tif"

with rasterio.open(file1) as raster1, rasterio.open(file2) as raster2:
    # read bands
    band1 = raster1.read(1)
    band2 = raster2.read(1)
    
    # change dtype because np.sqrt returns float
    profile = raster1.profile
    profile.update(dtype=rasterio.float64)
    
    # CALCULATION
    new_raster = np.sqrt(np.sqrt(band1)) * np.sqrt(band2)
    
    # save the new raster
    with rasterio.open(output, 'w', **profile) as dst:
        dst.write(new_raster.astype(rasterio.float64), 1)