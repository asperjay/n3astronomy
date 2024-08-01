from astropy.io import fits
import csv

outliers = [1464623,1270774,1463827,1463319,202709,203039,1462759,203220,1270128,694250]


# Open the FITS file
with fits.open('COSMOS2020_CLASSIC_R1_v2.2_p3.fits') as hdul:
    data = hdul[1].data

    subset = []
    indexData = []
    for outlier in outliers:
        print("Index "+str(outlier)+": ")
        print('\tlp_type: '+str(data['lp_type'][outlier]))
        print('\tlp_mass_med: '+str(data['lp_mass_med'][outlier]))
        print('\tlp_SFR_med: '+str(data['lp_SFR_med'][outlier]))
        print('\tlp_sSFR_med: '+str(data['lp_sSFR_med'][outlier]))
