import pywgrib2_xr as pywgrib2
from pywgrib2_xr.utils import remotepath

in_file = remotepath('nam.t12z.awak3d18.tm00.grib2')
out_file = '/tmp/subset2.grib2'
inv_file = '/tmp/nam.t12z.awak3d18.tm00.inv'

pywgrib2.wgrib(in_file, '-inv', inv_file, '-Match_inv')
match_str = ':(TMP:2 m above ground|[U|V]GRD:10 m above ground):'
pywgrib2.wgrib(in_file, '-i_file', inv_file, '-inv', '/dev/null',
               '-match', match_str, '-grib', out_file)
pywgrib2.free_files(in_file, out_file)
