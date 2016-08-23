import numpy as np
import pylab as pl
import netCDF4 as nc
pl.ion()

data = nc.Dataset("test_new.nc")
lon = data.variables["lon"][:]
lat = data.variables["lat"][:]

p = data.variables["level"][:]
p_data = 500.
ip = abs(p-p_data).argmin()

lonx, laty = np.meshgrid(lon, lat)

precip_ls = data.variables["lsp"][0,:,:]
precip_c  = data.variables["cp" ][0,:,:]
omega     = data.variables["w"  ][0,ip,:,:]

mask_m = np.logical_and(np.logical_and(lonx>=230, lonx<=290), np.logical_and(laty>=20, laty<=70))
mask_r = np.logical_and(np.logical_and(lonx>=  5, lonx<= 15), np.logical_and(laty>=40, laty<=50))

precip_ls_m = np.ma.masked_array(precip_ls, mask=~mask_m)
precip_c_m  = np.ma.masked_array(precip_c , mask=~mask_m)
omega_m     = np.ma.masked_array(omega    , mask=~mask_m)

precip_ls_r = np.ma.masked_array(precip_ls, mask=~mask_r)
precip_c_r  = np.ma.masked_array(precip_c , mask=~mask_r)
omega_r     = np.ma.masked_array(omega    , mask=~mask_r)

pl.figure()
pl.subplot(121)
pl.plot(omega_m, precip_ls_m, 'bo')
pl.subplot(122)
pl.plot(omega_r, precip_ls_r, 'ro')

pl.figure()
pl.subplot(121)
pl.plot(omega_m, precip_c_m, 'bo')
pl.subplot(122)
pl.plot(omega_r, precip_c_r, 'ro')
