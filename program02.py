import xarray as xr
import matplotlib.pyplot as plt
ds = xr.open_dataset('akw.t12z.grib.grib2',engine='cfgrib')
print(ds)
ds.isel(step=1)['u'].plot()
plt.show()
